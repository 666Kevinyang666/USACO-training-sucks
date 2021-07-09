n = int(input())
m = int(input())
x = []
for i in range(m+1):
  for j in range(m+1):
    x.append(i**2+j**2)
x = list(set(x))
# print(x)
res=[]
for i in x:
  for j in range(1,max(x)):
    temp = 0
    for a in range(n):
      if i+a*j in x:
        temp += 1   
    if temp==n:
      res.append([i,j])
res.sort(key = lambda x:x[1])
if res==[]:
  print('NONE')
  exit()
for i in range(len(res)):
  for j in range(2):
    print(res[i][j],end = ' ')
  print()
