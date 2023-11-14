maxscore=0
winner=0

for i in range(5):
  scores=[int (x) for x in input().split()]
  total=sum(scores)
  if total > maxscore:
    maxscore=total
    winner=i+1

print(winner,maxscore)