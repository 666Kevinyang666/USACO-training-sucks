fin = open("dualpal.in",'r')
fout = open("dualpal.out",'w')
N,S = map(int,fin.readline().split())
res = 0
def ispalindromes(x):
  if x == x[::-1]:
    return True
  else:
    return False
def polynomial(m,x):
  num = ''
  while x >= m:
    a = x%m
    x = x//m
    num+= str(a)
  num+=str(x)
  return num
while res < N:
  S+=1
  count=0
  for j in range(2,11):
    if ispalindromes(polynomial(j,S)) == True:
      count+=1
  if count>=2:
    res+=1
    fout.write(str(S)+'\n')
fout.close()
