file = "./day2in.txt"
# first column opponent, a rock, b paper, c scissors
# second column what you play, x rock, y paper, z scissors
# score 1 rock, 2 paper 3 scissors 
# 0 lost, 3 tie, 6 win
win = 6
lose = 0
tie = 3
rock = 1
paper = 2
scissors = 3
my_total_score = 0

# read, string; readlines list with \n; read().splitlines() list without \n
# part 2, x lose; y draw; z win, second column
with open(file, "r") as ofile:
    contents = ofile.read().splitlines()

for h in contents:
    for i, j in h.replace(" ","").split():
        if i == "A" and j == "X":
            my_total_score += lose + scissors
        elif i == "B" and j == "X":
            my_total_score += lose + rock
        elif i == "C" and j == "X":
            my_total_score += lose + paper
        elif i == "A" and j == "Y":
            my_total_score += tie + rock
        elif i == "A" and j == "Z":
            my_total_score += win + paper
        elif i == "B" and j == "Y":
            my_total_score += tie + paper
        elif i == "B" and j == "Z":
            my_total_score += win + scissors
        elif i == "C" and j == "Z":
            my_total_score += win + rock
        elif i == "C" and j == "Y":
            my_total_score += tie + scissors
        else:
            print("there are some issues, or you missed something")

print(f"My score: {my_total_score}")
