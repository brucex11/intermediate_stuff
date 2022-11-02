
print(f"tuples __name__: {__name__}")

def is_tuple():   # 'is' stands for intermediate-stuff
  """
  tuple: ordered, immutable, allows duplicate elements
  similar to list with main difference is that tuple CANNOT be changed
  after its creation!!
  """
  
  mytuple1 = ('Max', 28, 'Boston', 42)
  print(f"mytuple1: {mytuple1}")



if( __name__ == '__main__' ):
  is_tuple()
