import string
from collections import defaultdict
def solution(str1, str2):
    answer = 0
    str1=str1.lower()
    str2=str2.lower()
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    s1, s2 = set(), set()
    for i in range(len(str1)-1):
        t = str1[i:i+2]
        ok = True
        for j in t:
            if j not in string.ascii_lowercase:
                ok = False
        if ok:
            d1[t]+=1
            s1.add(t)
    for i in range(len(str2)-1):
        t = str2[i:i+2]
        ok = True
        for j in t:
            if j not in string.ascii_lowercase:
                ok = False
        if ok:
            d2[t]+=1
            s2.add(t)
    up, down = 0,0
    for i in s1&s2:
        up+=min(d1[i], d2[i])
    for i in s1|s2:
        down+=max(d1[i], d2[i])
    try:
        return int(up/down*65536)
    except:
        return 65536