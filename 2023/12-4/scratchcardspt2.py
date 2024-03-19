res = 0

cardList = [1 for i in range(190)]
currCard = 0

with open("12-4/input.txt", "r") as f:
    line = f.readline()

    while line != "":

        scratchcardSplit = line.split(":")
        numbers = scratchcardSplit[1].strip().split("|")
        winningNumbers = numbers[0].split(" ")
        yourNumbers = numbers[1].split(" ")

        i = 0
        while i < 10:
            if winningNumbers[i] == "" or winningNumbers[i] == " ":
                winningNumbers.remove("")
            else:
                i += 1
        if winningNumbers[-1] == "":
            winningNumbers = winningNumbers[:-1]
        j = 0
        while j < 25:
            if yourNumbers[j] == "" or yourNumbers[j] == " ":
                yourNumbers.remove("")
            else:
                j += 1
        
        winningSet = set(winningNumbers)
        yourSet = set(yourNumbers)

        currWins = 0
        for num in yourSet:
            if num in winningSet:
                currWins += 1

        
        for i in range(currWins):
            if currCard+i < 189:
                cardList[currCard+i+1] += cardList[currCard]

        currCard += 1
        line = f.readline()

for num in cardList:
    res += num

print(res)