inputFile = open("12-1/trebuchetinput.txt", "r")

line = inputFile.readline()

res = 0

while line != "":
    a,b = 0, len(line)-1
    foundOne = foundTwo = False

    while not foundOne or not foundTwo:
        # print(a,b)
        if not foundOne:
            if line[a].isdigit():
                foundOne = True
                res += int(line[a])*10
            else:
                a += 1

        if not foundTwo:
            if line[b].isdigit():
                foundTwo = True
                res += int(line[b])
            else:
                b -= 1


    line = inputFile.readline()

print(res)

inputFile.close()