

times = int(input())
respond = []
for x in range(times):
    sentence = input()
    if (sentence[0:10]=="Simon says"):
        respond.append(sentence[11:])

for x in respond:
    print(x)
    