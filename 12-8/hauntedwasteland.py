lines = []
stepOrder = ""

with open("12-8/input.txt") as f:
    stepOrder = f.readline().strip()
    f.readline()
    lines = [line.strip() for line in f.readlines()]
    # print(lines)
    # print(stepOrder)

def partOneSolve(lines,stepOrder):
    res = 0
    myDict = dict()
    curr = 'AAA'
    for line in lines:
        if line[0:3] not in myDict:
            myDict[line[0:3]] = [line[7:10],line[12:15]]

    while curr != "ZZZ":
        for step in stepOrder:
            if curr == "ZZZ":
                return res
            if step == "L":
                curr = myDict[curr][0]
                res += 1
            elif step == "R":
                curr = myDict[curr][1]
                res += 1
    return res

# print("p1",partOneSolve(lines,stepOrder))

def partTwoSolve(lines):
    res = 0
    myDict = {}
    curr = []
    for line in lines:
        if line[2] == "A":
            curr.append(line[0:3])
        if line[0:3] not in myDict:
            myDict[line[0:3]] = [line[7:10],line[12:15]]

    print(curr)

    idx1 = 'MCA'
    idx2 = 'AAA'
    idx3 = 'DCA'
    idx4 = 'LGA'
    idx5 = 'NLA'
    idx6 = 'VPA'
    
    def findSteps(start):
        steps = 0
        while start[-1] != "Z":
            for step in stepOrder:
                if start[-1] == "Z":
                    return steps
                if step == "L":
                    start = myDict[start][0]
                    steps += 1
                elif step == "R":
                    start = myDict[start][1]
                    steps += 1
        return steps
    
    print(findSteps(idx1)) #16343
    print(findSteps(idx2)) #16897
    print(findSteps(idx3)) #20221
    print(findSteps(idx4)) #18559
    print(findSteps(idx5)) #11911
    print(findSteps(idx6)) #21883

    #plugged into LCM calculator
    #16,563,603,485,021
    #16563603485021
    
    return res

print("p2",partTwoSolve(lines))