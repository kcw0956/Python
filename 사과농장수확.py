#
# [문제] 사과 수확하기1번부터 $N$번까지 번호가 붙은 $N$개의 사과가 나무에 달려 있다. 각 사과마다 수확 시 얻을 수 있는 이익과 수확할 수 있는 날이 존재한다.사과의 이익은 배열 $A$로, 수확 가능한 날짜는 배열 $B$로 주어진다. 즉, $i$번 사과는 수확하면 $A[i]$원의 이익을 얻을 수 있고, 오직 $B[i]$번째 날에만 수확할 수 있다.
# 김싸피는 번호가 연속된 사과들을 하나의 구간으로 선택해, 그 구간에 포함된 사과를 모두 수확하려고 한다.
# 단, 하루에는 사과를 하나만 수확할 수 있다. 따라서 선택한 구간 안에 같은 날짜에 수확해야 하는 사과가 2개 이상 있으면, 그 구간은 선택할 수 없다.
# 조건을 만족하도록 연속된 구간을 선택했을 때, 얻을 수 있는 최대 이익을 구하라
# .[예시]$N = 4, A = \{6, 2, 3, 2\}, B = \{3, 2, 3, 1\}$ 인 경우1번과 2번 사과를 선택하면 총 8원의 이익을 얻을 수 있다. 이는 가능한 최대 이익이다
# .하지만 1번, 2번, 3번 사과를 모두 수확하려 하면, 1번과 3번 사과의 수확 날짜가 같아 조건을 만족하지 못하므로 선택할 수 없다.
# [제약사항]$N$은 3 이상 500 이하이다. ($3 \le N \le 500$)각 $A[i]$는 1 이상 200 이하의 정수이다.각 $B[i]$는 1 이상 200 이하의 정수이다
# .[입력]가장 첫 줄에는 테스트 케이스의 총 수가 주어진다. 그 다음 줄부터 각 테스트 케이스가 주어지며, 각 테스트 케이스는 3줄로 구성된다.
# 각 테스트 케이스의 첫 줄에는 $N$이 주어진다.두 번째 줄에는 각 사과의 이익을 나타내는 배열 $A$가 공백으로 구분되어 주어진다.
# 세 번째 줄에는 각 사과를 수확할 수 있는 날짜를 나타내는 배열 $B$가 공백으로 구분되어 주어진다.
# [출력]각 테스트 케이스마다 한 줄에
# #x를 출력한 뒤, 공백을 한 칸 두고 문제에서 정의된 최대 이익을 출력한다.
# # (여기서 $x$는 1부터 시작하는 테스트 케이스 번호이다.)[입력 예시]Plaintext3
# 4
# 6 2 3 2
# 3 2 3 1
# 5
# 1 2 3 4 5
# 2 2 2 2 2
# 3
# 3 5 4
# 1 2 1
# [출력 예시]Plaintext#1 8
# #2 5
# #3 9

import sys


# 입력 속도를 빠르게 하기 위해 사용 (일반 input() 대신 sys.stdin.readline 사용 가능)
def solve():
    # 전체 테스트 케이스 수 입력
    T = int(sys.stdin.readline().split()[0])

    for tc in range(1, T + 1):
        N = int(sys.stdin.readline().strip())
        A = list(map(int, sys.stdin.readline().split()))
        B = list(map(int, sys.stdin.readline().split()))

        max_profit = 0
        current_profit = 0
        left = 0

        # 현재 구간에 포함된 수확 날짜들을 저장할 집합(Set)
        # 리스트보다 중복 체크(in) 속도가 O(1)로 훨씬 빠릅니다.
        visited_days = set()

        for right in range(N):
            # 새로 추가하려는 사과의 날짜(B[right])가 이미 구간에 있다면
            # 중복이 해결될 때까지 left 포인터를 한 칸씩 오른쪽으로 이동
            while B[right] in visited_days:
                visited_days.remove(B[left])
                current_profit -= A[left]
                left += 1

            # 현재 사과를 구간에 추가
            visited_days.add(B[right])
            current_profit += A[right]

            # 최대 이익 갱신
            if current_profit > max_profit:
                max_profit = current_profit

        print(f"#{tc} {max_profit}")


if __name__ == "__main__":
    solve()