
print(f"lambda_funcs __name__: {__name__}")


def is_lambda_funcs():   # 'is' stands for intermediate-stuff
  """
  lambda is an anonymous function.  It takes the arguments, evaluates the
      expression, and returns a result.
  
  lambda is used as an argument to higher-order functions, meaning functions
      that take (other) functions as arguments.

  lambda is used in built-in functions:
      * sorted map
      * filter
      * reduce

  syntax:  lambda arguments: expression
  example:  add10 = lambda x: x + 10

  'lambda' is keyword
  """
  
  print(f"basic syntax with one argument -------------------------------------")
  add10 = lambda x: x + 10   # add10 is now a function
  result = add10(5)
  print(f"lambda add10(5) result: {result}")

  # equivalent function to add10 above -----------------------------------------
  def add10_func(x):
    return x + 10
  
  result = add10_func(5)
  print(f"func add10_func(5) result: {result}")

  print(f"basic syntax with two arguments ------------------------------------")
  mult = lambda x,y: x * y
  result = mult(3,4)
  print(f"lambda mult(3,4) result: {result}")

  print(f"sorted example -----------------------------------------------------")
  points2D = [(15,1), (1,2), (5,-1), (10,4)]   # type is list, contains tuples
  points2D_sorted = sorted( points2D )
  print(f"points2D:               {points2D}")
  print(f"points2D_sorted by 'x': {points2D_sorted}")
  # by default, sorted uses the first element of the tuple to sort, and note
  # that the 'x' coord of the points are now in numerical order:
  # points2D:        [(15, 1), (1, 2), (5, -1), (10, 4)]
  # points2D_sorted: [(1, 2), (5, -1), (10, 4), (15, 1)]

  # spec a 'rule' on how to sort where said rule is a FUNCTION, ie, the 'key'
  # so, sort on the 'y' coord. 'y' is the tuple's index=1
  points2D_sorted = sorted( points2D, key=lambda j: j[1] )
  print(f"points2D_sorted by 'y': {points2D_sorted}")
  # and therefore the default 'x' coord is at index=0
  points2D_sorted = sorted( points2D, key=lambda j: j[0] )
  print(f"points2D_sorted by 'x': {points2D_sorted}")

  # equivalent function
  def sort_by_y_coord(point):
    return point[1]
  # use in sorted:
  points2D_sorted = sorted( points2D, key=sort_by_y_coord )
  print(f"points2D_sorted by 'y': {points2D_sorted}")

  # sort by sum of 'x' and 'y' coords
  points2D_sorted = sorted( points2D, key=lambda point: point[0] + point[1] )
  print(f"points2D_sorted by 'x+y': {points2D_sorted}")

  print(f"map function - transforms each element with a function -------------")
  # syntax:  map( func, sequence )
  a_list = [1,2,3,4,5]
  print(f"a_list: {a_list}")
  b_map = map( lambda x: x*2, a_list )
  print(f"b_map: {b_map}")
  print(f"convert to list for print")
  b_list = list(b_map)
  print(f"b_list: {b_list}")

  print(f"list comprehension -------------------------------------------------")
  c = [x*2 for x in a_list]
  print(a_list)
  print(c)

  print(f"filter function ----------------------------------------------------")
  # syntax:  filter( func, sequence )
  # returns all values for which the function evaluates to True
  a_list = [1,2,3,4,5,6]
  b_filtered = filter( lambda x: x%2, a_list )  # returns odd nums
  print(b_filtered)
  print(f"convert to list for print")
  b_list = list(b_filtered)
  print(f"b_list: {b_list}")
  b_filtered = filter( lambda x: x%2==0, a_list )  # returns even nums
  print(b_filtered)
  print(f"convert to list for print")
  b_list = list(b_filtered)
  print(f"b_list: {b_list}")

  print(f"filter function equivalent list comprehension ----------------------")
  c = [x for x in a_list if x%2==0]
  print(c)

  print(f"reduce function (from functools import reduce) ---------------------")
  from functools import reduce
  # syntax:  reduce( func, sequence )
  product_a = reduce( lambda x,y: x*y, a_list )  # returns product of all in list
  print(a_list)
  print(f"product of all in list above: {product_a}")


#-------------------------------------------------------------------------------
if( __name__ == '__main__' ):
  is_lambda_funcs()
