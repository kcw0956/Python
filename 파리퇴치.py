import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

max_flies = 0

for i in range(N - M + 1):
    for j in range(N - M + 1):
        current_files = 0

        for r in range(M):
            for c in range(M):
                current_files += board[i + r][j + c]

        if current_files > max_flies:
            max_flies = current_files

        


    


            

