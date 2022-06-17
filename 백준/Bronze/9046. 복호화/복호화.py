import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    s = input()
    cnt = [0]*26
    for i in s:
        if i!=' ':
            cnt[ord(i)-ord('a')]+=1
    m = max(cnt)
    if cnt.count(m) > 1:
        print('?')
    else:
        for i in range(26):
            if cnt[i] == m:
                print(chr(i+ord('a')))