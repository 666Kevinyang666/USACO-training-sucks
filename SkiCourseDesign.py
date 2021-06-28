'''
ID:KEVIN
LANG:PYTHON3
TASK:skidesign
'''
import sys
sys.stdin = open("skidesign.in",'r')
sys.stdout = open("skidesign.out",'w')
n = int(input())
height = []
for i in range(n):
  m = int(input())
  height.append(m)
height.sort()
res = float('inf')
for i in range(height[0],height[-1]):
  curr = 0
  for j in height:
    if j-i>17:
      curr += (j-i-17)**2
    if j<i:
      curr += (j-i)**2
  res = min(curr,res)
print(res)
