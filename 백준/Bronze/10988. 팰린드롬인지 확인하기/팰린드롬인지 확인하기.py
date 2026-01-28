import sys
input = sys.stdin.readline

word = input().strip()
for i in range(len(word)):
    if word[i] != word[len(word) - i - 1]:
        print(0)
        break
    if i == len(word)//2: 
        print(1)