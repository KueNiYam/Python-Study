# 2차원 리스트를 1차원 리스트로 만들기

my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])
print(answer)

# 방법 2 - itertools.chain
import itertools
answer = list(itertools.chain.from_iterable(my_list))
print(answer)

# 방법 3 - itertools와 unpacking
import itertools
answer = list(itertools.chain(*my_list))
print(answer)

# 방법 4 - list comprehension
answer = [element for array in my_list for element in array]
print(answer)

# 방법 5 - reduce 함수 이용 1
from functools import reduce
answer = list(reduce(lambda x, y: x+y, my_list))
print(answer)

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
answer = list(reduce(operator.add, my_list))