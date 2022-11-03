def is_list():   # 'is' stands for intermediate-stuff
  """
  list: ordered, mutable, allows duplicate elements
  """
  
  print(f"init a list with 5 elements all set to 0 ---------------------------")
  zero_list = [0] * 5
  pass

  a_list = [1,2,'text', ['abc','def']]
  pass   # set the breakpoint here in order to see a_list in WATCH pane

  one = a_list[1]
  pass

  print(f"create an empty list and append and pop ----------------------------")
  mylist2 = list()   # list is empty
  # mylist2.append(8,9,11,13)  # syntax error
  mylist2.append(8)  # len = 1
  mylist2.append(9)  # len = 2
  mylist2.append(11)  # len = 3

  pass
  mylist2.pop()  # len = 2, returns last element and removes it from list
  pass
  mylist2.insert( 1, 'blueberry')   # insert BEFORE index 1 such that insertion
                                    # is NOW at index == 1
  pass

  print(f"iterate ------------------------------------------------------------")
  for elem in a_list:
    print(f"elem: '{elem}'")
  
  print(f"check/find element in list -----------------------------------------")
  if( 'text' in a_list ):
    print(f"YES")
  if( 1 in a_list ):
    print(f"YES")

  print(f"length of list -----------------------------------------------------")
  len_a_list = len(a_list)
  pass

  print(f"remove element -----------------------------------------------------")
  print(f"1. a_list: {a_list}")
  elem_item = a_list.remove( 2 )  # '2' IS in the list, but elem_item = None
  # print(f"elem_item: {elem_item}")  # elem_item = None
  print(f"2. a_list: {a_list}")
  pass

  print(f"reverse (in place) -------------------------------------------------")
  rev = a_list.reverse()  # rev = None, a_list is mutable therefore is reversed
  print(f"3. a_list: {a_list}")
  pass
  a_list.reverse()  # back to original
  a_list[::-1]
  print(f"4. a_list: {a_list}")

  print(f"sort into new list -------------------------------------------------")
  sort_list = [4,3,1,-1,-5,10]
  new_sort = sorted(sort_list)
  pass
  print(f"sort (in place) ----------------------------------------------------")
  sort_list.sort()   # sort_list after sort(): [-5, -1, 1, 3, 4, 10]
  print(f"sort_list after sort(): {sort_list}")
  pass

  print(f"concatenate two lists with '+' -------------------------------------")
  ml1 = [0] * 5
  ml2 = [1] * 5
  ml3 = ml1 + ml2
  print(f"ml3: {ml3}")
  ml4 = ml2 + ml1
  print(f"ml4: {ml4}")
  #  ml3: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
  #  ml4: [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

  print(f"slicing with ':' ---------------------------------------------------")
  slice_list = [0,1,2,3,4,5,6,7,8,9]
  b_list = slice_list[1:5]
  print(f"b_list: {b_list}")  # b_list: [1, 2, 3, 4]
  b_list = slice_list[:5]
  print(f"b_list: {b_list}")  # b_list: [0, 1, 2, 3, 4]
  b_list = slice_list[5:]
  print(f"b_list: {b_list}")  # b_list: [5, 6, 7, 8, 9]

  print(f"slice with step size -----------------------------------------------")
  step_list = slice_list[::1]  # step defaults to 1
  print(f"step_list: {step_list}")  # step_list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  step_list = slice_list[::2]  # get every-other
  print(f"step_list: {step_list}")  # step_list: [0, 2, 4, 6, 8]

  print(f"assignment: use '=' and both lists are referencing the same list ---")
  print(f"therefore, use .copy() method for distinct list objects/instances. -")
  list_org = ['banana','cherry','apple']
  list_cpy = list_org
  print(f"list_org = list_cpy: {list_org} = {list_cpy}")
  list_cpy.append( 'lemon' )
  print(f"list_org = list_cpy: {list_org} = {list_cpy}")
  list_cpy = list_org.copy()
  list_cpy.append('orange')
  print(f"list_org: {list_org}")
  print(f"list_cpy: {list_cpy}")

  print(f"two more ways to make an actual copy -------------------------------")
  list_cpy2 = list_org[:]  # slice
  print(f"list_cpy2: {list_cpy2}")
  list_cpy3 = list(list_org)  # method with list as argument
  print(f"list_cpy3: {list_cpy3}")
  
  print(f"list comprehension: elegant and fast way to create a new list ------")
  # from an existing list but is expensive per CPU cycle time, it is slow.
  zz = [1,2,3,4,5,6]
  print(f"zz: {zz}")
  yy = [i*i for i in zz]  # square each element
  print(f"yy = zz squared: {yy}")
  xx = [i*-1 for i in zz]  # inverse each element
  print(f"xx = inverse of zz: {xx}")

  print(f"list comprehension -------------------------------------------------")
  a_list = [1,2,3,4,5]
  c = [x*2 for x in a_list]
  print(a_list)
  print(c)



if( __name__ == '__main__' ):
  is_list()
