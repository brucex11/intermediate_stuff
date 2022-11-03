
print(f"import_sys __name__: {__name__}")

import sys

def is_sys_tools():   # 'is' stands for intermediate-stuff
  """
  
  """
  
  print(f"getsizeof ----------------------------------------------------------")
  # note size diff between list and tuple objects
  my_list = [0,1,2,'hello',True]
  my_tuple = (0,1,2,'hello',True)
  print(f"sys.getsizeof(my_list) bytes: {sys.getsizeof(my_list)}")
  print(f"sys.getsizeof(my_tuple) bytes: {sys.getsizeof(my_tuple)}")




if( __name__ == '__main__' ):
  is_sys_tools()
