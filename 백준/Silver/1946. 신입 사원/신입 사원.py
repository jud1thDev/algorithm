import sys
input = sys.stdin.readline

def solution():
    t = int(input())
    results = []

    for _ in range(t):
        n = int(input())
        applicants = []
        
        for _ in range(n):
            doc, interview = map(int, input().split())
            applicants.append((doc, interview))
        
        applicants.sort(key=lambda x: x[0])
        
        count = 1
        lowest = applicants[0][1]

        for i in range(1, n):
            if applicants[i][1] < lowest:
                count += 1
                lowest = applicants[i][1]
        results.append(count)
    print(*results)

solution()
