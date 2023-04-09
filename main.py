import os 
import time
from mapReduce import map_reduce
from cleanup import cleanup

# SafeSize is the maximum number of bytes that can be processed by a single serverless function before it times out. This parameter ensures that a function is never terminated abruptly by the service provider
safe_size = int(1e6)

#input file
input_file_name = 'input.txt'

#removes all file instances of function invocations
cleanup()

#read file
file_size = os.path.getsize(input_file_name)

print(f"Input file size is {file_size} bytes.")

start = time.time()

# A number of iterations are performed over the input file, and in each iteration, the MapReduce algorithm is performed over a particular portion of the input text. The number of iterations is decided based on the size of the file and the SafeSize, whereas the starting position of each iteration of the MapReduce algorithm is decided based on the SafeSize
for i in range(int((file_size-1)/safe_size) +1):
  start_position = i*safe_size
  map_reduce(input_file_name , safe_size , start_position , file_size)

time_elapsed = time.time() - start

#print the time taken for the particular input file
print(f"Total time taken =  {time_elapsed} seconds.")


