file = open("data.txt", "r")

yourMoves = []
oppMoves = []

yourScore = 0
oppScore = 0

for l in file:
    line = l.split(" ")
    oppMoves.append(line[0])
    yourMoves.append(line[1][:1])


def round(player, score):

    return 0
