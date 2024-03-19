s2s = 35
s2f = 33
f2w = 28
w2l = 15
l2t = 32
t2h = 32
h2l = 16

seedString = ""
lines = []

with open("12-5/input.txt") as f:
    seedString = f.readline().strip()
    lines = [line.strip() for line in f.readlines()]

    # print(seedString)
    # print(lines)

def partOneSolve(lines,seedString):
    seedCount = 20
    def modifySeeds(seeds, lines, index, count):
        modified = [False for i in range(seedCount)]
        for j in range(count):
            dest_source_length = [int(entry) for entry in lines[index+j+1].split(" ") if entry.isdigit()]
            for k in range(seedCount):
                if seeds[k] - dest_source_length[1] < dest_source_length[2] and not modified[k] and seeds[k] >= dest_source_length[1]:
                    modified[k] = True
                    seeds[k] = dest_source_length[0] + seeds[k] - dest_source_length[1]

        # print(seeds)


    seedArray = seedString.split(":")
    seedLine = seedArray[1].strip().split(" ")
    seeds = [int(seedNum) for seedNum in seedLine if seedNum.isdigit()]

    # print(modified)
    # print(seeds)

    for i in range(len(lines)):
        if lines[i] == "seed-to-soil map:":
            modifySeeds(seeds, lines, i, s2s)
        elif lines[i] == "soil-to-fertilizer map:":
            modifySeeds(seeds, lines, i, s2f)
        elif lines[i] == "fertilizer-to-water map:":
            modifySeeds(seeds, lines, i, f2w)
        elif lines[i] == "water-to-light map:":
            modifySeeds(seeds, lines, i, w2l)
        elif lines[i] == "light-to-temperature map:":
            modifySeeds(seeds, lines, i, l2t)
        elif lines[i] == "temperature-to-humidity map:":
            modifySeeds(seeds, lines, i, t2h)
        elif lines[i] == "humidity-to-location map:":
            modifySeeds(seeds, lines, i, h2l)
    
    return min(seeds)

# print(partOneSolve(lines,seedString))

def partTwoSolve(lines):
    #seed one: 1367444651 99920667
    #seed one minimum: 
    #
    seedCount = 5020667
    seeds = [1367444651+i for i in range(seedCount)]
    def modifySeeds(seeds, lines, index, count):
        modified = [False for i in range(seedCount)]
        print("checking")
        for j in range(count):
            dest_source_length = [int(entry) for entry in lines[index+j+1].split(" ") if entry.isdigit()]
            for k in range(seedCount):
                if seeds[k] - dest_source_length[1] < dest_source_length[2] and not modified[k] and seeds[k] >= dest_source_length[1]:
                    modified[k] = True
                    seeds[k] = dest_source_length[0] + seeds[k] - dest_source_length[1]

        # print(seeds)


    # seedArray = seedString.split(":")
    # seedLine = seedArray[1].strip().split(" ")
    # seeds = [int(seedNum) for seedNum in seedLine if seedNum.isdigit()]

    for i in range(len(lines)):
        if lines[i] == "seed-to-soil map:":
            modifySeeds(seeds, lines, i, s2s)
        elif lines[i] == "soil-to-fertilizer map:":
            modifySeeds(seeds, lines, i, s2f)
        elif lines[i] == "fertilizer-to-water map:":
            modifySeeds(seeds, lines, i, f2w)
        elif lines[i] == "water-to-light map:":
            modifySeeds(seeds, lines, i, w2l)
        elif lines[i] == "light-to-temperature map:":
            modifySeeds(seeds, lines, i, l2t)
        elif lines[i] == "temperature-to-humidity map:":
            modifySeeds(seeds, lines, i, t2h)
        elif lines[i] == "humidity-to-location map:":
            modifySeeds(seeds, lines, i, h2l)
    
    return min(seeds)

print(partTwoSolve(lines))