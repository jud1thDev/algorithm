import sys
input = sys.stdin.readline

N = int(input().strip())
board = [list(input().strip()) for _ in range(N)]

head_r, head_c = -1, -1
found = False
for i in range(N):
    for j in range(N):
        if board[i][j] == '*':
            head_r, head_c = i, j
            found = True
            break
    if found:
        break

heart_r = head_r + 1
heart_c = head_c

left_arm = 0
c = heart_c - 1
while c >= 0 and board[heart_r][c] == '*':
    left_arm += 1
    c -= 1

right_arm = 0
c = heart_c + 1
while c < N and board[heart_r][c] == '*':
    right_arm += 1
    c += 1

waist = 0
r = heart_r + 1
while r < N and board[r][heart_c] == '*':
    waist += 1
    r += 1

waist_end_r = heart_r + waist 

left_leg = 0
r = waist_end_r + 1
c = heart_c - 1
while r < N and c >= 0 and board[r][c] == '*':
    left_leg += 1
    r += 1

right_leg = 0
r = waist_end_r + 1
c = heart_c + 1
while r < N and c < N and board[r][c] == '*':
    right_leg += 1
    r += 1

print(heart_r + 1, heart_c + 1)
print(left_arm, right_arm, waist, left_leg, right_leg)
