# SSAFY 코테 벼락치기: SWEA D2/D3 Python 풀이 40선

문제 원문은 SWEA에서 확인하고, 여기서는 시험장에서 바로 떠올릴 핵심 접근과 제출용 Python 코드를 정리했다.

입출력은 SWEA 기본 형식인 `#tc answer`를 기준으로 작성했다. 일부 D3 고전 문제는 테스트케이스가 항상 10개인 형식이라 그에 맞췄다.

---

## 문제 내용 한줄 요약

아래는 원문을 그대로 옮긴 것이 아니라, 문제 상황과 요구사항을 빠르게 파악할 수 있게 요약한 내용이다.

### D2 빠른 요약

| 번호 | 제목 | 문제 내용 요약 |
|---|---|---|
| 1284 | 수도 요금 경쟁 | 두 수도 회사의 요금 계산 방식이 주어질 때, 사용량 W에 대해 더 저렴한 요금을 구한다. |
| 1288 | 새로운 불면증 치료법 | N의 배수를 차례로 보면서 0부터 9까지 모든 숫자를 처음 보게 되는 시점의 수를 구한다. |
| 1926 | 간단한 369게임 | 1부터 N까지 출력하되, 숫자에 3/6/9가 들어가면 개수만큼 박수를 `-`로 출력한다. |
| 1940 | 가랏! RC카! | 가속, 감속, 유지 명령이 초 단위로 주어질 때 최종 이동 거리를 계산한다. |
| 1945 | 간단한 소인수분해 | 주어진 수를 2, 3, 5, 7, 11의 지수 형태로 분해해 각 지수를 출력한다. |
| 1946 | 간단한 압축 풀기 | 문자와 반복 횟수들이 주어질 때 압축을 풀고, 결과를 10글자씩 끊어 출력한다. |
| 1948 | 날짜 계산기 | 같은 해의 두 날짜가 주어질 때, 시작일과 종료일을 포함한 날짜 수를 구한다. |
| 1954 | 달팽이 숫자 | N x N 배열에 1부터 N²까지 달팽이 모양으로 숫자를 채워 출력한다. |
| 1959 | 두 개의 숫자열 | 길이가 다른 두 숫자열을 겹쳐 보며, 같은 위치끼리 곱한 합의 최댓값을 구한다. |
| 1961 | 숫자 배열 회전 | N x N 숫자 배열을 90도, 180도, 270도 회전한 결과를 한 줄씩 나란히 출력한다. |
| 1966 | 숫자를 정렬하자 | 주어진 숫자들을 오름차순으로 정렬해 출력한다. |
| 1970 | 쉬운 거스름돈 | 금액 N을 큰 화폐 단위부터 사용해 각 지폐/동전이 몇 개 필요한지 구한다. |
| 1974 | 스도쿠 검증 | 9 x 9 스도쿠 판이 올바른 완성 상태인지 행, 열, 3 x 3 영역을 검사한다. |
| 1976 | 시각 덧셈 | 12시간제 시각 두 개를 더한 결과의 시와 분을 구한다. |
| 1979 | 어디에 단어가 들어갈 수 있을까 | 0과 1로 된 퍼즐에서 길이 K짜리 단어가 정확히 들어갈 수 있는 자리 수를 센다. |
| 1983 | 조교의 성적 매기기 | 중간, 기말, 과제 점수로 총점을 계산해 K번째 학생의 학점을 구한다. |
| 1984 | 중간 평균값 구하기 | 10개 수에서 최댓값과 최솟값을 하나씩 제외한 평균을 반올림해 구한다. |
| 1986 | 지그재그 숫자 | 1부터 N까지 홀수는 더하고 짝수는 빼는 식의 결과를 구한다. |
| 1989 | 초심자의 회문 검사 | 주어진 문자열이 앞뒤로 같은 회문인지 판별한다. |
| 2001 | 파리 퇴치 | N x N 영역에서 M x M 파리채로 잡을 수 있는 파리 수의 최댓값을 구한다. |

### D3 빠른 요약

| 번호 | 제목 | 문제 내용 요약 |
|---|---|---|
| 1206 | View | 건물 높이 배열에서 좌우 2칸보다 높은 세대만 조망권이 있다고 보고 총 조망 세대 수를 구한다. |
| 1208 | Flatten | 가장 높은 곳의 상자를 낮은 곳으로 옮기는 작업을 반복한 뒤 최고점과 최저점 차이를 구한다. |
| 1213 | String | 긴 문자열에서 특정 패턴 문자열이 몇 번 등장하는지 센다. |
| 1215 | 회문1 | 8 x 8 글자판에서 지정된 길이의 가로/세로 회문 개수를 구한다. |
| 1216 | 회문2 | 100 x 100 글자판에서 가로/세로로 만들 수 있는 가장 긴 회문의 길이를 구한다. |
| 1220 | Magnetic | 자성체들이 놓인 테이블에서 위아래 자성체가 서로 막혀 생기는 교착 상태 개수를 센다. |
| 1221 | GNS | 영어처럼 생긴 특수 숫자 문자열들을 정해진 숫자 순서대로 정렬한다. |
| 1225 | 암호생성기 | 8개 숫자를 큐처럼 돌리며 1부터 5까지 반복해서 빼다가 0 이하가 되면 암호를 완성한다. |
| 1228 | 암호문1 | 주어진 암호문 리스트에 여러 삽입 명령을 적용한 뒤 앞 10개를 출력한다. |
| 1229 | 암호문2 | 암호문 리스트에 삽입과 삭제 명령을 적용한 뒤 앞 10개를 출력한다. |
| 1230 | 암호문3 | 암호문 리스트에 삽입, 삭제, 추가 명령을 적용한 뒤 앞 10개를 출력한다. |
| 1240 | 단순 2진 암호코드 | 2진 문자열 속 56비트 암호코드를 해독하고 검증식이 맞으면 숫자 합을 출력한다. |
| 1289 | 원재의 메모리 복구하기 | 모두 0인 메모리를 목표 비트열로 바꾸기 위해 필요한 최소 뒤집기 횟수를 구한다. |
| 1493 | 수의 새로운 연산 | 특수한 좌표 기반 숫자 배치에서 두 수를 좌표로 바꿔 더한 뒤 다시 숫자로 변환한다. |
| 1860 | 진기의 최고급 붕어빵 | 붕어빵 생산 주기와 손님 도착 시간이 주어질 때, 모든 손님에게 바로 줄 수 있는지 판단한다. |
| 2805 | 농작물 수확하기 | 마름모 모양 수확 영역 안에 있는 농작물 가치의 합을 구한다. |
| 2814 | 최장 경로 | 무방향 그래프에서 같은 정점을 두 번 방문하지 않는 가장 긴 경로 길이를 구한다. |
| 3032 | 홍준이의 숫자 놀이 | 두 정수 A, B에 대해 확장 유클리드 계수 x, y를 구한다. |
| 3131 | 100만 이하의 모든 소수 | 1,000,000 이하의 모든 소수를 오름차순으로 출력한다. |
| 3431 | 준환이의 운동관리 | 권장 운동 시간 범위와 실제 운동 시간이 주어질 때 부족 시간 또는 초과 여부를 출력한다. |

---

## D2 20문제

### 1. 1284. 수도 요금 경쟁

문제 내용: 두 수도 회사의 요금 계산 방식이 주어질 때, 사용량 W에 대해 더 저렴한 요금을 구한다.

풀이 핵심: 핵심은 P사 요금과 Q사 요금을 각각 계산해서 더 싼 값을 고르는 것이다. Q사는 사용량이 R 이하이면 기본요금 Q, 초과하면 초과량마다 S를 더한다.

```python
T = int(input())
for tc in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    a = P * W
    b = Q if W <= R else Q + (W - R) * S
    print(f"#{tc} {min(a, b)}")
```

### 2. 1288. 새로운 불면증 치료법

문제 내용: N의 배수를 차례로 보면서 0부터 9까지 모든 숫자를 처음 보게 되는 시점의 수를 구한다.

풀이 핵심: `N, 2N, 3N...`을 보면서 나온 숫자를 집합에 넣는다. 0부터 9까지 모두 보면 종료한다.

```python
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    seen = set()
    k = 0
    while len(seen) < 10:
        k += 1
        seen.update(str(N * k))
    print(f"#{tc} {N * k}")
```

### 3. 1926. 간단한 369게임

문제 내용: 1부터 N까지 출력하되, 숫자에 3/6/9가 들어가면 개수만큼 박수를 `-`로 출력한다.

풀이 핵심: 숫자 문자열에 3, 6, 9가 몇 개 있는지 세고, 있으면 그 개수만큼 `-`를 출력한다.

```python
N = int(input())
ans = []
for x in range(1, N + 1):
    s = str(x)
    cnt = s.count("3") + s.count("6") + s.count("9")
    ans.append("-" * cnt if cnt else s)
print(*ans)
```

### 4. 1940. 가랏! RC카!

문제 내용: 가속, 감속, 유지 명령이 초 단위로 주어질 때 최종 이동 거리를 계산한다.

풀이 핵심: 속도는 음수가 될 수 없다. 명령마다 속도를 갱신하고, 매초 이동거리에 현재 속도를 더한다.

```python
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    speed = 0
    dist = 0
    for _ in range(N):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            speed += cmd[1]
        elif cmd[0] == 2:
            speed = max(0, speed - cmd[1])
        dist += speed
    print(f"#{tc} {dist}")
```

### 5. 1945. 간단한 소인수분해

문제 내용: 주어진 수를 2, 3, 5, 7, 11의 지수 형태로 분해해 각 지수를 출력한다.

풀이 핵심: 주어진 수가 2, 3, 5, 7, 11로 몇 번 나누어지는지 센다.

```python
T = int(input())
primes = [2, 3, 5, 7, 11]
for tc in range(1, T + 1):
    N = int(input())
    counts = []
    for p in primes:
        c = 0
        while N % p == 0:
            N //= p
            c += 1
        counts.append(c)
    print(f"#{tc}", *counts)
```

### 6. 1946. 간단한 압축 풀기

문제 내용: 문자와 반복 횟수들이 주어질 때 압축을 풀고, 결과를 10글자씩 끊어 출력한다.

풀이 핵심: 문자와 반복 횟수를 받아 전체 문자열을 만든 뒤 10글자씩 끊어 출력한다.

```python
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    s = ""
    for _ in range(N):
        ch, cnt = input().split()
        s += ch * int(cnt)

    print(f"#{tc}")
    for i in range(0, len(s), 10):
        print(s[i:i + 10])
```

### 7. 1948. 날짜 계산기

문제 내용: 같은 해의 두 날짜가 주어질 때, 시작일과 종료일을 포함한 날짜 수를 구한다.

풀이 핵심: 월별 일수를 누적해서 두 날짜가 몇 일 차이인지 구한다. 문제는 시작일과 종료일을 모두 포함하므로 `+1`을 한다.

```python
T = int(input())
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def day_of_year(month, day):
    return sum(days[:month]) + day

for tc in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    ans = day_of_year(m2, d2) - day_of_year(m1, d1) + 1
    print(f"#{tc} {ans}")
```

### 8. 1954. 달팽이 숫자

문제 내용: N x N 배열에 1부터 N²까지 달팽이 모양으로 숫자를 채워 출력한다.

풀이 핵심: 방향 배열을 두고, 다음 칸이 범위 밖이거나 이미 채워졌으면 방향을 바꾼다.

```python
T = int(input())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    r = c = d = 0
    for num in range(1, N * N + 1):
        board[r][c] = num
        nr, nc = r + dr[d], c + dc[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= N or board[nr][nc]:
            d = (d + 1) % 4
            nr, nc = r + dr[d], c + dc[d]
        r, c = nr, nc

    print(f"#{tc}")
    for row in board:
        print(*row)
```

### 9. 1959. 두 개의 숫자열

문제 내용: 길이가 다른 두 숫자열을 겹쳐 보며, 같은 위치끼리 곱한 합의 최댓값을 구한다.

풀이 핵심: 짧은 배열을 긴 배열 위에서 한 칸씩 밀며 곱의 합 최댓값을 구한다.

```python
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M:
        A, B = B, A
        N, M = M, N

    best = -10**18
    for start in range(M - N + 1):
        total = 0
        for i in range(N):
            total += A[i] * B[start + i]
        best = max(best, total)
    print(f"#{tc} {best}")
```

### 10. 1961. 숫자 배열 회전

문제 내용: N x N 숫자 배열을 90도, 180도, 270도 회전한 결과를 한 줄씩 나란히 출력한다.

풀이 핵심: 90도 회전은 `arr[N-1-r][c]`, 180도는 `arr[N-1-r][N-1-c]`, 270도는 `arr[r][N-1-c]` 패턴으로 만들 수 있다.

```python
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    print(f"#{tc}")
    for r in range(N):
        a = "".join(arr[N - 1 - c][r] for c in range(N))
        b = "".join(arr[N - 1 - r][N - 1 - c] for c in range(N))
        c = "".join(arr[c][N - 1 - r] for c in range(N))
        print(a, b, c)
```

### 11. 1966. 숫자를 정렬하자

문제 내용: 주어진 숫자들을 오름차순으로 정렬해 출력한다.

풀이 핵심: Python에서는 `sort()`로 충분하다. SWEA D2에서는 정렬 구현보다 입출력 실수가 더 흔하다.

```python
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print(f"#{tc}", *nums)
```

### 12. 1970. 쉬운 거스름돈

문제 내용: 금액 N을 큰 화폐 단위부터 사용해 각 지폐/동전이 몇 개 필요한지 구한다.

풀이 핵심: 큰 단위 지폐부터 몫을 세고 나머지를 다음 단위로 넘긴다.

```python
T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, T + 1):
    N = int(input())
    ans = []
    for m in money:
        ans.append(N // m)
        N %= m
    print(f"#{tc}")
    print(*ans)
```

### 13. 1974. 스도쿠 검증

문제 내용: 9 x 9 스도쿠 판이 올바른 완성 상태인지 행, 열, 3 x 3 영역을 검사한다.

풀이 핵심: 각 행, 열, 3x3 박스가 1부터 9까지 정확히 한 번씩 나오는지 확인한다.

```python
T = int(input())
target = set(range(1, 10))

for tc in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    ok = True

    for i in range(9):
        if set(board[i]) != target:
            ok = False
        if set(board[r][i] for r in range(9)) != target:
            ok = False

    for sr in range(0, 9, 3):
        for sc in range(0, 9, 3):
            box = set()
            for r in range(sr, sr + 3):
                for c in range(sc, sc + 3):
                    box.add(board[r][c])
            if box != target:
                ok = False

    print(f"#{tc} {1 if ok else 0}")
```

### 14. 1976. 시각 덧셈

문제 내용: 12시간제 시각 두 개를 더한 결과의 시와 분을 구한다.

풀이 핵심: 분을 더해서 60 이상이면 시간으로 올리고, 시간은 12를 넘어가면 12시간제로 맞춘다.

```python
T = int(input())
for tc in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1 + h2
    m = m1 + m2
    h += m // 60
    m %= 60
    while h > 12:
        h -= 12
    print(f"#{tc} {h} {m}")
```

### 15. 1979. 어디에 단어가 들어갈 수 있을까

문제 내용: 0과 1로 된 퍼즐에서 길이 K짜리 단어가 정확히 들어갈 수 있는 자리 수를 센다.

풀이 핵심: 행과 열에서 연속된 1의 길이를 세고, 길이가 정확히 K인 구간만 카운트한다. 배열 양끝 처리를 위해 0을 하나 붙이면 편하다.

```python
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for r in range(N):
        cnt = 0
        for c in range(N + 1):
            if c < N and board[r][c] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0

    for c in range(N):
        cnt = 0
        for r in range(N + 1):
            if r < N and board[r][c] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0

    print(f"#{tc} {ans}")
```

### 16. 1983. 조교의 성적 매기기

문제 내용: 중간, 기말, 과제 점수로 총점을 계산해 K번째 학생의 학점을 구한다.

풀이 핵심: 총점을 계산하고 내림차순 정렬한 뒤 K번째 학생의 등수를 찾는다. 같은 등급은 N/10명씩 배정된다.

```python
T = int(input())
grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    scores = []
    for idx in range(1, N + 1):
        mid, final, hw = map(int, input().split())
        total = mid * 0.35 + final * 0.45 + hw * 0.20
        scores.append((total, idx))

    scores.sort(reverse=True)
    for rank, (_, idx) in enumerate(scores):
        if idx == K:
            ans = grades[rank // (N // 10)]
            break
    print(f"#{tc} {ans}")
```

### 17. 1984. 중간 평균값 구하기

문제 내용: 10개 수에서 최댓값과 최솟값을 하나씩 제외한 평균을 반올림해 구한다.

풀이 핵심: 최댓값과 최솟값을 제외하고 평균을 반올림한다. Python의 `round()`는 은행가 반올림이라, SWEA에서는 `int(x + 0.5)`가 안전하다.

```python
T = int(input())
for tc in range(1, T + 1):
    nums = list(map(int, input().split()))
    nums.remove(max(nums))
    nums.remove(min(nums))
    avg = sum(nums) / len(nums)
    print(f"#{tc} {int(avg + 0.5)}")
```

### 18. 1986. 지그재그 숫자

문제 내용: 1부터 N까지 홀수는 더하고 짝수는 빼는 식의 결과를 구한다.

풀이 핵심: 1부터 N까지 홀수는 더하고 짝수는 뺀다.

```python
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ans = 0
    for x in range(1, N + 1):
        ans += x if x % 2 else -x
    print(f"#{tc} {ans}")
```

### 19. 1989. 초심자의 회문 검사

문제 내용: 주어진 문자열이 앞뒤로 같은 회문인지 판별한다.

풀이 핵심: 문자열과 뒤집은 문자열이 같으면 회문이다.

```python
T = int(input())
for tc in range(1, T + 1):
    s = input().strip()
    print(f"#{tc} {1 if s == s[::-1] else 0}")
```

### 20. 2001. 파리 퇴치

문제 내용: N x N 영역에서 M x M 파리채로 잡을 수 있는 파리 수의 최댓값을 구한다.

풀이 핵심: 모든 MxM 영역의 합을 완전탐색한다. N이 작아서 단순 이중 반복으로 충분하다.

```python
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    best = 0

    for r in range(N - M + 1):
        for c in range(N - M + 1):
            total = 0
            for i in range(M):
                for j in range(M):
                    total += board[r + i][c + j]
            best = max(best, total)

    print(f"#{tc} {best}")
```

---

## D3 20문제

### 1. 1206. View

문제 내용: 건물 높이 배열에서 좌우 2칸보다 높은 세대만 조망권이 있다고 보고 총 조망 세대 수를 구한다.

풀이 핵심: 각 건물은 좌우 2칸 안의 가장 높은 건물보다 높을 때만 조망권이 생긴다. 차이만큼 더한다.

```python
for tc in range(1, 11):
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(2, N - 2):
        near = max(h[i - 2], h[i - 1], h[i + 1], h[i + 2])
        if h[i] > near:
            ans += h[i] - near
    print(f"#{tc} {ans}")
```

### 2. 1208. Flatten

문제 내용: 가장 높은 곳의 상자를 낮은 곳으로 옮기는 작업을 반복한 뒤 최고점과 최저점 차이를 구한다.

풀이 핵심: 가장 높은 상자에서 하나 빼고 가장 낮은 상자에 하나 더하는 작업을 dump번 반복한다.

```python
for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump):
        hi = boxes.index(max(boxes))
        lo = boxes.index(min(boxes))
        boxes[hi] -= 1
        boxes[lo] += 1

    print(f"#{tc} {max(boxes) - min(boxes)}")
```

### 3. 1213. String

문제 내용: 긴 문자열에서 특정 패턴 문자열이 몇 번 등장하는지 센다.

풀이 핵심: 패턴의 시작 위치를 모두 검사한다. `str.count()`도 가능하지만, 직접 슬라이싱하면 겹치는 경우까지 자연스럽게 처리된다.

```python
for _ in range(10):
    tc = int(input())
    pattern = input().strip()
    text = input().strip()
    n = len(pattern)
    ans = 0
    for i in range(len(text) - n + 1):
        if text[i:i + n] == pattern:
            ans += 1
    print(f"#{tc} {ans}")
```

### 4. 1215. 회문1

문제 내용: 8 x 8 글자판에서 지정된 길이의 가로/세로 회문 개수를 구한다.

풀이 핵심: 8x8 배열에서 길이 N인 가로/세로 문자열을 모두 잘라 회문인지 확인한다.

```python
for tc in range(1, 11):
    N = int(input())
    board = [input().strip() for _ in range(8)]
    ans = 0

    for r in range(8):
        for c in range(8 - N + 1):
            s = board[r][c:c + N]
            if s == s[::-1]:
                ans += 1

    for c in range(8):
        for r in range(8 - N + 1):
            s = "".join(board[r + i][c] for i in range(N))
            if s == s[::-1]:
                ans += 1

    print(f"#{tc} {ans}")
```

### 5. 1216. 회문2

문제 내용: 100 x 100 글자판에서 가로/세로로 만들 수 있는 가장 긴 회문의 길이를 구한다.

풀이 핵심: 100x100 배열에서 가능한 길이를 큰 것부터 검사한다. 처음 발견한 길이가 정답이므로 바로 종료해도 된다.

```python
for _ in range(10):
    tc = int(input())
    board = [input().strip() for _ in range(100)]
    ans = 1

    found = False
    for length in range(100, 0, -1):
        for r in range(100):
            for c in range(100 - length + 1):
                s = board[r][c:c + length]
                if s == s[::-1]:
                    ans = length
                    found = True
                    break
            if found:
                break
        if found:
            break

        for c in range(100):
            for r in range(100 - length + 1):
                s = "".join(board[r + i][c] for i in range(length))
                if s == s[::-1]:
                    ans = length
                    found = True
                    break
            if found:
                break
        if found:
            break

    print(f"#{tc} {ans}")
```

### 6. 1220. Magnetic

문제 내용: 자성체들이 놓인 테이블에서 위아래 자성체가 서로 막혀 생기는 교착 상태 개수를 센다.

풀이 핵심: 열마다 위에서 아래로 보며 1을 만난 뒤 2를 만나면 교착 상태 1개다. 0은 무시한다.

```python
for tc in range(1, 11):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for c in range(N):
        has_north = False
        for r in range(N):
            if board[r][c] == 1:
                has_north = True
            elif board[r][c] == 2 and has_north:
                ans += 1
                has_north = False

    print(f"#{tc} {ans}")
```

### 7. 1221. GNS

문제 내용: 영어처럼 생긴 특수 숫자 문자열들을 정해진 숫자 순서대로 정렬한다.

풀이 핵심: 문자 숫자를 실제 순서 인덱스로 바꾸어 정렬한 뒤 다시 출력한다.

```python
order = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
rank = {word: i for i, word in enumerate(order)}

T = int(input())
for _ in range(T):
    tc, n = input().split()
    nums = input().split()
    nums.sort(key=lambda x: rank[x])
    print(tc)
    print(*nums)
```

### 8. 1225. 암호생성기

문제 내용: 8개 숫자를 큐처럼 돌리며 1부터 5까지 반복해서 빼다가 0 이하가 되면 암호를 완성한다.

풀이 핵심: 큐에서 맨 앞 값을 꺼내 1,2,3,4,5를 반복해서 빼고 뒤에 넣는다. 0 이하가 되면 0을 넣고 종료한다.

```python
from collections import deque

for _ in range(10):
    tc = int(input())
    q = deque(map(int, input().split()))
    dec = 1

    while True:
        x = q.popleft() - dec
        if x <= 0:
            q.append(0)
            break
        q.append(x)
        dec = dec + 1 if dec < 5 else 1

    print(f"#{tc}", *q)
```

### 9. 1228. 암호문1

문제 내용: 주어진 암호문 리스트에 여러 삽입 명령을 적용한 뒤 앞 10개를 출력한다.

풀이 핵심: 명령 `I x y ...`는 x 위치에 y개 숫자를 삽입한다. 앞에서부터 10개만 출력한다.

```python
for tc in range(1, 11):
    N = int(input())
    arr = input().split()
    M = int(input())
    cmd = input().split()

    i = 0
    while i < len(cmd):
        if cmd[i] == "I":
            x = int(cmd[i + 1])
            y = int(cmd[i + 2])
            data = cmd[i + 3:i + 3 + y]
            arr[x:x] = data
            i += 3 + y

    print(f"#{tc}", *arr[:10])
```

### 10. 1229. 암호문2

문제 내용: 암호문 리스트에 삽입과 삭제 명령을 적용한 뒤 앞 10개를 출력한다.

풀이 핵심: 암호문1에 삭제 명령 `D x y`가 추가된다. 삭제는 슬라이스를 빈 리스트로 바꾸면 된다.

```python
for tc in range(1, 11):
    N = int(input())
    arr = input().split()
    M = int(input())
    cmd = input().split()

    i = 0
    while i < len(cmd):
        op = cmd[i]
        if op == "I":
            x = int(cmd[i + 1])
            y = int(cmd[i + 2])
            data = cmd[i + 3:i + 3 + y]
            arr[x:x] = data
            i += 3 + y
        elif op == "D":
            x = int(cmd[i + 1])
            y = int(cmd[i + 2])
            arr[x:x + y] = []
            i += 3

    print(f"#{tc}", *arr[:10])
```

### 11. 1230. 암호문3

문제 내용: 암호문 리스트에 삽입, 삭제, 추가 명령을 적용한 뒤 앞 10개를 출력한다.

풀이 핵심: 삽입, 삭제, 추가 명령을 모두 처리한다. `A y ...`는 뒤에 붙이면 된다.

```python
for tc in range(1, 11):
    N = int(input())
    arr = input().split()
    M = int(input())
    cmd = input().split()

    i = 0
    while i < len(cmd):
        op = cmd[i]
        if op == "I":
            x = int(cmd[i + 1])
            y = int(cmd[i + 2])
            data = cmd[i + 3:i + 3 + y]
            arr[x:x] = data
            i += 3 + y
        elif op == "D":
            x = int(cmd[i + 1])
            y = int(cmd[i + 2])
            arr[x:x + y] = []
            i += 3
        else:
            y = int(cmd[i + 1])
            data = cmd[i + 2:i + 2 + y]
            arr.extend(data)
            i += 2 + y

    print(f"#{tc}", *arr[:10])
```

### 12. 1240. 단순 2진 암호코드

문제 내용: 2진 문자열 속 56비트 암호코드를 해독하고 검증식이 맞으면 숫자 합을 출력한다.

풀이 핵심: 오른쪽 끝의 1을 찾으면 그 앞 56비트가 암호다. 7비트씩 숫자로 바꾸고 검증식을 통과하면 합을 출력한다.

```python
code = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    rows = [input().strip() for _ in range(N)]
    bits = ""

    for row in rows:
        if "1" in row:
            end = row.rfind("1")
            bits = row[end - 55:end + 1]
            break

    nums = [code[bits[i:i + 7]] for i in range(0, 56, 7)]
    check = (nums[0] + nums[2] + nums[4] + nums[6]) * 3 + nums[1] + nums[3] + nums[5] + nums[7]
    ans = sum(nums) if check % 10 == 0 else 0
    print(f"#{tc} {ans}")
```

### 13. 1289. 원재의 메모리 복구하기

문제 내용: 모두 0인 메모리를 목표 비트열로 바꾸기 위해 필요한 최소 뒤집기 횟수를 구한다.

풀이 핵심: 왼쪽부터 목표 비트를 보며 현재 상태와 다르면 한 번 뒤집어야 한다. 뒤집은 뒤 현재 상태가 그 비트가 된다.

```python
T = int(input())
for tc in range(1, T + 1):
    target = input().strip()
    cur = "0"
    ans = 0
    for ch in target:
        if ch != cur:
            ans += 1
            cur = ch
    print(f"#{tc} {ans}")
```

### 14. 1493. 수의 새로운 연산

문제 내용: 특수한 좌표 기반 숫자 배치에서 두 수를 좌표로 바꿔 더한 뒤 다시 숫자로 변환한다.

풀이 핵심: 숫자를 좌표로 바꾸고, 두 좌표를 더한 뒤 다시 숫자로 바꾼다. 대각선 번호를 기준으로 누적 개수를 계산한다.

```python
def num_to_pos(n):
    diag = 1
    before = 0
    while before + diag < n:
        before += diag
        diag += 1
    offset = n - before
    return offset, diag - offset + 1

def pos_to_num(x, y):
    diag = x + y - 1
    before = diag * (diag - 1) // 2
    return before + x

T = int(input())
for tc in range(1, T + 1):
    p, q = map(int, input().split())
    x1, y1 = num_to_pos(p)
    x2, y2 = num_to_pos(q)
    ans = pos_to_num(x1 + x2, y1 + y2)
    print(f"#{tc} {ans}")
```

### 15. 1860. 진기의 최고급 붕어빵

문제 내용: 붕어빵 생산 주기와 손님 도착 시간이 주어질 때, 모든 손님에게 바로 줄 수 있는지 판단한다.

풀이 핵심: 손님 도착 시간을 정렬한다. i번째 손님이 도착한 시각까지 만들어진 붕어빵 수가 i명보다 적으면 불가능하다.

```python
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    times = sorted(map(int, input().split()))
    ok = True

    for i, t in enumerate(times, start=1):
        made = (t // M) * K
        if made < i:
            ok = False
            break

    print(f"#{tc} {'Possible' if ok else 'Impossible'}")
```

### 16. 2805. 농작물 수확하기

문제 내용: 마름모 모양 수확 영역 안에 있는 농작물 가치의 합을 구한다.

풀이 핵심: 가운데 행까지는 더하는 범위를 넓히고, 이후에는 줄인다. 맨해튼 거리로 판단해도 된다.

```python
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input().strip())) for _ in range(N)]
    mid = N // 2
    ans = 0

    for r in range(N):
        dist = abs(mid - r)
        for c in range(dist, N - dist):
            ans += farm[r][c]

    print(f"#{tc} {ans}")
```

### 17. 2814. 최장 경로

문제 내용: 무방향 그래프에서 같은 정점을 두 번 방문하지 않는 가장 긴 경로 길이를 구한다.

풀이 핵심: 정점 수가 작으므로 모든 정점에서 DFS를 시작한다. 방문한 정점 수의 최댓값이 답이다.

```python
T = int(input())

def dfs(v, length):
    global best
    best = max(best, length)
    for nxt in graph[v]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, length + 1)
            visited[nxt] = False

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    best = 1
    visited = [False] * (N + 1)
    for start in range(1, N + 1):
        visited[start] = True
        dfs(start, 1)
        visited[start] = False

    print(f"#{tc} {best}")
```

### 18. 3032. 홍준이의 숫자 놀이

문제 내용: 두 정수 A, B에 대해 확장 유클리드 계수 x, y를 구한다.

풀이 핵심: 확장 유클리드 알고리즘으로 `A*x + B*y = gcd(A, B)`를 만족하는 x, y를 구한다. 이 문제에서는 gcd가 1인 케이스의 계수를 출력한다.

```python
def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    g, x, y = egcd(A, B)
    print(f"#{tc} {x} {y}")
```

### 19. 3131. 100만 이하의 모든 소수

문제 내용: 1,000,000 이하의 모든 소수를 오름차순으로 출력한다.

풀이 핵심: 에라토스테네스의 체로 1,000,000 이하 소수를 모두 구해 출력한다. 이 문제는 테스트케이스 번호 출력이 없다.

```python
N = 1_000_000
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(N ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False

ans = [str(i) for i in range(2, N + 1) if is_prime[i]]
print(" ".join(ans))
```

### 20. 3431. 준환이의 운동관리

문제 내용: 권장 운동 시간 범위와 실제 운동 시간이 주어질 때 부족 시간 또는 초과 여부를 출력한다.

풀이 핵심: 운동 시간이 L보다 작으면 부족한 시간을, L 이상 U 이하이면 0을, U보다 크면 -1을 출력한다.

```python
T = int(input())
for tc in range(1, T + 1):
    L, U, X = map(int, input().split())
    if X < L:
        ans = L - X
    elif X <= U:
        ans = 0
    else:
        ans = -1
    print(f"#{tc} {ans}")
```

---

## 벼락치기 순서 추천

1. D2: `1954`, `1974`, `1979`, `2001`을 먼저 풀어 2차원 배열 감각을 잡는다.
2. D3: `1215`, `1216`, `1220`, `1225`로 SWEA 고정 10테케 형식에 익숙해진다.
3. 시간이 남으면 `1240`, `1493`, `2814`, `3032`를 본다. 이 네 문제는 D3 중에서도 사고 패턴이 달라서 실전 대비 효율이 좋다.
