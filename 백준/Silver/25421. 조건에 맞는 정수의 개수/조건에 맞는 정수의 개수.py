arr = [9,39,175,793,3611]
for i in range(99999):arr.append((arr[-1]*6-arr[-2]*5-arr[-3]*8+arr[-4]*4+arr[-5]*2)%987654321)
print(arr[int(input())-1])