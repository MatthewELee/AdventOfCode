file = open("data.txt", "r")

yourMoves = []
oppMoves = []

yourScore = 0
oppScore = 0

for l in file:
    line = l.split(" ")
    oppMoves.append(line[0])
    yourMoves.append(line[1][:1])

def changeValue(moves):
    for idx, m in enumerate(moves):
        if m == "A" or m == "X":
            moves[idx] = "Rock"
        elif m == "B" or m == "Y":
            moves[idx] = "Scissors"
        elif m == "C" or m == "Z":
            moves[idx] = "Paper"
    return moves

oppMoves = changeValue(oppMoves)
yourMoves = changeValue(yourMoves)

def playRound(playerMoves, scdPlayerMoves, score):
    for idx, moves in playerMoves:
        print(moves)

#playRound(oppMoves, yourMoves, oppScore)
