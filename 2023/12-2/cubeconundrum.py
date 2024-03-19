
numCubes = {
    "red," : 12,
    "blue," : 14,
    "green," : 13,
    "red" : 12,
    "blue" : 14,
    "green" : 13
}

res = 0

with open("12-2/input.txt", "r") as f:
    line = f.readline()

    while line != "":
        isValid = True
        gameSplit = line.split(":")
        gameNum = gameSplit[0]
        gameID = int(gameNum[5:])

        games = gameSplit[1].split(";")
        for game in games:
            gamesSplit = game.split(" ")
            # print(len(gamesSplit))
            for i in range(0,len(gamesSplit)-1):
                # print(i)
                # print(gamesSplit[i])
                # print(i)
                if gamesSplit[i].isdigit():
                    # print(gamesSplit[i],gamesSplit[i+1],numMarbles[gamesSplit[i+1]])
                    # print(gamesSplit[i+1])
                    # print(numMarbles[gamesSplit[i+1]])
                    if int(gamesSplit[i]) > numCubes[gamesSplit[i+1].strip()]:
                        # print("no")
                        isValid = False
                        break
        # if not isValid:
        #     print(gameID)
        if isValid:
            res += gameID
        # print("blah")
        line = f.readline()

print(res)