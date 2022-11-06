print(f"In module/file raises: __name__ == {__name__}")

def is_raise():   # 'is' stands for intermediate-stuff
  """
  
  """


  print(f"AssertionError -----------------------------------------------------")
  try:
    x = -5
    assert( x >= 0 ), "x is not positive, x = " + str(x)
  except AssertionError as e:
    print(f"AssertionError: >>{e}<<")
    pass
  else:
    pass
  finally:
    pass

  print(f"raise with 'if' ----------------------------------------------------")
  try:
    x = -5
    if x < 0:
      raise Exception( "variable 'x' should be positive" )
  except Exception as e:
    print(f"Exception: >>{e}<<")
    pass
  else:
    pass
  finally:
    print(f"invert negative num: {x}")
    x *= -1
    print(f"x is now = {x}")


#-------------------------------------------------------------------------------
if( __name__ == '__main__' ):
  is_raise()
