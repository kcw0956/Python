import sys
from collections import deque


def solve_p01():
    input = sys.stdin.readline
    t = int(input())
    for tc in range(1, t + 1):
        n, d = map(int, input().split())
        heights = list(map(int, input().split()))

        for _ in range(d):
            heights.sort()
            if heights[-1] - heights[0] <= 1:
                break
            heights[0] += 1
            heights[-1] -= 1

        heights.sort()
        print(f"#{tc} {heights[-1] - heights[0]}")


def solve_p02():
    input = sys.stdin.readline
    t = int(input())
    for tc in range(1, t + 1):
        q = deque(map(int, input().split()))
        dec = 1

        while True:
            x = q.popleft() - dec
            if x <= 0:
                q.append(0)
                break
            q.append(x)
            dec += 1
            if dec == 6:
                dec = 1

        print(f"#{tc}", *q)


def solve_p03():
    input = sys.stdin.readline

    def count_line(line, k):
        count = 0
        length = 0
        for x in line:
            if x == 1:
                length += 1
            else:
                if length == k:
                    count += 1
                length = 0
        if length == k:
            count += 1
        return count

    t = int(input())
    for tc in range(1, t + 1):
        n, k = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        ans = 0

        for r in range(n):
            ans += count_line(board[r], k)

        for c in range(n):
            col = [board[r][c] for r in range(n)]
            ans += count_line(col, k)

        print(f"#{tc} {ans}")


def solve_p04():
    input = sys.stdin.readline
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    t = int(input())
    for tc in range(1, t + 1):
        n, m = map(int, input().split())
        board = [list(input().strip()) for _ in range(n)]

        sr = sc = gr = gc = -1
        for r in range(n):
            for c in range(m):
                if board[r][c] == "S":
                    sr, sc = r, c
                elif board[r][c] == "G":
                    gr, gc = r, c

        dist = [[-1] * m for _ in range(n)]
        q = deque([(sr, sc)])
        dist[sr][sc] = 0

        while q:
            r, c = q.popleft()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < m:
                    if dist[nr][nc] == -1 and board[nr][nc] != "#":
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr, nc))

        print(f"#{tc} {dist[gr][gc]}")


def solve_p05():
    input = sys.stdin.readline
    t = int(input())
    for tc in range(1, t + 1):
        n, b = map(int, input().split())
        heights = list(map(int, input().split()))
        ans = 10**9

        def search(idx, total):
            nonlocal ans
            if total >= b:
                ans = min(ans, total - b)
                return
            if idx == n:
                return
            if ans == 0:
                return

            search(idx + 1, total + heights[idx])
            search(idx + 1, total)

        search(0, 0)
        print(f"#{tc} {ans}")


def solve_p06():
    input = sys.stdin.readline
    t = int(input())
    for tc in range(1, t + 1):
        s = input().strip()
        stack = []

        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        print(f"#{tc} {len(stack)}")


if __name__ == "__main__":
    # 실행하고 싶은 문제 함수로 바꿔서 사용하세요.
    solve_p01()
