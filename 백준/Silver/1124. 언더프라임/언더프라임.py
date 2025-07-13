import sys 
input = sys.stdin.readline

# 구하고자 하는 것: A 이상 B 이하 언더프라임 개수
def solution():
    A, B = map(int, input().split())

    is_prime = [True]*(B+1) # 소수인지 여부가 나와있는 배열
    is_prime[0], is_prime[1] = False, False # 0과 1은 소수가 아님

    # 에레토스테네스의 체
    for i in range(2, int(B**0.5)+1):
        if is_prime[i]: # i가 소수일 때만
            for j in range(i*i, B+1, i):
                is_prime[j] = False
        
    primes = [x for x in range(2, B+1) if is_prime[x]]
    ans = 0

    for n in range(A, B+1):
        tmp = n
        count = 0
        for i in primes:
            if i*i > tmp:
                break
            while tmp % i == 0: # i가 tmp의 소인수라면 나눌 때마다 count 증가
                count += 1
                tmp //= i
        if tmp > 1: # 남은 값이 1보다 크면 그 값도 소인수이므로 count 1 증가
            count += 1 
        
        # 소인수 개수가 2 이상이고, 그 개수가 소수라면 언더프라임
        if count >= 2 and is_prime[count]:
            ans += 1
    
    return print(ans)

solution()