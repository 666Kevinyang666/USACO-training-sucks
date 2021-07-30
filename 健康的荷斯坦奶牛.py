import sys
sys.stdin = open('holstein.in','r')
sys.stdout = open('holstein.out','w')
# import itertools
v = int(input())
needs = list(map(int,input().split()))
g = int(input())
scoop = []
# p = []
# happy = []
for i in range(g):
  line = list(map(int,input().split()))
  scoop.append(line)
a = g+1
res = [0]*g
eaten = [0]*g
feed = [0]*v
def dfs(x):
  global v,needs,g,a,res,eaten,feed,scoop
  if x == g:
    return
  eaten[x] = 1
  for i in range(v):
    feed[i] += scoop[x][i]
  flag = True
  for i in range(v):
    if feed[i]< needs[i]:
      flag = False
      break
  if flag and sum(eaten) < a:
    a = sum(eaten)
    res = list(eaten)
  if not flag:
    dfs(x+1)
  eaten[x] = 0
  for j in range(v):
    feed[j] -= scoop[x][j]
  dfs(x+1)
dfs(0)
ans = ''
ans += str(sum(res))+' '
for i in range(g):
   if res[i]!=0:
     ans += str(i+1)+' '
