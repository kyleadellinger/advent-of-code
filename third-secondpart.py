
import string

file = "./day3in.txt"

with open(file, "r") as ofile:
    contents = ofile.read().splitlines()

# create list of the single value every three lines shares
threes = []
temp_list = []
for x in contents:
    temp_list.append(x)
    if len(temp_list) == 3:
        threes.append(temp_list)
        temp_list = []
    else:
        pass
# create list of single matching character from sets of three strings at a time
outcome = []
for x in threes:
    first, second, third = x[0], x[1], x[2]
    for y in first:
        if y in second and y in third:
            outcome.append(y)
            break
        else:
            pass
print(outcome)
print(len(outcome))

# get number values and letters
numbers = [x for x in range(1, len(string.ascii_letters) + 1)]
letters = [x for x in string.ascii_letters]

# create dict from list comprehensions above
yes = dict(zip(letters, numbers))

new_outcome = [yes.get(x) for x in outcome]

# print sum of output for answer
print(sum(new_outcome))

# checks
print(len(outcome), len(new_outcome))
print(len(threes))
