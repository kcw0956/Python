from collections import deque, Counter, defaultdict
import heapq
import bisect
import math

# -----------------------------
# 1. 기본 입출력
# -----------------------------
# n = int(input())
# a, b = map(int, input().split())
# arr = list(map(int, input().split()))

# 올림/내림: math.ceil(3.14) → 4, math.floor(3.78) → 3제곱/제곱근: math.pow(x, y) ($x^y$), math.sqrt(x) ($\sqrt{x}$)팩토리얼/최대공약수: math.factorial(5) → 120, math.gcd(12, 18) → 6상수: math.pi (원주율), math.e (자연상수)

# 0.1 + 0.2 -> 근삿값이 나와서 일치하지 않음 a==b 대신 math.isclose(a,b) 사용
n = 5
arr = [3, 1, 4, 1, 5]

print("합:", sum(arr))
print("최댓값:", max(arr))
print("최솟값:", min(arr))
print("정렬:", sorted(arr))
print("역정렬:", sorted(arr, reverse=True))


# -----------------------------
# 2. 반복문, 조건문
# -----------------------------
for x in arr:
    if x % 2 == 0:
        print(x, "짝수")
    else:
        print(x, "홀수")

for i in range(len(arr)):
    print(i, arr[i])

for i, x in enumerate(arr):
    print("인덱스:", i, "값:", x)


# -----------------------------
# 3. 문자열 처리
# -----------------------------
s = "hello python world"

print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.replace("python", "coding"))
print(s.split())
print("-".join(s.split()))

# 문자 개수 세기
cnt = Counter(s)
print(cnt["o"])

# 문자열 뒤집기
print(s[::-1])

# 알파벳만 추출
only_alpha = "".join(ch for ch in s if ch.isalpha())
print(only_alpha)

# 숫자 문자열 처리
num_str = "12345"
digits = list(map(int, num_str))
print(digits)


# -----------------------------
# 4. 리스트 컴프리헨션
# -----------------------------
squares = [x * x for x in arr]
evens = [x for x in arr if x % 2 == 0]
print(squares)
print(evens)

matrix = [[0] * 3 for _ in range(3)]
print(matrix)


# -----------------------------
# 5. 딕셔너리, 집합
# -----------------------------
d = defaultdict(int)

for x in arr:
    d[x] += 1

print(dict(d))

unique = set(arr)
print(unique)

if 3 in unique:
    print("3 있음")


# -----------------------------
# 6. 정렬 key 사용
# -----------------------------
words = ["banana", "a", "apple", "kiwi"]

print(sorted(words))                 # 사전순
print(sorted(words, key=len))         # 길이순
print(sorted(words, key=lambda x: (len(x), x)))  # 길이순 후 사전순

pairs = [(3, "c"), (1, "b"), (1, "a")]
print(sorted(pairs, key=lambda x: (x[0], x[1])))


# -----------------------------
# 7. 스택
# -----------------------------
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

while stack:
    print("pop:", stack.pop())


# 괄호 검사
def is_valid_parentheses(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0

print(is_valid_parentheses("({[]})"))
print(is_valid_parentheses("({[})"))


# -----------------------------
# 8. 큐
# -----------------------------
q = deque()

q.append(1)
q.append(2)
q.append(3)

while q:
    print("popleft:", q.popleft())


# -----------------------------
# 9. BFS
# -----------------------------
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}

def bfs(start):
    visited = set()
    q = deque([start])
    visited.add(start)

    order = []

    while q:
        now = q.popleft()
        order.append(now)

        for nxt in graph[now]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)

    return order

print("BFS:", bfs(1))


# -----------------------------
# 10. DFS 재귀
# -----------------------------
def dfs(now, visited, order):
    visited.add(now)
    order.append(now)

    for nxt in graph[now]:
        if nxt not in visited:
            dfs(nxt, visited, order)

order = []
dfs(1, set(), order)
print("DFS:", order)


# -----------------------------
# 11. 격자 탐색 BFS
# -----------------------------
grid = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 1]
]

def grid_bfs(sr, sc):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    count = 0

    while q:
        r, c = q.popleft()
        count += 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    q.append((nr, nc))

    return count

print("연결된 칸 수:", grid_bfs(0, 0))


# -----------------------------
# 12. 투 포인터
# 연속 부분합이 target인 구간 찾기
# -----------------------------
nums = [1, 2, 3, 2, 5]
target = 5

left = 0
current_sum = 0
answer = 0

for right in range(len(nums)):
    current_sum += nums[right]

    while current_sum > target:
        current_sum -= nums[left]
        left += 1

    if current_sum == target:
        answer += 1

print("부분합 target 개수:", answer)


# -----------------------------
# 13. 누적합
# -----------------------------
arr = [1, 2, 3, 4, 5]
prefix = [0]

for x in arr:
    prefix.append(prefix[-1] + x)

# 구간 [l, r] 합, 0-indexed
l, r = 1, 3
range_sum = prefix[r + 1] - prefix[l]
print("구간합:", range_sum)


# -----------------------------
# 14. 이진 탐색
# -----------------------------
arr = [1, 3, 5, 7, 9]

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(binary_search(arr, 7))

# bisect 사용
print(bisect.bisect_left(arr, 5))
print(bisect.bisect_right(arr, 5))


# -----------------------------
# 15. 힙 / 우선순위 큐
# -----------------------------
heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

while heap:
    print("heap pop:", heapq.heappop(heap))

# 최대 힙처럼 쓰기
max_heap = []
for x in [5, 1, 3]:
    heapq.heappush(max_heap, -x)

while max_heap:
    print("max heap pop:", -heapq.heappop(max_heap))


# -----------------------------
# 16. 소수 판별
# -----------------------------
def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True

print(is_prime(17))
print(is_prime(20))


# -----------------------------
# 17. 최대공약수, 최소공배수
# -----------------------------
a, b = 12, 18

g = math.gcd(a, b)
l = a * b // g

print("gcd:", g)
print("lcm:", l)


# -----------------------------
# 18. 완전탐색
# -----------------------------
arr = [1, 2, 3]
result = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        result.append((arr[i], arr[j]))

print("두 개 고르기:", result)


# -----------------------------
# 19. 재귀 팩토리얼
# -----------------------------
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# -----------------------------
# 20. 자주 쓰는 실전 함수
# -----------------------------
def solution_example(scores):
    """
    점수 리스트를 받아서:
    1. 평균 이상 점수만 고르고
    2. 내림차순 정렬하고
    3. 중복 제거하고
    4. 문자열로 반환
    """
    avg = sum(scores) / len(scores)

    filtered = []

    for score in scores:
        if score >= avg:
            filtered.append(score)

    filtered = sorted(set(filtered), reverse=True)

    return " ".join(map(str, filtered))

print(solution_example([80, 90, 70, 90, 100]))