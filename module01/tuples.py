
print(f"tuples __name__: {__name__}")

def is_tuple():   # 'is' stands for intermediate-stuff
  """
  tuple: ordered, immutable, allows duplicate elements
  similar to list with main difference is that tuple CANNOT be changed
  after its creation!!
  """
  
  mytuple1 = ('Max', 28, 'Boston', 42)
  print(f"mytuple1: {mytuple1}")

  # tuple with single element, add comma to end of list
  mytuple2 = "Mean",  # parens not needed
  print(f"mytuple2: {mytuple2}")
  print(f"type(mytuple2): {type(mytuple2)}")
  mytuple3 = ("Mean",)
  print(f"mytuple3: {mytuple3}")
  print(f"type(mytuple3): {type(mytuple3)}")

  # tuple function
  mytuple4 = tuple(['Max', 32, 'New York'])
  print(f"mytuple4: {mytuple4}")
  t_list = ['Max', 32, 'New York']
  mytuple5 = tuple(t_list)
  print(f"mytuple5: {mytuple5}")

  # elements
  print(f"elems of mytuple5: {mytuple5[0]} {mytuple5[1]} {mytuple5[2]}")
  try:
    item3 = mytuple5[3]
    print(f"item3: {item3}")
  except IndexError:
    print(f"ERROR")
  else:
    pass
  finally:
    pass




if( __name__ == '__main__' ):
  is_tuple()
