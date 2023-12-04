res = 0

symbols = {
    '%',
    "#",
    "*",
    '/',
    '-',
    '&',
    '=',
    '+',
    '$',
    '@'
}

dirs = [
    [0,1], #east
    [0,-1], #west
    [1,0], #south
    [-1,0], #north
    [-1,-1], #northwest
    [-1,1], #northeast
    [1,1], #southeast
    [1,-1] #southwest
]

inputArray = []

def searchAround(row,col,maxRow,maxCol):
    numSet = set()
    for dir in dirs:
        newR = row + dir[0]
        newC = col + dir[1]
        if newR < 0 or newR >= maxRow:
            continue
        if newC < 0 or newC >= maxCol:
            continue
        if inputArray[newR][newC].isdigit():
            digit = getDigit(newR,newC,maxCol)
            if digit in numSet:
                continue
            else:
                numSet.add(digit)
    return numSet

def getDigit(row,col,maxCol):
    digitString = inputArray[row][col]
    placeholder = True
    fpointer = col
    bpointer = col
    while placeholder: #forwards
        if fpointer >= maxCol-1:
            break
        if inputArray[row][fpointer+1].isdigit():
            digitString += inputArray[row][fpointer+1]
            fpointer += 1
        else:
            break
    while placeholder: #backwards
        if bpointer <= 0:
            break
        if inputArray[row][bpointer-1].isdigit():
            digitString = inputArray[row][bpointer-1] + digitString
            bpointer -= 1
        else:
            break
    return int(digitString)
        

with open("12-3/input.txt", "r") as f:
    line = f.readline()

    while line != "":
        line = line.strip()
        arrayLine = []
        for character in line:
            arrayLine.append(character)
        
        inputArray.append(arrayLine)
        line = f.readline()

    numRows = len(inputArray)
    for row in range(numRows):
        numCols = len(inputArray[row])
        col = 0
        while col < numCols:
            if inputArray[row][col] == "*":
                numHashset = searchAround(row,col,numRows,numCols)
                if len(numHashset) == 2:
                    gearRatio = list(numHashset)
                    res += gearRatio[0] * gearRatio[1]
            col += 1

    #86619648 < ans

    #i just added 993*993 to the answer lol cause i couldn't account for edge case

print(res)