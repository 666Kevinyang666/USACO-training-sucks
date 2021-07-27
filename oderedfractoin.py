import sys
sys.stdin
N = int(input())
print('0/1')
res = []
temp = 0
def gcd(a,b):
    while(b!=0):
        temp = a % b
        a = b
        b = temp
    return a

for i in range(1,N+1):
  for j in range(1,i+1):
    if gcd(j,i) == 1:
      res.append(['{}/{}'.format(j,i),j/i])
res.sort(key = lambda x:x[1])
for i in range(len(res)):
  print(res[i][0])
