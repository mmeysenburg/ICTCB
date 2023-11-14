name=input()
shortname=name[0]
for i in range(1,len(name)):

    if shortname[i]!=name[i-1]:
      
        shortname+=name[i]
print(shortname)
