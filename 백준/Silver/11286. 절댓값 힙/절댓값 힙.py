import heapq
import sys
input = sys.stdin.readline
class A:
    def __init__(self, x):
        self.x = x
    
    def __lt__(self, other):
        if abs(self.x) == abs(other.x):
            return self.x<other.x
        return abs(self.x) < abs(other.x)

h = []
for i in range(int(input())):
    x = int(input())
    if x == 0:
        if h:
            print(heapq.heappop(h).x)
        else:
            print(0)
    else:
        heapq.heappush(h, A(x))