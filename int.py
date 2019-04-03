"""
arr[A:B:C]의 의미는, index A부터 index B까지 C의 간격으로
  배열을 만들라는 말이다.
"""

arr = range(10)
print(*arr)

arr[::2] # 처음부터 끝까지 두 칸 간격으로
print(*arr[::2])

arr[1::2] # index 1부터 끝까지 두 칸 간격으로
print(*arr[1::2])

arr[::-1] # 처음부터 끝까지 -1칸 간격으로(== 역순으로)
print(*arr[::-1])

arr[::-2] # 처음부터 끝까지 -2칸 간격으로(== 역순, 두 칸 간격)
print(*arr[::-2])

arr[3::-1] # index 3부터 끝까지 -1칸 간격으로(== 역순으로)
print(*arr[3::-1])

arr[1:6:2] # index 1부터 index 6까지 두 칸 간격으로
print(*arr[1:6:2])

"""
파이썬의 int(x, base = 10) 함수는 진법 변환을 지원합니다.
"""
num = '3212'
base = 5
answer = int(num, base)
print(answer)