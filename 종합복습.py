from d1문제.평균값 import test_case
from test import target

T = 0


def 압축문제():
    N = int(input())
    s = ""

    for _ in range(N):
        ch, cnt = input().split()
        s += ch * int(cnt)
        print(f"#{test_case}")
        for i in range(0, len(s), 10):
            print(s[i:i + 10])

def 날짜_계산기():
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def day_of_year(month, day):
        return sum(days[:month]) + day
    for tc in range(1, T + 1):
        m1, d1, m2, d2 = map(int, input().split())
        ans = day_of_year(m1, d1) - day_of_year(m2, d2) + 1

def 두개의숫자열():
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if (N > M):
        A, B = B, A
        N, M = M, N

    best = -10 ** 18
    for start in range(M - N + 1):
        total = 0
        for i in range(N):
            total += A[i] + B[start + i]
        result = max(best, total)

# 문제 내용: N x N 숫자 배열을 90도, 180도, 270도 회전한 결과를 한 줄씩 나란히 출력한다.
#
# 풀이 핵심: 90도 회전은 arr[N-1-r][c], 180도는 arr[N-1-r][N-1-c], 270도는 arr[r][N-1-c] 패턴으로 만들 수 있다.
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [input().split() for _ in range(N)]
#
#     print(f"#{tc}")
#     for r in range(N):
#         a = "".join(arr[N - 1 - c][r] for c in range(N))
#         b = "".join(arr[N - 1 - r][N - 1 - c] for c in range(N))
#         c = "".join(arr[c][N - 1 - r] for c in range(N))
#         print(a, b, c)
board = [list(map(int, input().split())) for _ in range(T)]
N = 0
M = 0
K = 0
def 스도쿠검증():
    board = [list(map(int, input().split())) for _ in range(T)]
    ok = True

    target = set(range(1, 10))

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

def 단어들어가기():
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

#
# 16. 1983. 조교의 성적 매기기
# 문제 내용: 중간, 기말, 과제 점수로 총점을 계산해 K번째 학생의 학점을 구한다.
#
# 풀이 핵심: 총점을 계산하고 내림차순 정렬한 뒤 K번째 학생의 등수를 찾는다. 같은 등급은 N/10명씩 배정된다.
#
# T = int(input())
# grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
#
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     scores = []
#     for idx in range(1, N + 1):
#         mid, final, hw = map(int, input().split())
#         total = mid * 0.35 + final * 0.45 + hw * 0.20
#         scores.append((total, idx))
#
#     scores.sort(reverse=True)
#     for rank, (_, idx) in enumerate(scores):
#         if idx == K:
#             ans = grades[rank // (N // 10)]
#             break
#     print(f"#{tc} {ans}")

def 건물뷰():
    h = list(map(int, input().split()))
    ans = 0

    for i in range(2, N - 2):
        near = max(h[i - 1], h[i - 2], h[i + 1], h[i + 2])
        if (h[i] > near):
            ans += h[i] - near

def 문자열패턴찾기():
    pattern = input().strip()
    text = input().strip()
    ans = 0
    n = len(pattern)

    for i in range(len(text) - n + 1):
        if text[i: i + n] == pattern:
            ans += 1

def 회문세로():
    s= "".join(arr[r + i][c] for i in range(N))