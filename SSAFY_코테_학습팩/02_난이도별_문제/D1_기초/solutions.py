import sys


def solve_p01():
    input = sys.stdin.readline
    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        arr = list(map(int, input().split()))
        odd_sum = 0
        total = 0
        for x in arr:
            total += x
            if x % 2 == 1:
                odd_sum += x
        avg = int(total / n + 0.5)
        print(f"#{tc} {odd_sum} {avg}")


def solve_p02():
    input = sys.stdin.readline
    t = int(input())
    for tc in range(1, t + 1):
        word = input().strip()
        total = 0
        for ch in word:
            total += ord(ch) - ord("A") + 1
        print(f"#{tc} {total}")


def solve_p03():
    input = sys.stdin.readline
    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        scores = list(map(int, input().split()))
        count = [0] * 101
        for score in scores:
            count[score] += 1

        best = 0
        for score in range(101):
            if count[score] >= count[best]:
                best = score

        print(f"#{tc} {best}")


def solve_p04():
    input = sys.stdin.readline
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def day_of_year(month, day):
        return sum(days[:month]) + day

    t = int(input())
    for tc in range(1, t + 1):
        m1, d1, m2, d2 = map(int, input().split())
        ans = day_of_year(m2, d2) - day_of_year(m1, d1) + 1
        print(f"#{tc} {ans}")


def solve_p05():
    input = sys.stdin.readline
    t = int(input())
    for tc in range(1, t + 1):
        n, q = map(int, input().split())
        cards = list(map(int, input().split()))

        for _ in range(q):
            left, right = map(int, input().split())
            for i in range(left - 1, right):
                cards[i] = 1 - cards[i]

        print(f"#{tc} {sum(cards)}")


def solve_p06():
    input = sys.stdin.readline
    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        parts = []
        for _ in range(n):
            ch, cnt = input().split()
            parts.append(ch * int(cnt))

        result = "".join(parts)
        print(f"#{tc}")
        for i in range(0, len(result), 10):
            print(result[i:i + 10])


if __name__ == "__main__":
    # 실행하고 싶은 문제 함수로 바꿔서 사용하세요.
    # 예: solve_p03()
    solve_p01()
