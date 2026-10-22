import sys
input = sys.stdin.readline

test_case = int(input())

for T in range(test_case):
    average = 0
    sum = 0
    arr = list(map(int, input().split()))

    for i in range(len(arr)):
        sum += arr[i]
        average = round(sum / len(arr))

    print(f"#{T + 1} {average}")