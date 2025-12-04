lst = [(2,4), (1,3), (6,8)]
even_tuples = [t for t in lst if all(x % 2 == 0 for x in t)]
print(even_tuples)