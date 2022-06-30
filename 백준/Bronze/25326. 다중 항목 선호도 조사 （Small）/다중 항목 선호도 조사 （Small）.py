from bisect import bisect_left


def solution(info, query):
    answer = []
    dd = {}
    x = ['kor', 'eng', 'math']
    y = ['apple', 'pear', 'orange']
    z = ['red', 'blue', 'green']
    for i in x:
        dd[i] = {}
        for j in y:
            dd[i][j] = {}
            for k in z:
                dd[i][j][k] = 0
    for i in info:
        a, b, c = i.split()
        dd[a][b][c] += 1
    for q in query:
        a, b, c = q.split()
        cnt = 0
        if a == '-':
            xx = x
        else:
            xx = [a]
        if b == '-':
            yy = y
        else:
            yy = [b]
        if c == '-':
            zz = z
        else:
            zz = [c]
        for i in xx:
            for j in yy:
                for k in zz:
                    cnt+=dd[i][j][k]
        answer.append(cnt)
    return answer


n, m = map(int, input().split())
info = [input() for i in range(n)]
query = [input()for i in range(m)]
for i in solution(info, query):
    print(i)
