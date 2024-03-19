def digitChecker(string, character, index, isA):
    if isA: #first pointer
        if character == "o":
            if len(string) - index >= 3:
                if string[index:index+3] == "one":
                    return 1
        elif character == "t":
            # print("run")
            if len(string) - index >= 3: #check two
                # print("yes")
                if len(string) - index >= 5: #check three
                    # print("ah")
                    if string[index:index+5] == "three":
                        return 3
                    elif string[index:index+3] == "two":
                        return 2
                else:
                    if string[index:index+3] == "two":
                        return 2
        elif character == "f":
            if len(string) - index >= 4: #four or five
                if string[index:index+4] == "four":
                    return 4
                elif string[index:index+4] == "five":
                    return 5
        elif character == "s":
            if len(string) - index >= 3: 
                if len(string) - index >= 5: #seven
                    if string[index:index+5] == "seven":
                        return 7
                    elif string[index:index+3] == "six":
                        return 6
                else: #six
                    if string[index:index+3] == "six":
                        return 6
        elif character == "e":
            if len(string) - index >= 5:
                if string[index:index+5] == "eight":
                    return 8
        else: #nine
            if len(string) - index >= 4:
                if string[index:index+4] == "nine":
                    return 9

    else: #second pointer
        if character == "e": #one or three or five or nine
            if index >= 2:
                if index >= 3:
                    if index >= 4: #three
                        if string[index-4:index] == "thre":
                            return 3
                        elif string[index-3:index] == "fiv":
                            return 5
                        elif string[index-3:index] == "nin":
                            return 9
                        elif string[index-2:index] == "on":
                            return 1
                    else: #five or nine
                        if string[index-3:index] == "fiv":
                            return 5
                        elif string[index-3:index] == "nin":
                            return 9
                        elif string[index-2:index] == "on":
                            return 1
                else: #one
                    if string[index-2:index] == "on":
                        return 1
        elif character == "o": #two 
            if index >= 2:
                if string[index-2:index] == "tw":
                    return 2
        elif character == "r": #four
            if index >= 3:
                if string[index-3:index] == "fou":
                    return 4
        elif character == "x": #six
            if index >= 2:
                if string[index-2:index] == "si":
                    return 6
        elif character == "n": #seven
            if index >= 4:
                if string[index-4:index] == "seve":
                    return 7
        else: #eight
            if index >= 4:
                if string[index-4:index] == "eigh":
                    return 8
    return 0

def main():
    print("running")
    inputFile = open("12-1/trebuchetinput.txt", "r")

    validFirst = ["o", "t", "f", "s", "e", "n"]

    validLast = ["e", "o", "r", "x", "n", "t"]

    line = inputFile.readline()

    res = 0

    while line != "":
        a,b = 0, len(line)-1
        foundOne = foundTwo = False

        while not foundOne or not foundTwo:
            # print(a,b)
            if not foundOne:
                if line[a] in validFirst:
                    # print("test")
                    digit = digitChecker(line, line[a], a, True)
                    if digit:
                        foundOne = True
                        res += digit*10
                elif line[a].isdigit():
                    foundOne = True
                    res += int(line[a])*10
                a += 1

            if not foundTwo:
                if line[b] in validLast:
                    digit = digitChecker(line, line[b], b, False)
                    if digit:
                        foundTwo = True
                        res += digit
                elif line[b].isdigit():
                    foundTwo = True
                    res += int(line[b])
                b -= 1

        # print(res)

        #53758 < ans < 55370
        line = inputFile.readline()

    print(res)

    inputFile.close()

if __name__ == "__main__":
    print("running")
    main()