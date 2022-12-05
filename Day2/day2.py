file = open("data.txt", "r")

playerMoves = []
oppMoves = []

for l in file:
    line = file.readline()
    line = line.split(" ")
    print(line)
    oppMoves.append(line[0])
    playerMoves.append(line[1])

#print(playerMoves)
