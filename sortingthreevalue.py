N = int(input())
nums = []
for i in range(N):
  num = int(input())
  nums.append(num)
one = nums.count(1)
two = nums.count(2)
three = nums.count(3)
res = 0
temp = 0
lone = nums[:one]
ltwo = nums[one:one + two]
lthree = nums[one+two:]
res += min(lone.count(2),ltwo.count(1))
temp += abs(lone.count(2)-ltwo.count(1))
res += min(lone.count(3),lthree.count(1))
temp += abs(lone.count(3)-lthree.count(1))
res += min(ltwo.count(3),lthree.count(2))
temp += abs(ltwo.count(3)-lthree.count(2))
temp = temp//3*2
print(res+temp)
