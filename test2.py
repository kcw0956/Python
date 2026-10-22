import sys

# input = sys.stdin.readline

# s = input().strip()
# a = input().strip()

# print("hello")
# print("hello","fuck", "hiihihhihihi", sep = ", ")
# print(s)
# print(a)

# n = int(input())
# a, b = map(int, input().split())

# arr = list(map(int, input().split()))

# input = sys.stdin.readline

# n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)] #board를 생성하게 되는 구조 리스트를 받아서 []를 감싸라는 구조여서 

arr2 = [int[input()] for _ in range(5)]
print(arr)

list2 = [i for i in range(5)] #5번 돌면서 i를 요소로 채워준다 0 1 2 3 4 5

listSqure = [i * i for i in range(5)] # 제곱 

list3 = [0 for i in range(5)]

num = int(input())

board = [[0] * num for _ in range(num)]


