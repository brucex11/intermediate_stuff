
print(f"In module/file miscues: __name__ == {__name__}")

def is_misque():   # 'is' stands for intermediate-stuff
  """
  
  """

  print(f"try/except template ------------------------------------------------")
  try:
    pass
  except IndexError as e:
    print(f"IndexError: >>{e}<<")
    pass
  else:
    pass
  finally:
    pass

  print(f"FileNotFoundError --------------------------------------------------")
  try:
    file = open('somefile.txt')
  except FileNotFoundError as e:
    print(f"FileNotFoundError: >>{e}<<")
    pass
  else:
    pass
  finally:
    pass

  print(f"IndexError ---------------------------------------------------------")
  t_list = ['Max', 32, 'New York']
  mytuple5 = tuple(t_list)
  # print(f"mytuple5: {mytuple5}")
  # print(f"elems of mytuple5: {mytuple5[0]} {mytuple5[1]} {mytuple5[2]}")

  try:
    idx = 9
    item3 = mytuple5[idx]
    print(f"item3: {item3}")
  except IndexError as e:
    print(f"IndexError: >>{e}, index={idx}<<")
  else:
    pass
  finally:
    pass

  print(f"KeyError -----------------------------------------------------------")
  try:
    my_dict = {'name':'Max'}
    my_dict['age']
  except KeyError as e:
    print(f"KeyError: >>{e}<<")
    pass
  else:
    pass
  finally:
    pass

  print(f"ModuleNotFoundError is a subclass of ImportError -------------------")
  # 

  print(f"NameError ----------------------------------------------------------")
  try:
    a = bb
  except NameError as e:
    print(f"NameError: >>{e}<<")

  print(f"TypeError ----------------------------------------------------------")
  try:
    a = 5 + '10'
  except TypeError as e:
    print(f"TypeError: >>{e}<<")
  else:
    pass
  finally:
    pass

  print(f"ValueError ---------------------------------------------------------")
  try:
    val = 4
    a = [1,2,3]
    a.remove(val)
  except ValueError as e:
    print(f"ValueError: >>{e}, value={val}<<")
    pass
  else:
    pass
  finally:
    pass


#-------------------------------------------------------------------------------
if( __name__ == '__main__' ):
  is_misque()
