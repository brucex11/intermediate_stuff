
print(f"tuples __name__: {__name__}")

def is_tuple():   # 'is' stands for intermediate-stuff
  """
  tuple: ordered, immutable, allows duplicate elements
  similar to list with main difference is that tuple CANNOT be changed
  after its creation!!
  """
  
  mytuple1 = ( 'Max', 28, 'Boston', 42000 )
  print(f"mytuple1: {mytuple1}")

  # tuple with single element, add comma to end of list ------------------------
  mytuple2 = "Mean",  # parens not needed
  print(f"mytuple2: {mytuple2}")
  print(f"type(mytuple2): {type(mytuple2)}")
  mytuple3 = ("Mean",)
  print(f"mytuple3: {mytuple3}")
  print(f"type(mytuple3): {type(mytuple3)}")

  # tuple function -------------------------------------------------------------
  mytuple4 = tuple(['Max', 32, 'New York'])
  print(f"mytuple4: {mytuple4}")
  t_list = ['Max', 32, 'New York']
  mytuple5 = tuple(t_list)
  print(f"mytuple5: {mytuple5}")

  # elements -------------------------------------------------------------------
  print(f"elems of mytuple5: {mytuple5[0]} {mytuple5[1]} {mytuple5[2]}")
  try:
    idx = 5
    item3 = mytuple5[idx]
    print(f"item3: {item3}")
  except IndexError as e:
    print(f"IndexError: >>{e}, index={idx}<<")
  else:
    pass
  finally:
    pass

  # negative index values reference the end of the tuple (just like list) ------
  idx = -1
  print(f"mytuple5[{idx}]: {mytuple5[idx]}")
  idx -= 1
  print(f"mytuple5[{idx}]: {mytuple5[idx]}")

  # TypeError: 'tuple' does not support reassignment ---------------------------
  try:
    mytuple5[0] = 'Timmy'
  except TypeError as e:
    print(f"TypeError: >>{e}<<")

  # iterate --------------------------------------------------------------------
  for i in mytuple4:
    print(f"mytuple val: {i}")

  # check/find element in tuple ------------------------------------------------
  if( 'Max' in mytuple5 ):
    print(f"YES in TUPLE")
  if( 1 in mytuple5 ):
    print(f"YES in TUPLE")
  else:
    print(f"NOT in TUPLE")

  # length of tuple ------------------------------------------------------------
  mytuple6 = ('a', 'p', 'p', 'l', 'e')
  len_mytuple6 = len(mytuple6)
  print(f"length mytuple6: {len_mytuple6}")

  # count num elements ---------------------------------------------------------
  letter = 'p'
  count_mytuple6 = mytuple6.count(letter)
  print(f"COUNT of letter '{letter}' in apple: {count_mytuple6}")

  # first index of -------------------------------------------------------------
  print(f"index of first letter '{letter}' in apple: {mytuple6.index(letter)}")

  # ValueError for index of element that does not exist ------------------------
  try:
    mytuple6.index('z')
  except ValueError as e:
    print(f"ValueError: >>{e}<<")
    pass
  else:
    pass
  finally:
    pass

  # convert tuple to list ------------------------------------------------------
  mylist6 = list(mytuple6)
  mytuple7 = tuple(mylist6)

  # slicing with ':' -----------------------------------------------------------
  slice_tuple = (0,1,2,3,4,5,6,7,8,9)
  b_tuple = slice_tuple[1:5]
  print(f"b_tuple: {b_tuple}")  # b_tuple: [1, 2, 3, 4]
  b_tuple = slice_tuple[:5]
  print(f"b_tuple: {b_tuple}")  # b_tuple: [0, 1, 2, 3, 4]
  b_tuple = slice_tuple[5:]
  print(f"b_tuple: {b_tuple}")  # b_tuple: [5, 6, 7, 8, 9]

  # slice with step size -------------------------------------------------------
  step_tuple = slice_tuple[::1]  # step defaults to 1
  print(f"step_tuple: {step_tuple}")  # step_tuple: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  step_tuple = slice_tuple[::2]  # get every-other
  print(f"step_tuple: {step_tuple}")  # step_tuple: [0, 2, 4, 6, 8]

  # reverse (in place) ---------------------------------------------------------
  b_tuple[::-1]
  print(f"reversed b_tuple: {b_tuple}")

  # return comma-delimited variable names --------------------------------------
  print(mytuple1)
  try:
    name, age, city = mytuple1
    print(f"{name} {age} {city}")
  except ValueError as e:
    print(f"ValueError: >>{e}<<")
  finally:
    name, age, city, salary = mytuple1  # must match num elements
    print(f"{name} {age} {city} {salary}")

  # get elements with * operator to be saved into list
  print(slice_tuple)
  i1, *i2, i3 = slice_tuple
  print(f"{i1} {i2} {i3}")


#-------------------------------------------------------------------------------
if( __name__ == '__main__' ):
  is_tuple()
