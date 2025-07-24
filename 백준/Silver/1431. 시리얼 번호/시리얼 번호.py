import sys 
input = sys.stdin.readline

n = int(input())
serials = [input().strip() for _ in range(n)]

def get_sum(serial):
    total = 0
    for ch in serial:
        if ch.isdigit(): total += int(ch)
    return total

# 정렬
serials.sort(key=lambda x: (len(x), get_sum(x), x)) # 길이 오름차순, 숫자만의합, 사전순

# 출력
for serial in serials:
    print(serial)