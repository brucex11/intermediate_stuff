
print(f"import_timeit __name__: {__name__}")

import timeit

def is_timeit_tools():   # 'is' stands for intermediate-stuff
  """
  
  """
  print(f"time between list and tuple ----------------------------------------")
  # tuple is faster than list !!
  print(f"list:  {timeit.timeit(stmt='[0, 1, 2, 3, 4, 5]', number=1000000)}" )
  print(f"tuple: {timeit.timeit(stmt='(0, 1, 2, 3, 4, 5)', number=1000000)}" )
  # import_timeit __name__: __main__
  # list:  0.145210099988617
  # tuple: 0.08090850000735372


#-------------------------------------------------------------------------------
if( __name__ == '__main__' ):
  is_timeit_tools()
