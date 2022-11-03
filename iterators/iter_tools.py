
print(f"iter_tools __name__: {__name__}")

import sys

def is_iter_tools():   # 'is' stands for intermediate-stuff
  """
  The itertools module is a collection of tools for handling iterators.
  Iterators are data types that can be used in a for-loop.
  The most common iterator is the list.

  itertools: product, permutations, combinations, accumulate, groupby, infinite
  """
  
  print(f"product (from itertools import product) ----------------------------")
  from itertools import product
  a_list = [1,2]
  b_list = [3]
  prod = product(a_list, b_list)
  print(f"a_list: {a_list}")
  print(f"b_list: {b_list}")
  print(f"product: {prod}")
  print(f"convert to list for print")
  p_list = list(prod)
  print(f"p_list: {p_list}")

  print(f"product with repeat=2 ----------------------------------------------")
  prod = product(a_list, b_list, repeat=2)
  p_list = list(prod)
  print(f"p_list: {p_list}")

  print(f"permutations (from itertools import permutations) ------------------")
  from itertools import permutations
  a_list = [1,2,3]
  print(f"a_list: {a_list}")
  perm = permutations(a_list)
  print(f"perm: {perm}")
  print(f"convert to list for print")
  p_list = list(perm)
  print(f"p_list - full: {p_list}")
  perm = permutations(a_list, 2)
  p_list = list(perm)
  print(f"p_list - length=2: {p_list}")

  print(f"combinations (from itertools import combinations) ------------------")
  from itertools import combinations
  a_list = [1,2,3,4]
  print(f"a_list: {a_list}")
  comb = combinations(a_list, 2)
  print(f"comb: {comb}")
  print(f"convert to list for print")
  c_list = list(comb)
  print(f"c_list: {c_list}")



if( __name__ == '__main__' ):
  is_iter_tools()
