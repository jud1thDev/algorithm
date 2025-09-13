import sys
input = sys.stdin.readline

from collections import Counter

given = input().strip().upper()

counter = Counter(given) 
most_used = max(counter.values())

ans = []
for alphabet, cnt in counter.items(): # (alphabet, cnt)
    if cnt == most_used:
        ans.append(alphabet)
    
if len(ans) == 1:
    print(ans[0])
else: print('?')