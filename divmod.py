from functools import reduce

#Low level style
a = 7
b = 5
print(a//b, a%b)

#Python style
a = 7
b = 5
print(*divmod(a, b))

"""
무조건 divmod()를 사용하는게 좋은 방법은 아니다.
가독성이나, 팀의 코드 스타일에 따라서도 다를 수 있고,
divmod()는 작은 숫자를 다룰 때는 a//b, a%b보다 느리다.
"""

"""
Packing
 - 하나의 변수에 여러 개의 값을 넣는것
Unpacking
 - 패킹된 변수에서 여러 개의 값을 꺼내오는 것
"""

c = (3, 4)
d, e = c
f = d, e

"""
Python Asterisk(*):
 1. 곱셈 및 거듭제곱 연산에 사용할 때
 2. 리스트형 컨테이너 타입의 데이터를 반복 확장하고자 할 때
 3. 가변인자 (Variadic Arguments)를 사용할 때
 4. 컨테이너 타입의 데이터를 Unpacking할 때
"""

#1
2 * 3 # 6

#2
zeros_list = [0] * 100
print(str(zeros_list))

zeros_tuple = (0, ) * 100
print(str(zeros_tuple))

vector_list = [[1, 2, 3]]
print(str(vector_list * 3))

#3
def positional_arguments(*args):
	print(args)

positional_arguments('ming', 'alice', 'tom', 'wilson', 'roy')

def keyword_arguments(**kwargs):
	print(kwargs)

keyword_arguments(first='ming', second='alice', fourth='wilson', third='tom', fifth='roy')

def both_of(*args, **kwargs):
	print(args)
	print(kwargs)

both_of('ming', 'alice', 'tom', fourth='wilson', fifth='roy')

"""
keyword(**kwargs)는 positional(*args) 앞에 올 수 없다.
"""

#4
primes = [2, 3, 5, 7, 11, 13]

def product(*numbers):
	p = reduce(lambda x, y: x * y, numbers)
	return p

print(product(*primes))

print(product(primes))
