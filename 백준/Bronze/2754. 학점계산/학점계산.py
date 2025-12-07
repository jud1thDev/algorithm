import sys
input = sys.stdin.readline

grade = input().strip()

alphabet = grade[0]

score = 0.0 # F
if grade == 'F':
    print(score)
    exit()

is_plus = grade[1]

if alphabet == 'A':
    score = 4.0
elif alphabet == 'B':
    score = 3.0
elif alphabet == 'C':
    score = 2.0
elif alphabet == 'D':
    score = 1.0

if is_plus == '+':
    score += 0.3
elif is_plus == '-':
    score -= 0.3

print(score)
       