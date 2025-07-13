import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    ops = list(map(int, input().split()))
    max_val = -int(1e9)
    min_val = int(1e9)

    def dfs(idx, result):
        nonlocal max_val, min_val

        if idx == n:
            max_val = max(max_val, result)
            min_val = min(min_val, result)
            return

        if ops[0] > 0:
            ops[0] -= 1
            dfs(idx + 1, result + arr[idx])
            ops[0] += 1

        if ops[1] > 0:
            ops[1] -= 1
            dfs(idx + 1, result - arr[idx])
            ops[1] += 1

        if ops[2] > 0:
            ops[2] -= 1
            dfs(idx + 1, result * arr[idx])
            ops[2] += 1

        if ops[3] > 0:
            ops[3] -= 1
            if result < 0:
                val = -(-result // arr[idx])
            else:
                val = result // arr[idx]
            dfs(idx + 1, val)
            ops[3] += 1

    dfs(1, arr[0])
    print(max_val)
    print(min_val)

solution()