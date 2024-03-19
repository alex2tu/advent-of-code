times = []
distances = []

with open("12-6/input.txt") as f:
    timeLine = f.readline().strip()
    distanceLine = f.readline().strip()

    timeLineString = timeLine[6:].strip()
    times = timeLineString.split(" ")

    distanceString = distanceLine[10:].strip()
    distances = distanceString.split(" ")

    i = 0
    while i < 4:
        # print(times)
        # print(i)
        if times[i] == "" or times[i] == " ":
            times.remove("")
        else:
            i += 1
    if times[-1] == "":
        times = times[:-1]
    j = 0
    while j < 4:
        # print(j)
        if distances[j] == "" or distances[j] == " ":
            distances.remove("")
        else:
            j += 1
    
    print(times,distances)

def partOneSolve(times,distances):
    res = 1
    for index in range(4):
        currMult = 0
        time = int(times[index])
        distance = int(distances[index])

        for speed in range(1,time):
            if speed * (time-speed) > distance:
                # if index == 2:
                #     print(speed)
                currMult += 1
        
        # print(currMult)
        res *= currMult
    return res

print(partOneSolve(times,distances))

def partTwoSolve():
    res = 0
    time = 53897698
    distance = 313109012141201
    # time = 71530
    # distance = 940200

    for speed in range(1,time):
        if speed * (time-speed) > distance:
            res += 1
    
    return res

print(partTwoSolve())