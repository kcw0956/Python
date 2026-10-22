import sys
from collections import deque


def solve_m01():
    input = sys.stdin.readline
    t = int(input())
    for tc in range(1, t + 1):
        n, q = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        prefix = [[0] * (n + 1) for _ in range(n + 1)]

        for r in range(1, n + 1):
            for c in range(1, n + 1):
                prefix[r][c] = (
                    prefix[r - 1][c]
                    + prefix[r][c - 1]
                    - prefix[r - 1][c - 1]
                    + board[r - 1][c - 1]
                )

        ans = -10**18
        for _ in range(q):
            r1, c1, r2, c2 = map(int, input().split())
            total = (
                prefix[r2][c2]
                - prefix[r1 - 1][c2]
                - prefix[r2][c1 - 1]
                + prefix[r1 - 1][c1 - 1]
            )
            ans = max(ans, total)

        print(f"#{tc} {ans}")


def solve_m02():
    input = sys.stdin.readline
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    t = int(input())
    for tc in range(1, t + 1):
        n, m = map(int, input().split())
        board = [list(map(int, input().strip())) for _ in range(n)]
        dist = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
        q = deque([(0, 0, 0)])
        dist[0][0][0] = 0

        while q:
            r, c, broken = q.popleft()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < n and 0 <= nc < m):
                    continue

                if board[nr][nc] == 0 and dist[nr][nc][broken] == -1:
                    dist[nr][nc][broken] = dist[r][c][broken] + 1
                    q.append((nr, nc, broken))
                elif board[nr][nc] == 1 and broken == 0 and dist[nr][nc][1] == -1:
                    dist[nr][nc][1] = dist[r][c][broken] + 1
                    q.append((nr, nc, 1))

        candidates = [x for x in dist[n - 1][m - 1] if x != -1]
        ans = min(candidates) if candidates else -1
        print(f"#{tc} {ans}")


def solve_m03():
    input = sys.stdin.readline
    t = int(input())
    for tc in range(1, t + 1):
        n, limit = map(int, input().split())
        dp = [0] * (limit + 1)

        for _ in range(n):
            score, time = map(int, input().split())
            for cur in range(limit, time - 1, -1):
                dp[cur] = max(dp[cur], dp[cur - time] + score)

        print(f"#{tc} {max(dp)}")


def solve_m04():
    input = sys.stdin.readline
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    t = int(input())
    for tc in range(1, t + 1):
        n, m = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        visited = [[False] * m for _ in range(n)]
        areas = 0
        max_size = 0

        for sr in range(n):
            for sc in range(m):
                if board[sr][sc] == 0 or visited[sr][sc]:
                    continue

                areas += 1
                size = 1
                visited[sr][sc] = True
                q = deque([(sr, sc)])

                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if 0 <= nr < n and 0 <= nc < m:
                            if board[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                size += 1
                                q.append((nr, nc))

                max_size = max(max_size, size)

        print(f"#{tc} {areas} {max_size}")


if __name__ == "__main__":
    # 실행하고 싶은 문제 함수로 바꿔서 사용하세요.
    solve_m01()
