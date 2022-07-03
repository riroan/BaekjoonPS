def solution(places):
    answer = []
    def check(x,y):
        return 0<=x<5 and 0<=y<5
    for p in places:
        ok = 1
        for x in range(5):
            for y in range(5):
                if p[x][y] != 'P':
                    continue
                for dx, dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                    tx,ty = x+dx, y+dy
                    if not check(tx,ty):
                        continue
                    if p[tx][ty] == 'P':
                        ok = 0
                for dx, dy in [[-1,-1],[-1,1],[1,-1],[1,1]]:
                    tx,ty = x+dx, y+dy
                    if not check(tx,ty):
                        continue
                    if p[tx][ty] != 'P':
                        continue
                    if not (p[x+dx][y] == 'X' and p[x][y+dy] == 'X'):
                        ok = 0
                for dx , dy in [[0,-2],[0,2],[2,0],[-2,0]]:
                    tx,ty = x+dx, y+dy
                    if not check(tx,ty):
                        continue
                    if p[tx][ty] != 'P':
                        continue
                    if p[x+dx//2][y+dy//2]!= 'X':
                        ok = 0
        answer.append(ok)
    return answer