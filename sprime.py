n = int(input())
def isprime(x):
    if x % 2 == 0:
        return x == 2
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True

def dfs(prime,depth):
  if depth == n:
    print(prime)
    return
  for i in range(1,10,2):
    p = 10*prime+i
    if isprime(p):
      dfs(p,depth+1)
for i in [2,3,5,7]:
  dfs(i,1)
