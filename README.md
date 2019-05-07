# Python-Study
## 1. 설명
"파이썬을 파이썬답게" 공부  
<https://programmers.co.kr/learn/courses/4008>

## 2. 목록  

    * divmod  
    * int  
    * ljust, center, rjust  
    * string 모듈  
    * sorted  
    * zip  
    * map  
    * join  
    * sequence type의 * 연산  
    * product  
    * from_iterable  
    * combinations, permutations  
    * Counter  
    * List comprehension의 if문  
    * swap  
    * binary search  
    * class의 자동 string casting  
    * inf  
    * 파일 입출력 간단하게 하기  

------------------------------------------------------------------------------------------------------------------

## divmod
몫과 나머지

    a = 7
    b = 5
    print( *divmod(a, b) )

## int
n진법으로 표기된 string을 10진법 숫자로 변환하기

    # 예시) 5진법으로 적힌 문자열'3212'를 10진법으로 바꾸기
    num = '3212'
    base = 5
    answer = int(num, base)

## ljust, center, rjust  
문자열 정렬하기

    s = 'abc'
    n = 7
    s.ljust(n)
    s.center(n)
    s.rjust(n)

## string 모듈  
 - 모든 대문자를
 - 또는 모든 소문자를
 - 또는 모든 대소문자를
 - 또는 숫자를
 
 가져오는 방법
 
    import string
    
    string.ascii_lowercase # 소문자
    string.ascii_uppercase # 대문자
    string.ascii_letters # 대소문자 모두
    string.digits # 숫자

## sorted  
원본을 유지한 채, 정렬된 리스트 구하기

    list1 = [3, 2, 1]
    list2 = sorted(list1)

## zip  

    mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    new_list = list(map(list, zip(*mylist)))
    
**파이썬 3 한글 번역 - zip**에 따르면
> zip(\*iterables)는 각 iterables의 요소들을 모으는 이터레이터를 만듭니다.
> 반환 값은 튜플의 이터레이터를 돌려주는데, i 번째 튜플은 각 인자로 전달된 시퀀스나 이터러블의 i 번째 요소를 포함합니다.

영어 원문:
> Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.

    mylist = [1, 2, 3]
    new_list = [40, 50, 60]
    for i in zip(mylist, new_list):
        print(i)
        
    (1, 40)
    (2, 50)
    (3, 60)
    
**사용 예 #1 - 여러개의 Iterable 동시에 순회할 때 사용**

    list1 = [1, 2, 3, 4]
    list2 = [100, 120, 30, 300]
    list3 = [392, 2, 33, 1]
    answer = []
    for i, j, k in zip(list1, list2, list3):
        print(i + j + k)

**사용 예 #2 - Key 리스트와 Value 리스트로 딕셔너리 생성하기**

    animals = ['cat', 'dog', 'lion']
    sounds = ['meow', 'woof', 'roar']
    answer = dict(zip(animal, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}

## map  

    list1 = ['1', '100', '33']
    list2 = list(map(int, list1))

## join  

    my_list = ['1', '100', '33']
    answer = ''.join(my_list)

## sequence type의 * 연산  

    n = int(input().strip())
    answer = [123, 456] * n

## product  
Cartesian Product(데카르트 곱, 곱집합)

    import itertools
    
    iterable1 = 'ABCD'
    iterable2 = 'xy'
    iterable3 = '1234'
    itertools.product(iterable1, iterable2, iterable3)

## from_iterable  
2차원 리스트를 1차원 리스트로 만들기

    # 방법 1 - sum 함수
    answer = sum(my_list, [])
    
    # 방법 2 - itertools.chain
    import itertools
    list(itertools.chain.from_iterable(my_list))
    
    # 방법 3 - itertools와 unpacking
    import itertools
    list(itertools.chain(*my_list))
    
    # 방법 4 - list comprehension 이용
    [element for array in my_list for element in array]
    
    # 방법 5 - reduce 함수 이용 1
    from functools import reduce
    list(reduce(lambda x, y: x+y, my_list))
    
    # 방법 6 - reduce 함수 이용 2
    from functools import reduce
    import operator
    list(reduce(operator.add, my_list))

## combinations, permutations
순열과 조합

    import itertools
    
    pool = ['A', 'B', 'C']
    itertools.permutations(pool)
    itertools.permutations(pool, 2)
    itertools.combinations(pool, 2)

## Counter  

    import collections
    
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
    answer = collections.Counter(my_list)
    
    print(answer[1]) # = 4
    print(answer[3]) # = 3
    print(answer[100]) # = 0

## List comprehension의 if문  

    mylist = [3, 2, 6, 7]
    answer = [i**2 for i in mylist if i % 2 == 0]

## swap  

    a, b = 3, 4
    a, b = b, a

## binary search 

    import bisect
    
    mylist = [1, 2, 3, 7, 9, 11, 13]
    print(bisect.bisect(mylist, 3))

## class의 자동 string casting  

    class Coord(object):
        def __init__ (self, x, y):
            self.x, self.y = x, y
        def __str__ (self):
            return '({}, {})'. format(self.x, self.y)
            
    point = Coord(1, 2)
    print(point)

## inf  

    man_val = float('inf')
    min_val = float('-inf')

## 파일 입출력 간단하게 하기 

    with open('myfile.txt') as file:
        for line in file,.readlines():
            print(line.strip().split('\t'))
            
**파이썬의 with - as**
1. 파일을 close 하지 않아도 됩니다: with - as 블록이 졸료되면 파일이 자동으로 close 됩니다.
2. readlines가 EOF까지만 읽으므로, while 문 안에서 EOF를 체크할 필요가 없습니다.
⨳ with - as 구문은 파일 뿐만 아니라 socket이나 http 등에서도 사용할 수 있습니다.
