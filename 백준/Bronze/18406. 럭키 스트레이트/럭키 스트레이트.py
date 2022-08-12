n=input()
l=len(n)
arr = list(map(int, list(n[:l//2])))
brr = list(map(int, list(n[l//2:])))
if sum(arr) == sum(brr):
    print("LUCKY")
else:
    print("READY")