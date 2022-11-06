print(f"In module/file raises: __name__ == {__name__}")

def is_strings():   # 'is' stands for intermediate-stuff
  """
  
  """

  text = 'EPIC'

  print(f"Leading and Trailing -----------------------------------------------")
  print(f'{text:#<20}')  # trail
  print(f'{text:_>20}')  # lead
  print(f'{text:.^20}')  # lead and trail



#-------------------------------------------------------------------------------
if( __name__ == '__main__' ):
  is_strings()
