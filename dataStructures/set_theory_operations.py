#Union 
set_A = {1, 2, 3, 4}
set_B = {'a', 'b', 'c', 'd'}

print(set_A | set_B)
print(set_A.union(set_B))
print(set_B.union(set_A))

#Intersection
set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}

print(set_A & set_B)
print(set_A.intersection(set_B))

#Difference
print(set_A - set_B)
print(set_B - set_A)
print(set_A.difference(set_B))

#Symmetric Difference
print(set_A.symmetric_difference(set_B))
sym_diff_method = set_A ^ set_B
print(sym_diff_method)
sym_diff_method = set_B ^ set_A
print(sym_diff_method)