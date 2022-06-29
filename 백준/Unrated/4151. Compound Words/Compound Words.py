arr = []
try:
    while True:
        arr.append(input())
except:
    pass

class Trie:
    def __init__(self):
        self.arr = [None] * 26
        self.end = False

    def insert(self, s, ix=0):
        if len(s) == ix:
            self.end = True
            return
        c = s[ix]
        if self.arr[ord(c)-ord('a')] == None:
            self.arr[ord(c) - ord('a')] = Trie()
        self.arr[ord(c) - ord('a')].insert(s, ix+1)

    def get(self, s, ix=0):
        if len(s) == ix:
            return self
        return self.arr[ord(s[ix])-ord('a')].get(s, ix+1)

    def find(self, s=''):
        global ss, ans
        if self.end:
            if s in ss and not s == '':
                ans.add(sss + s)
        for i in range(26):
            if self.arr[i] != None:
                self.arr[i].find(s + chr(ord('a')+i))

trie = Trie()
for i in arr:
    trie.insert(i)
ss = set(arr)
ans = set()
for sss in arr:
    trie.get(sss).find()
ans = list(ans)
ans.sort()
for i in ans:
    print(i)