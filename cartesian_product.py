"""
곱집합

: 'ABCD', 'xy
 -> 'Ax', 'Ay', 'Bx', 'By', 'Cx', 'Cy', 'Dx', 'Dy'
"""

import itertools

iterable1 = 'ABCD'
iterable2 = ('x', 'z')
iterable3 = [1, 2, 3, 4]
answer = itertools.product(iterable1, iterable2, 
						   iterable3)

print(list(answer))