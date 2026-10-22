import heapq
import sys
from collections import deque


def solve_p01():
    input = sys.stdin.readline
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    opposite = [1, 0, 3, 2]
    connect = {
        0: [],
        1: [0, 1, 2, 3],
        2: [0, 1],
        3: [2, 3],
        4: [0, 3],
        5: [1, 3],
        6: [1, 2],
        7: [0, 2],
    }

    t = int(input())
    for tc in range(1, t + 1):
        n, m, r, c, limit = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        visited = [[0] * m for _ in range(n)]
        q = deque([(r, c)])
        visited[r][c] = 1

        while q:
            cr, cc = q.popleft()
            if visited[cr][cc] == limit:
                continue
            pipe = board[cr][cc]
            for d in connect[pipe]:
                nr = cr + dr[d]
                nc = cc + dc[d]
                if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0:
                    next_pipe = board[nr][nc]
                    if opposite[d] in connect[next_pipe]:
                        visited[nr][nc] = visited[cr][cc] + 1
                        q.append((nr, nc))

        ans = sum(1 for row in visited for x in row if x)
        print(f"#{tc} {ans}")


def solve_p02():
    input = sys.stdin.readline
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    t = int(input())
    for tc in range(1, t + 1):
        n, k = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        max_height = max(max(row) for row in board)
        visited = [[False] * n for _ in range(n)]
        ans = 0

        def dfs(r, c, length, used_cut):
            nonlocal ans
            ans = max(ans, length)

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < n and 0 <= nc < n):
                    continue
                if visited[nr][nc]:
                    continue

                if board[nr][nc] < board[r][c]:
                    visited[nr][nc] = True
                    dfs(nr, nc, length + 1, used_cut)
                    visited[nr][nc] = False
                elif not used_cut and board[nr][nc] - k < board[r][c]:
                    original = board[nr][nc]
                    board[nr][nc] = board[r][c] - 1
                    visited[nr][nc] = True
                    dfs(nr, nc, length + 1, True)
                    visited[nr][nc] = False
                    board[nr][nc] = original

        for r in range(n):
            for c in range(n):
                if board[r][c] == max_height:
                    visited[r][c] = True
                    dfs(r, c, 1, False)
                    visited[r][c] = False

        print(f"#{tc} {ans}")


def solve_p03():
    input = sys.stdin.readline
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def is_edge(r, c, n):
        return r == 0 or r == n - 1 or c == 0 or c == n - 1

    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(n)]
        cores = []
        for r in range(n):
            for c in range(n):
                if board[r][c] == 1 and not is_edge(r, c, n):
                    cores.append((r, c))

        best_connected = 0
        best_wire = 10**9

        def path_cells(r, c, d):
            cells = []
            nr = r + dr[d]
            nc = c + dc[d]
            while 0 <= nr < n and 0 <= nc < n:
                if board[nr][nc] != 0:
                    return None
                cells.append((nr, nc))
                nr += dr[d]
                nc += dc[d]
            return cells

        def dfs(idx, connected, wire):
            nonlocal best_connected, best_wire
            if connected + (len(cores) - idx) < best_connected:
                return
            if idx == len(cores):
                if connected > best_connected:
                    best_connected = connected
                    best_wire = wire
                elif connected == best_connected:
                    best_wire = min(best_wire, wire)
                return

            r, c = cores[idx]
            for d in range(4):
                cells = path_cells(r, c, d)
                if cells is None:
                    continue
                for wr, wc in cells:
                    board[wr][wc] = 2
                dfs(idx + 1, connected + 1, wire + len(cells))
                for wr, wc in cells:
                    board[wr][wc] = 0

            dfs(idx + 1, connected, wire)

        dfs(0, 0, 0)
        print(f"#{tc} {best_connected} {best_wire}")


def solve_p04():
    input = sys.stdin.readline
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    inf = 10**9

    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        board = [list(map(int, input().strip())) for _ in range(n)]
        dist = [[inf] * n for _ in range(n)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            cost, r, c = heapq.heappop(heap)
            if cost != dist[r][c]:
                continue
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < n:
                    next_cost = cost + board[nr][nc]
                    if next_cost < dist[nr][nc]:
                        dist[nr][nc] = next_cost
                        heapq.heappush(heap, (next_cost, nr, nc))

        print(f"#{tc} {dist[n - 1][n - 1]}")


if __name__ == "__main__":
    # 실행하고 싶은 문제 함수로 바꿔서 사용하세요.
    solve_p01()
