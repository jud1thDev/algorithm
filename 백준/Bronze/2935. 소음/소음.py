import sys
input = sys.stdin.readline

A = int(input().strip())
operator = input().strip() # + || *
B = int(input().strip())

ans = (A + B) if operator == '+' else (A * B)
print(ans)