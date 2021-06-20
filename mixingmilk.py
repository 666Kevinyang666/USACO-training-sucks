import sys
sys.stdin = open("milk.in",'r')
sys.stdout = open("milk.out",'w')
n,m = map(int,input().split())
data = []
res = 0
for i in range(m):
  p,a = map(int,input().split())
  data.append([p,a])
data.sort()
for i in range(m):
  for j in range(data[i][1]):
    res += data[i][0]
    n -= 1
    if n == 0:
      print(res)
      exit()
print(res)
