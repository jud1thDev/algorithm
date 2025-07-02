# 운체같당ㅋㅋ
# 구하는 것: 각 사람이 필요한 시간의 합의 최솟값
def solution():
    n = input().strip()
    p_list = list(map(int, input().strip().split()))

    p_list.sort()
    ans = 0
    tmp = 0

    for i in range(len(p_list)):
        tmp += p_list[i]
        ans += tmp 

    print(ans)

solution()
