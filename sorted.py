"""
보통 사람들은 deep copy와 sort 함수를 이용합니다.
"""

list1 = [3, 2, 1]
list2 = [i for i in list1]
list2.sort()
print(list2)

"""
파이썬의 sorted를 사용해보세요.
"""

list3 = sorted(list1)
print(list3)