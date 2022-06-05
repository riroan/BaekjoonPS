arr = [["###", "#.#", "#.#", "#.#", "###"], ["..#", "..#", "..#", "..#", "..#"], ["###", "..#", "###", "#..", "###"],
       ["###","..#","###","..#","###"],["#.#","#.#","###","..#","..#"], ["###","#..","###","..#","###"],
       ["###", "#..", "###", "#.#", "###"], ["###", "..#", "..#", "..#", "..#"],["###","#.#","###","#.#","###"],
       ["###","#.#","###","..#","###"]]
s = [input().split() for i in range(5)]
t = [[] for i in range(4)]
for i in range(5):
    for j in range(4):
        t[j].append(s[i][j])
def diff(t):
    for i in range(10):
        ok = True
        for j in range(5):
            for k in range(3):
                if t[j][k] == '#' and arr[i][j][k] == '.':
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return i
    

ans = [0]*4
ans[0] = diff(t[0])
ans[1] = diff(t[1])
ans[2] = diff(t[2])
ans[3] = diff(t[3])
print(f"{ans[0]}{ans[1]}:{ans[2]}{ans[3]}")