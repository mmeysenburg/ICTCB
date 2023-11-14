dimensions=input().split()

if int(dimensions[0]) - int(dimensions[2]) < 2 or int(dimensions[1]) - int(dimensions[3]) < 2:
   print(0)
else:
  print(1)


