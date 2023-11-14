pol = int(input())
count=0
for i in range(pol):
  q,y = input().split()
  qual = float(q)*float(y)
  count=count+qual
print(count)  