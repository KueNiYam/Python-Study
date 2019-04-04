"""
전치행렬 구하기
"""

mylist = [[1,2,3],[4,5,6],[7,8,9]]
ziped = zip(*mylist)
new_list = list(map(list,ziped))
print(new_list)

"""
  zip(*iterables)는 각 iterables의 요소들을 모으는 이터레이터를
만듭니다. 튜플의 이터레이트를 돌려주는데, i 번째 튜플은 각 인자로
전달된 시퀀스나 이터러블의 i번째 요소를 포함합니다.
"""

mylist = [1,2,3]
new_list = [40,50,60]
for i in zip(mylist, new_list):
	print(i)

#사용 예 #1 - 여러 개의 iterable 동시에 순회할 때 사용
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for i, j, k in zip(list1, list2, list3):
	print(i + j + k)

#사용 예 #2 - Key 리스트와 Value 리스트로 딕셔너리 생성하기
"""
파이썬의 zip 함수와 dict 생성자를 이용하면 코드 단 한 줄로, 두 리스트를
  합쳐 딕셔너리로 만들 수 있습니다.
"""
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds))
print(str(answer))