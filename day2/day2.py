file = open("input.txt", "r")
fileCopy = open("input.txt", "r")
score = 0


# problem 1:
# X for Rock, Y for Paper, and Z for Scissors
# A for Rock, B for Paper, and C for Scissors
# 1 pts for playing rock, 2 pts for playing Paper and 3 pts for Scissors
# 6 pts for win - 3pts for draw
for line in file:
    [him, me] = line.split()
    if (me == 'X'):  # rock
        score += 1
        if (him == "C"):  # rock scissors
            score += 6
        elif (him == "A"):  # rock rock
            score += 3
    elif (me == "Y"):  # paper
        score += 2
        if (him == "B"):  # paper paper
            score += 3
        elif (him == "A"):  # paper rock
            score += 6
    elif (me == "Z"):  # scissors
        score += 3
        if (him == "C"):  # scissors scissors
            score += 3
        elif (him == "B"):  # scissors paper
            score += 6
print("Problem 1: ", score)

# Problem 2 :
# A for Rock, B for Paper, and C for Scissors
# X for a lost, Y for a draw, and Z for wins
# 1 pts for playing rock, 2 pts for playing Paper and 3 pts for Scissors
file = open("input.txt", "r")
score2 = 0

for line in file:
    [him, result] = line.split()

    if (him == "A"):  # he plays rock
        if (result == "Z"):  # Win
            score2 += 6
            score2 += 2
        elif (result == "Y"):  # draw
            score2 += 3
            score2 += 1
        elif (result == "X"):  # lost
            score2 += 3
    if (him == "B"):  # he plays Paper
        if (result == "Z"):  # Win
            score2 += 6
            score2 += 3
        elif (result == "Y"):  # draw
            score2 += 3
            score2 += 2
        elif (result == "X"):  # lost
            score2 += 1
    if (him == "C"):  # he plays Scissors
        if (result == "Z"):  # Win
            score2 += 6
            score2 += 1
        elif (result == "Y"):  # draw
            score2 += 3
            score2 += 3
        elif (result == "X"):  # lost
            score2 += 2

print("Problem 2: ", score2)
