n,b,d = map(int,input().split())
res = [0]
for i in range(257):
  count = 0
  temp = bin(i)
  comp = bin(res[-1])
  temp = '0'*(b-len(temp)+2)+temp[2:]
  comp = '0'*(b-len(comp)+2)+comp[2:]

  for j in range(b):
    if temp[j] != comp[j]:
      count += 1
  diff = 0
  if count >= d:
    for a in range(len(res)):
      diff = 0
      comp = bin(res[a])
      comp = '0'*(b-len(comp)+2)+comp[2:]
      for h in range(b):
        if temp[h]!=comp[h]:
          diff += 1
      if diff>=d:
        continue  
      else:
        break
  if diff >=d:
    res.append(i)
happy = 0
for i in range(len(res)):
  if (res.index(res[i])+1)%10!=0:
    print(res[i],end = ' ')
    happy += 1
  if (res.index(res[i])+1)%10==0:
    print(res[i])
    happy += 1
  if happy == n:
    break
