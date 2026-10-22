import sys

input = sys.stdin.readline


def read_int():
    return int(input())


def read_two_ints():
    return map(int, input().split())


def read_int_list():
    return list(map(int, input().split()))


def read_number_board(n):
    return [list(map(int, input().split())) for _ in range(n)]


def read_digit_board(n):
    # 01023처럼 공백 없이 붙은 숫자 격자
    return [list(map(int, input().strip())) for _ in range(n)]


def read_char_board(n):
    # S..#처럼 문자로 된 격자
    return [list(input().strip()) for _ in range(n)]


def swea_template():
    t = int(input())
    for tc in range(1, t + 1):
        answer = 0
        print(f"#{tc} {answer}")
