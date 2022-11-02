
def run_as_main():
  import lists, tuples
  print(f'run as main __name__: {__name__}')
  lists.is_list()
  tuples.is_tuple()

def run_as_import():
  print(f'run as import __name__: {__name__}')


if( __name__ == '__main__' ):
  run_as_main()
else:
  run_as_import()
