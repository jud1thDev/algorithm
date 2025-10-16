def solution(n, tops):
    MOD = 10007
    nOf124 = [0] * (n + 1)
    nOf3 = [0] * (n + 1)
    
    # 초기값 설정 
    nOf124[0] = 1
    nOf3[0] = 0

    for i in range(1, n + 1):
        nOf3[i] = (nOf124[i-1] + nOf3[i-1]) % MOD
        nOf124[i] = (nOf3[i-1] * (1 + tops[i-1]) + nOf124[i-1] * (2 + tops[i-1])) % MOD

    return (nOf124[n] + nOf3[n]) % MOD
