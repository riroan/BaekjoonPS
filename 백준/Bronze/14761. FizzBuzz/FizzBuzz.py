# author:  riroan
# created:  2023.11.24 07:44:18
import sys
input = lambda: sys.stdin.readline().strip()

a,b,c = map(int, input().split())
for i in range(1, c+1):
    if i%a==0 and i%b == 0:
        print("FizzBuzz")
    elif i%a==0:
        print("Fizz")
    elif i%b ==0:
        print("Buzz")
    else:
        print(i)
