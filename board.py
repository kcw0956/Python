import sys

# board = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]

# for row in board:
#     print(row)

# n = 5
# m = 5
# board = [[0] * m for _ in range(n)]

input = sys.stdin.readline

n, m = map(int, input().split())

# board = []
#
# for i in range(n):
#     row = list(map(int, input().split())) #map 은 개체라서 리스트로 형변환 해주는 작업이 필요해서 감싸주는것임
#     # 보통 board 를 만든다면 board = [[0] * n for _ in range(m)] 이렇게 만듦
#     # 만약 숫자가 아닌 문자열 list를 만드려면 함수를 적용 후 int형 변환인 map 개체가 아닌 그냥 list(input().split()) 이런식으로 받으면 됨
#
#     board.append(row)

board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for row in board:
    print(*row)
