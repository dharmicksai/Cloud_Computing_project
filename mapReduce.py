import pickle
import time
import json

def map_reduce(file_name , safe_size , start_position , file_size):

  # The input file is opened and only the first SafeSize bytes starting from the starting position is read
  file = open(file_name, 'r')
  file.seek(start_position)
  Lines = file.readlines(safe_size)
  
  if start_position:
    file2 = open(f'intermediateFiles/intermediate-{start_position}.txt' , 'rb')
    wordCount = pickle.load(file2)
  else:
    wordCount = {}

  # The word count for the read lines is calculated and a Python dictionary that contains the word count that is calculated from the previous iterations of the MapReduce algorithm is updated with the latest word count values.
  for line in Lines:
      # remove leading and trailing whitespace
      line = line.strip()
      # split the line into words
      words = line.split()
      # increase counters
      for word in words:
          if word in wordCount.keys():
            wordCount[word] = wordCount[word] + 1
          else:
            wordCount[word] = 1

  # Once the entire text in the input file is processed, the final output is stored in ‘output.txt’ in a plain format without serialization. 
  if file_size<=safe_size+start_position:
    output_file = open('output.txt','w')
    print(f'Storing output in {output_file.name}')
    output_file.write(json.dumps(wordCount))
    output_file.close()
  else:
    output_file = open(f'intermediateFiles/intermediate-{start_position+safe_size}.txt','wb')
  # Word count is serialized and dumped in a file using Pickle.
    print(f'Storing auxilary data in in {output_file.name}')
    pickle.dump(wordCount,output_file)
    output_file.close()

