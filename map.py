"""
Problem: 정수를 담은 이차원 리스트, mylist가 solution 함수의
		파라미터로 주어집니다. solution 함수가 mylist 각 원소의
		길이를 담은 리스트를 리턴하도록 코드를 작성해주세요.
"""

#Low level style
def solution(mylist):
	answer = []
	for item in mylist:
		answer.append(len(item))
	return answer

#Python style
def solution(mylist):
	return list(map(len, mylist))

"""
Description: map(f, iterable)은 함수(f)와 반복 가능한(iterable) 
			자료형을 입력으로 받는다.
			map은 입력 받은 자료형의 각 요소가 함수 f에 의해 수행된
			결과를 묶어서 리턴하는 함수이다.
"""

