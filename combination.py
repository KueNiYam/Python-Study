from itertools import combinations

pool = ['A', 'B', 'C']
print(list(map(''.join, combinations(pool, 2))))
print(list(map(''.join, combinations(pool, 3))))