import sys
input = lambda: sys.stdin.readline().strip()
import random

class defaultdict:
    def __init__(self, func):
        self.RANDOM = random.randint(0, 1 << 64)
        self.default = func
        self.dict = {}

    def __iter__(self):
        for key in [self.RANDOM ^ i for i in self.dict]:
            yield key

    def __repr__(self):
        ret = '{'
        for ix, key in enumerate(self):
            if ix >0:
                ret+=', '
            ret += str(key) + ': ' + str(self[key])
        ret += '}'
        return ret

    def __getitem__(self, key):
        myKey = self.RANDOM ^ key
        if myKey not in self.dict:
            self.dict[myKey] = self.default()
        return self.dict[myKey]

    def __setitem__(self, key, item):
        myKey = self.RANDOM ^ key
        self.dict[myKey] = item

    def getKeys(self):
        return [self.RANDOM ^ i for i in self.dict]
for test in range(int(input())):
    arr = list(map(int, input().split()))
    n, arr = arr[0], arr[1:]
    d = defaultdict(int)
    for i in arr:
        d[i]+=1
    ans = -1
    ok = True
    for i in d:
        if d[i] > n/2:
            if ans == -1:
                ans = i
            else:
                ok = False
                break
    if ok and ans != -1:
        print(ans)
    else:
        print("SYJKGW")