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
    for dir in dirs:
        newR = row + dir[0]
        newC = col + dir[1]
        if newR < 0 or newR >= maxRow:
            continue
        if newC < 0 or newC >= maxCol:
            continue
        if inputArray[newR][newC] in symbols:
            return True
    return False

def getDigit(row,col,maxCol):
    digitString = inputArray[row][col]
    forward = True
    fpointer = col
    while forward:
        if fpointer >= maxCol-1:
            break
        # print(row,fpointer+1)
        # print(inputArray[row][fpointer+1])
        if inputArray[row][fpointer+1].isdigit():
            digitString += inputArray[row][fpointer+1]
            fpointer += 1
        else:
            break
    # print(row,col)
    # print(digitString)
    return digitString
        

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
        # print(numCols)
        col = 0
        while col < numCols:
            if inputArray[row][col].isdigit():
                digit = getDigit(row,col,numCols)
                for i in range(len(digit)):
                    if searchAround(row,col+i,numRows,numCols):
                        # print(int(digit))
                        print(int(digit))
                        res += int(digit)
                        break
                col += len(digit)
            col += 1

print(res)