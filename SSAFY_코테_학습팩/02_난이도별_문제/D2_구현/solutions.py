import sys


def solve_p01():
    input = sys.stdin.readline
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        board = [[0] * n for _ in range(n)]
        r = c = d = 0

        for num in range(1, n * n + 1):
            board[r][c] = num
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nr >= n or nc < 0 or nc >= n or board[nr][nc] != 0:
                d = (d + 1) % 4
                nr = r + dr[d]
                nc = c + dc[d]
            r, c = nr, nc

        print(f"#{tc}")
        for row in board:
            print(*row)


def solve_p02():
    input = sys.stdin.readline
    t = int(input())
    for tc in range(1, t + 1):
        n, m = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        ans = 0

        for r in range(n - m + 1):
            for c in range(n - m + 1):
                total = 0
                for i in range(m):
                    for j in range(m):
                        total += board[r + i][c + j]
                ans = max(ans, total)

        print(f"#{tc} {ans}")


def solve_p03():
    input = sys.stdin.readline

    def rotate_90(board):
        n = len(board)
        rotated = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                rotated[c][n - 1 - r] = board[r][c]
        return rotated

    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(n)]
        r90 = rotate_90(board)
        r180 = rotate_90(r90)
        r270 = rotate_90(r180)

        print(f"#{tc}")
        for i in range(n):
            a = "".join(map(str, r90[i]))
            b = "".join(map(str, r180[i]))
            c = "".join(map(str, r270[i]))
            print(a, b, c)


def solve_p04():
    input = sys.stdin.readline
    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        board = [list(map(int, input().strip())) for _ in range(n)]
        mid = n // 2
        total = 0

        for r in range(n):
            dist = abs(mid - r)
            for c in range(dist, n - dist):
                total += board[r][c]

        print(f"#{tc} {total}")


def solve_p05():
    input = sys.stdin.readline
    t = int(input())
    for tc in range(1, t + 1):
        target = input().strip()
        current = "0"
        count = 0

        for bit in target:
            if bit != current:
                count += 1
                current = bit

        print(f"#{tc} {count}")


def solve_p06():
    input = sys.stdin.readline
    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]

    t = int(input())
    for tc in range(1, t + 1):
        n, k = map(int, input().split())
        board = [[0] * n for _ in range(n)]

        for _ in range(k):
            r, c = map(int, input().split())
            r -= 1
            c -= 1
            for d in range(5):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < n:
                    board[nr][nc] += 1

        ans = max(max(row) for row in board)
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    # 실행하고 싶은 문제 함수로 바꿔서 사용하세요.
    solve_p01()
