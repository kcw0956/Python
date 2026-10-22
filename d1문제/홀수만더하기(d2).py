import sys
input = sys.stdin.readline

repeat = int(input())

for i in range(repeat):
    sum = 0
    num = 1
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        if (arr[i] % 2) != 0:
            sum += arr[i]
    print(f"#{num} {sum}")
    num += 1
    

