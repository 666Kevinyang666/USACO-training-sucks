m,s,c = map(int,input().split())
num = []
for i in range(c):
  n = int(input())
  num.append(n)
num.sort()
distance = []
res = num[-1]-num[0]+1
for i in range(c-1):
  distance.append(num[i+1]-num[i]-1)
distance.sort(key = lambda x:-x)
while distance[-1]==0:  
  distance = distance[:len(distance)-1]
minnum = min(m-1,len(distance))
print(res-sum(distance[:minnum]))
