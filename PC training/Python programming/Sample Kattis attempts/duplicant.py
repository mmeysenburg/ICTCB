from collections import Counter

sentence = Counter(input().split())
print(sentence)
print(sentence.values())
count = (filter(lambda w: w > 1, sentence.values()))

count=any(count)


if count==True:
    print("no")
else:
    print("yes")

    