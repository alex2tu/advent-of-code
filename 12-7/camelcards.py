lines = []

def orderCards(camelHands,powerOrder):
        handOrder = [None]
        for camelHand in camelHands:
            for i in range(len(handOrder)):
                if handOrder[i] == None:
                    handOrder.insert(i,camelHand)
                    break
                else:
                    if powerOrder.index(camelHand[0][0]) > powerOrder.index(handOrder[i][0][0]): 
                        handOrder.insert(i,camelHand)
                        # handOrder = handOrder[:i] + highCard + handOrder[i:]
                        break
                    elif powerOrder.index(camelHand[0][0]) < powerOrder.index(handOrder[i][0][0]): #stronger hand
                        continue
                    else:
                        if powerOrder.index(camelHand[0][1]) > powerOrder.index(handOrder[i][0][1]): #weaker
                            handOrder.insert(i,camelHand)
                            break
                        elif powerOrder.index(camelHand[0][1]) < powerOrder.index(handOrder[i][0][1]):
                            continue
                        else:
                            if powerOrder.index(camelHand[0][2]) > powerOrder.index(handOrder[i][0][2]): #weaker
                                handOrder.insert(i,camelHand)
                                break
                            elif powerOrder.index(camelHand[0][2]) < powerOrder.index(handOrder[i][0][2]):
                                continue
                            else:
                                if powerOrder.index(camelHand[0][3]) > powerOrder.index(handOrder[i][0][3]): #weaker
                                    handOrder.insert(i,camelHand)
                                    break
                                elif powerOrder.index(camelHand[0][3]) < powerOrder.index(handOrder[i][0][3]):
                                    continue
                                else:
                                    if powerOrder.index(camelHand[0][4]) > powerOrder.index(handOrder[i][0][4]): #weaker
                                        handOrder.insert(i,camelHand)
                                        break
                                    elif powerOrder.index(camelHand[0][4]) < powerOrder.index(handOrder[i][0][4]):
                                        continue
                                    else:
                                        if powerOrder.index(camelHand[0][2]) > powerOrder.index(handOrder[i][0][2]): #weaker
                                            handOrder.insert(i,camelHand)
                                            break
                                        elif powerOrder.index(camelHand[0][2]) < powerOrder.index(handOrder[i][0][2]):
                                            handOrder.insert(i+1,camelHand)
        return handOrder

with open("12-7/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

def partOneSolve(lines):
    cardPowers = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

    highCards = []
    onePairs = []
    twoPairs = []
    triples = []
    fullHouses = []
    quads = []
    fiveOfKinds = []
                    
    res = 0
    for line in lines:
        lineSplit = line.split(" ")
        hand = lineSplit[0]
        bid = int(lineSplit[1])

        myDict = dict()

        for card in hand:
            if card in myDict:
                myDict[card] += 1
            else:
                myDict[card] = 1
        
        if len(myDict) == 5:
            highCards.append([hand,bid])
        elif len(myDict) == 1:
            fiveOfKinds.append([hand,bid])
        elif len(myDict) == 2:
            if myDict.get(hand[0]) == 2 or myDict.get(hand[0]) == 3:
                fullHouses.append([hand,bid])
            elif myDict.get(hand[0]) == 1 or myDict.get(hand[0]) == 4:
                quads.append([hand,bid])
        elif len(myDict) == 4:
            onePairs.append([hand,bid])
        else: #dict is len 3
            found = False
            for key in myDict:
                if myDict[key] == 3:
                    triples.append([hand,bid])
                    found = True
            if not found:
                twoPairs.append([hand,bid])
        
    # print(highCards, onePairs, twoPairs, triples, fullHouses, quads, fiveOfKinds)

    orderedHighCards = orderCards(highCards,cardPowers)
    orderedOnePairs = orderCards(onePairs,cardPowers)
    orderedTwoPairs = orderCards(twoPairs,cardPowers)
    orderedTriples = orderCards(triples,cardPowers)
    orderedFullHouses = orderCards(fullHouses,cardPowers)
    orderedQuads = orderCards(quads,cardPowers)
    orderedFiveOfKinds = orderCards(fiveOfKinds,cardPowers)

    trueHandOrder = orderedHighCards[:-1] + orderedOnePairs[:-1] + orderedTwoPairs[:-1] + orderedTriples[:-1]
    trueHandOrder = trueHandOrder + orderedFullHouses[:-1] + orderedQuads[:-1] + orderedFiveOfKinds[:-1]           

    # print(trueHandOrder)

    for index in range(len(trueHandOrder)):
        res += trueHandOrder[index][1] * (index+1)
    return res

# print(partOneSolve(lines))

def partTwoSolve(lines):
    powerOrder = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']

    res = 0

    highCards = []
    onePairs = []
    twoPairs = []
    triples = []
    fullHouses = []
    quads = []
    fiveOfKinds = []

    for line in lines:
        lineSplit = line.split(" ")
        hand = lineSplit[0]
        bid = int(lineSplit[1])

        myDict = dict()

        for card in hand:
            if card in myDict:
                myDict[card] += 1
            else:
                myDict[card] = 1
        
        if len(myDict) == 5:
            if 'J' in myDict:
                onePairs.append([hand,bid])
            else:
                highCards.append([hand,bid])
        elif len(myDict) == 1:
            fiveOfKinds.append([hand,bid])
        elif len(myDict) == 2:
            if myDict.get(hand[0]) == 1 or myDict.get(hand[0]) == 4:
                if 'J' in myDict:
                    fiveOfKinds.append([hand,bid])
                else:
                    quads.append([hand,bid])
            elif myDict.get(hand[0]) == 3 or myDict.get(hand[0]) == 2:
                if 'J' in myDict:
                    fiveOfKinds.append([hand,bid])
                else:
                    fullHouses.append([hand,bid])
        elif len(myDict) == 4:
            if 'J' in myDict:
                triples.append([hand,bid])
            else:
                onePairs.append([hand,bid])
        else: #dict is len 3
            found = False
            for key in myDict:
                if myDict[key] == 3:
                    if 'J' in myDict:
                        quads.append([hand,bid])
                    else:
                        triples.append([hand,bid])
                    found = True
            if not found:
                if 'J' in myDict:
                    if myDict['J'] == 2:
                        quads.append([hand,bid])
                    else:
                        fullHouses.append([hand,bid])
                else:
                    twoPairs.append([hand,bid])

    orderedHighCards = orderCards(highCards,powerOrder)
    orderedOnePairs = orderCards(onePairs,powerOrder)
    orderedTwoPairs = orderCards(twoPairs,powerOrder)
    orderedTriples = orderCards(triples,powerOrder)
    orderedFullHouses = orderCards(fullHouses,powerOrder)
    orderedQuads = orderCards(quads,powerOrder)
    # print(quads)
    # print(orderedQuads)
    orderedFiveOfKinds = orderCards(fiveOfKinds,powerOrder)

    trueHandOrder = orderedHighCards[:-1] + orderedOnePairs[:-1] + orderedTwoPairs[:-1] + orderedTriples[:-1]
    trueHandOrder = trueHandOrder + orderedFullHouses[:-1] + orderedQuads[:-1] + orderedFiveOfKinds[:-1]  

    # print(trueHandOrder)

    for index in range(len(trueHandOrder)):
        res += trueHandOrder[index][1] * (index+1)
    return res

    #250054801

print(partTwoSolve(lines))