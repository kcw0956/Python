import sys


str1 = "merry christmas"

list1 = [1, 2, 3, 4, 5]
cnt = str1.count('s')

# result = "fuck".join(sorted(str1, reverse=True))
print(list1)


parts = []
for _ in range(len(list1)):
    ch, cnt = input().split()
    parts.append(ch * int(cnt))

result = "".join(parts)
print(result)

























