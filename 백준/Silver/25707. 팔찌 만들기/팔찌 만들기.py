import sys 
input = sys.stdin.readline

# 구하고자 하는 것: 사용하는 줄의 길이의 최솟값
def solution():
    n = int(input().strip())
    marbles = list(map(int, input().strip().split()))
    marbles.sort()
    ans = marbles[-1] - marbles[0]

    for i in range(len(marbles)-1):
        ans += marbles[i+1] - marbles[i]

    print(ans)
    
solution()