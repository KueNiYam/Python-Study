from itertools import permutations

pool = ['A', 'B', 'C']
print(list(map(''.join, permutations(pool))))
print(list(map(''.join, permutations(pool,2))))