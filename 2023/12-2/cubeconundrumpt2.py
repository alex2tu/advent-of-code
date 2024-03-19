res = 0

with open("12-2/input.txt", "r") as f:
    line = f.readline()

    while line != "":
        numCubes = {
            "red" : 0,
            "blue" : 0,
            "green" : 0
        }
        gameSplit = line.split(":")

        games = gameSplit[1].split(";")
        for game in games:
            gamesSplit = game.split(" ")
            for i in range(0,len(gamesSplit)-1):
                if gamesSplit[i].isdigit():
                    color = gamesSplit[i+1].strip()
                    if color[-1] == ',':
                        color = color[:-1]
                    if int(gamesSplit[i]) > numCubes[color]:
                        numCubes[color] = int(gamesSplit[i]) 
        
        res += numCubes["blue"] * numCubes["green"] * numCubes["red"]

        line = f.readline()

print(res)