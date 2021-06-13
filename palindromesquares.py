import sys
sys.stdin = open('palsquare.in','r')
sys.stdout = open('palsquare.out','w')
N = int(input())
def d(num):
    return chr(num + ord('A') - 10)
def ispalindromes(x):
  if x == x[::-1]:
    return True
  else:
    return False

def polynomial(num):#进制转化
    res = ''
    while num:
        num, r = divmod(num, N)
        if r >= 10:
            res = d(r) + res
        else:
            res = str(r) + res
    return res

for i in range(1,301):
  if ispalindromes(polynomial(i**2)) == True :
    print(str(polynomial(i))+' '+str(polynomial(i**2)))
