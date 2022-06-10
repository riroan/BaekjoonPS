a=int(input())
b=int(input())
c=int(input())
arr = [0]*10
for i in str(a*b*c):
    arr[ord(i)-ord('0')]+=1
for i in arr:
    print(i)