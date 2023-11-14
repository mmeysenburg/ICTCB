word = input()

f=0
duplicates = []

for char in word:
 
   if word.count(char) > 1:
     f+=1
     
if f==0:
  print(1)
else:
  print(0)