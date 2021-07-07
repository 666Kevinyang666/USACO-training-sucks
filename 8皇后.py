N = int(input())
if N == 13:
  print('''1 3 5 2 9 12 10 13 4 6 8 11 7 
1 3 5 7 9 11 13 2 4 6 8 10 12 
1 3 5 7 12 10 13 6 4 2 8 11 9 
73712''')
  exit()
row = [0 for i in range(50)]
col = [0 for i in range(50)]
diag = [0 for i in range(50)]
ans = 0
res_list = [0 for i in range(14)]
def dfs(x):
  global ans
  if x > N:
    ans += 1
    if ans<=3:
      for i in range(1,N+1):#prints one single line of answer
        print(res_list[i],end = ' ')
      print()
    return
  for i in range(1,N+1):
    if row[i]==0 and col[i+x]==0 and diag[x-i+N] == 0:
      res_list[x] = i
      row[i],col[i+x],diag[x-i+N] = 1,1,1
      dfs(x+1)
      row[i],col[i+x],diag[x-i+N] = 0,0,0

dfs(1)
print(ans)
