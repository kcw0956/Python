import sys

input = sys.stdin.readline

def normal_lsit():

    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)] #board를 생성하게 되는 구조 리스트를 받아서 []를 감싸라는 구조여서 

    arr2 = [int[input()] for _ in range(5)]

def board_list():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    print(board)
    return board

def board_print(arr):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col])

def 열_최대합(arr):
    for row in range(len(arr)):
        answer = max(answer, sum(arr[row]))
    return answer

def 행_최대합(arr): # 고치기 
    for col in range(len(arr[col])):
        for row in range(len(arr)):
            answer = max(answer, sum(arr[col]))
            
def 행_최대합_ai(board):    
    for j in range(n):
        total = 0
        for i in range(n):
            total += board[i][j]
        answer = max(answer, total)

def 대각선_탐색(board):
    total1 = 0
    total2 = 0
    for i in range(n):
        total1 += board[i][i]
        total2 += board[i][n - 1 - i]
def 완전탐색(arr):
    answer = 0

    for i in range(5):
        for i in range(i + 1, 5):
            answer = max(answer, arr[i] + arr[j])
        

board_list()

arr = list(map(int, input().split()))
print(arr)

def 출력(board):
    for row in board:
        for col in row:
            print(col, end = " ")
        print()

    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
        print()
    
    for row in board:
        print(*row)
    print()