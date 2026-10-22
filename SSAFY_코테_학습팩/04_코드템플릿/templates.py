import heapq
import sys
from collections import deque

input = sys.stdin.readline


def swea_loop():
    t = int(input())
    for tc in range(1, t + 1):
        ans = 0
        print(f"#{tc} {ans}")


def in_range(r, c, n, m):
    return 0 <= r < n and 0 <= c < m


DR4 = [-1, 1, 0, 0]
DC4 = [0, 0, -1, 1]

DR8 = [-1, -1, -1, 0, 0, 1, 1, 1]
DC8 = [-1, 0, 1, -1, 1, -1, 0, 1]


def rotate_90(board):
    n = len(board)
    m = len(board[0])
    rotated = [[0] * n for _ in range(m)]
    for r in range(n):
        for c in range(m):
            rotated[c][n - 1 - r] = board[r][c]
    return rotated


def bfs_grid(board, sr, sc):
    n = len(board)
    m = len(board[0])
    dist = [[-1] * m for _ in range(n)]
    q = deque([(sr, sc)])
    dist[sr][sc] = 0

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + DR4[d]
            nc = c + DC4[d]
            if in_range(nr, nc, n, m) and dist[nr][nc] == -1 and board[nr][nc] != 1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    return dist


def dfs_grid(board, visited, r, c):
    n = len(board)
    m = len(board[0])
    visited[r][c] = True

    for d in range(4):
        nr = r + DR4[d]
        nc = c + DC4[d]
        if in_range(nr, nc, n, m) and not visited[nr][nc] and board[nr][nc] == 1:
            dfs_grid(board, visited, nr, nc)


def prefix_sum_2d(board):
    n = len(board)
    m = len(board[0])
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for r in range(n):
        for c in range(m):
            prefix[r + 1][c + 1] = (
                prefix[r][c + 1]
                + prefix[r + 1][c]
                - prefix[r][c]
                + board[r][c]
            )
    return prefix


def rect_sum(prefix, r1, c1, r2, c2):
    # 0-index, r2/c2 포함
    return (
        prefix[r2 + 1][c2 + 1]
        - prefix[r1][c2 + 1]
        - prefix[r2 + 1][c1]
        + prefix[r1][c1]
    )


def dijkstra_grid(cost_board):
    n = len(cost_board)
    m = len(cost_board[0])
    inf = 10**18
    dist = [[inf] * m for _ in range(n)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]

    while heap:
        cost, r, c = heapq.heappop(heap)
        if cost != dist[r][c]:
            continue
        for d in range(4):
            nr = r + DR4[d]
            nc = c + DC4[d]
            if in_range(nr, nc, n, m):
                next_cost = cost + cost_board[nr][nc]
                if next_cost < dist[nr][nc]:
                    dist[nr][nc] = next_cost
                    heapq.heappush(heap, (next_cost, nr, nc))

    return dist


def subset_dfs_example(arr, target):
    n = len(arr)
    best = 10**18

    def dfs(idx, total):
        nonlocal best
        if total >= target:
            best = min(best, total - target)
            return
        if idx == n:
            return
        if best == 0:
            return
        dfs(idx + 1, total + arr[idx])
        dfs(idx + 1, total)

    dfs(0, 0)
    return best
