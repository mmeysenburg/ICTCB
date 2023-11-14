def mileage(speed, time):
    total = 0
    for i in range(len(time) - 1, 0, -1):
                #start stop step
        #print(i)
        time[i] -= time[i-1] 
    for i in range(len(speed)):
        total += speed[i] * time[i]
    return total

totaldis = []


while True:

    speed = []
    time = []

    n = int(input())
    if n == -1:
        break
    for x in range(n):


        s_h = input().split()
      #print(s_h)
        speed.append(int(s_h[0]))
        time.append(int(s_h[1]))

    totaldis.append(mileage(speed, time))

for miles in totaldis:
    print(miles, "miles")

    