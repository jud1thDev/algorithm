import re
def solution(files):
    split_files = []
    for file in files:
        line = re.split(r'(\d+)', file)
        split_files.append((line[0], line[1], file)) # (Head, Number, 원본file)
        
    # 정렬: Head 사전순(대소문자구분x), Number 오름차순
    split_files.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    return [s[2] for s in split_files]