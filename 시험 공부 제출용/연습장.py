import sys

readline = sys.stdin.readline

# N = int(input())
# A, B = map(int, input().split())
#
# arr = list(map(int, input().split()))
#
# board = [list(map(int, input().split())) for _ in range(N)]

ex = 1, 2, 3, 4, 5, 6, 7

print(ex)


arr = list(map(int, input().split()))

total = sum(arr)
mx = max(arr)
mn = min(arr)


count = [0] * 101
for x in arr:
    count[x] += 1