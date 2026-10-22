A, B = map(int, input().split())
print(A //B)
print(A % B)

nums = list(map(int, input().split()))
average = sum(nums)/ len(nums)

nums = list(map(int, input().split()))
repeat = 0

result = 0

for n in nums:
    if n % 2 == 1:
        result += n

print(max(nums))

n = input()
print(n[::-1]) #뒤집기 

n = input() # 문자로 받기

sum = 0
for i in n:
    sum += int(i)

year = int(input())

if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(1)
else:
    print(0)

nums = list(map(int, input().split()))

nums.sort()

print(nums[len(nums)//2])

arr = list(map(int, input().split()))
count = [0] * 101
for i in arr:
    count[i] += 1

max_count = max(count)

for i in range(100, -1, -1):
    if count[i] == max_count:
        print(i)
        break

from collections import Counter

print(Counter(arr).most_common())