import sys
def input(): return sys.stdin.readline().strip()


test = 1
while True:
    s = list(input())
    if '-' in s:
        break
    cnt = 0
    for i in range(len(s)):
        ss = []
        for ix, i in enumerate(s):
            if i == '{':
                ss.append((i, ix))
            else:
                if len(ss) == 0:
                    cnt+=1
                    s[ix] = '{'
                    break
                else:
                    ss.pop()
        else:
            if ss:
                s[ss[-1][1]] = '}'
                cnt+=1
    print(f"{test}. {cnt}")
    test += 1
