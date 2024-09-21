"""this scripts has the walkthorugh function that helps us 
highlight the contents within the specific directory in path"""

from pathlib import Path
import os
path = Path("dummy")
def walk_through_dir(dir_path):
  """Walks through dir_path returning its contents."""
  for dirpath, dirnames, filenames in os.walk(dir_path):
    print(f"There are {len(dirnames)} directories and {len(filenames)} files/images in '{dirpath}'.")

walk_through_dir(path)   ### path is the dir 


"""example output: There are 1 directories and 1 files/images in 'dummy'.
 There are 0 directories and 1 files/images in 'dummy/dum1'."""