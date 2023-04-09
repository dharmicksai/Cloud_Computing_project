import os

# cleans up file instances of intermediatary function invocations
def cleanup():
  # folder path
  dir_path = 'intermediateFiles'
  
  # Iterate directory
  for path in os.listdir(dir_path):
      # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        os.remove(os.path.join(dir_path, path))