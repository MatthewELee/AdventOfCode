# Matthew Lee - Day 1
file = open("data.txt", "r")
read = file.readlines()

currTotal = 0
totalArray = []
for line in read:
    if line == "\n":
        # Not efficient, stores everything into array
        totalArray.append(currTotal)
        currTotal = 0
    else:
        currTotal += int(line)
totalArray.sort(reverse=True)
totalArray = totalArray[:3]
print("Top 3 highest total calories:", totalArray)
sumCal = 0
for i in totalArray:
    sumCal += i
print("Total:", sumCal)
