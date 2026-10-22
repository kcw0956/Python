def o_1(arr):
    return arr[0]


def o_n(arr):
    total = 0
    for x in arr:
        total += x
    return total


def o_n_squared(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
    return count


def o_n_m(board):
    total = 0
    n = len(board)
    m = len(board[0])
    for r in range(n):
        for c in range(m):
            total += board[r][c]
    return total


def o_log_n(n):
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count


def o_n_log_n(arr):
    arr = arr[:]
    arr.sort()
    return arr


def subset_o_2_power_n(arr):
    n = len(arr)
    result = []

    def dfs(idx, selected):
        if idx == n:
            result.append(selected[:])
            return

        selected.append(arr[idx])
        dfs(idx + 1, selected)
        selected.pop()

        dfs(idx + 1, selected)

    dfs(0, [])
    return result


def permutation_o_n_factorial(arr):
    n = len(arr)
    result = []
    used = [False] * n
    current = []

    def dfs():
        if len(current) == n:
            result.append(current[:])
            return

        for i in range(n):
            if not used[i]:
                used[i] = True
                current.append(arr[i])
                dfs()
                current.pop()
                used[i] = False

    dfs()
    return result


def estimate_operations(n):
    values = {
        "O(N)": n,
        "O(N^2)": n * n,
        "O(N^3)": n * n * n,
        "O(2^N)": 2**n if n <= 60 else "too large",
    }
    return values


if __name__ == "__main__":
    for n in [10, 100, 1000, 100000]:
        print(n, estimate_operations(n))
