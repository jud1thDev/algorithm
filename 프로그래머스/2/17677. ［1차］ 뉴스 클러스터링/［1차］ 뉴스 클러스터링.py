from collections import Counter

# 구하는 것: 자카드 유사도
def solution(str1, str2):
    answer = []
    
    def spliting(str):
        str = str.lower() # 대소문자 차이는 무시
        out = []
        for i in range(len(str) - 1):
            a, b = str[i], str[i + 1]
            if a.isalpha() and b.isalpha():
                out.append(str[i:i+2])
        return out
            
    c1 = Counter(spliting(str1))
    c2 = Counter(spliting(str2))
    # print(list1, list2)
    
    a = c1 & c2
    b = c1 | c2
    
    similarity = sum(a.values()) / sum(b.values()) if b else 1
    # print(similarity)
    
    return int(similarity*65536)
