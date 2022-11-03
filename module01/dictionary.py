
print(f"dictionary __name__: {__name__}")

def is_dictionary():   # 'is' stands for intermediate-stuff
  """
  key-value pairs, unordered, mutable
  """
  
  print(f"initialize ---------------------------------------------------------")
  mydict1 = { 'name': 'Maxx', 'age': 28, 'city': 'New York' }
  print(f"mydict1: {mydict1}")

  print(f"initialize using function ------------------------------------------")
  mydict2 = dict( name='Mary', age=37, city='Melbourne' )
  print(f"mydict2: {mydict2}")

  print(f"get values ---------------------------------------------------------")
  val01 = mydict1['name']
  print(f"name: {val01}")
  print(mydict1.get('name'))  # returns 'Maxx'

  print(f"KeyError -----------------------------------------------------------")
  try:
    mydict1['no_key_by_keyname']
  except KeyError as e:
    print(f"KeyError: >>{e} in {mydict1}<<")

  print(f"insert/add new values ----------------------------------------------")
  mydict1['email'] = 'maxx@xyz.com'
  print(mydict1.get('email'))  # prints 'maxx@xyz.com'

  print(f"overwrite existing values ------------------------------------------")
  mydict1['email'] = 'maxx@abc.com'
  print(mydict1.get('email'))  # prints 'maxx@abc.com'

  print(f"remove existing key/value pair -------------------------------------")
  del(mydict1['city'])
  print(mydict1)
  mydict1.pop('age')
  print(mydict1)

  # since python 3.7, popitem removes the last-inserted key/val pair
  mydict1.popitem()  # email was last-insert, see line 29
  print(mydict1)

  print(f"check if key exists ( 2-way: if and try/Except KeyError (see above) ")
  if 'name' in mydict2:   # if not a key, then false, and print() never called
    print(mydict2['name'])

  print(f"loop keys ----------------------------------------------------------")
  print(f"loop thru keys of mydict2: {mydict2}")
  for key in mydict2:
    print(f"  key: {key}")

  key_list = mydict2.keys()
  print(f"key_list: {key_list}, type is {type(key_list)}")
  for key in key_list:
    print(f"  key: {key}")

  print(f"loop vals ----------------------------------------------------------")
  for value in mydict2:
    print(f"  value: {value}")  # NOT work, returns keys

  val_list = mydict2.values()
  print(f"val_list: {val_list}, type is {type(val_list)}")
  for val in val_list:
    print(f"  value: {val}")

  print(f"loop keys and vals -------------------------------------------------")
  for key, val in mydict2.items():
    print(f"item pair: {key}<->{val}")

  print(f"copy ---------------------------------------------------------------")
  mydict2_cpy = mydict2   # copy is same as original
  print(f"mydict2_cpy: {mydict2_cpy}")
  # modify the copy also modifies the original
  mydict2_cpy['phone'] = '212 555 5555'
  print(f"mydict2 original: {mydict2}")

  mydict3 = mydict2.copy()
  mydict4 = dict(mydict3)
  print(mydict3)
  print(mydict4)

  print(f"merge two dictionaries ---------------------------------------------")
  dict_1 = { 'name': 'Sally', 'age': 17, 'email': 'sally@example.com' }
  dict_2 = dict(name='Veronica', age=41, city='New York')
  dict_1.update(dict_2)
  print(f"Update: {dict_1}")


if( __name__ == '__main__' ):
  is_dictionary()
