import string

file = "./day3in.txt"

with open(file, "r") as ofile:
    contents = ofile.read().splitlines()

# for lines in file, split lines by half length
# iterate through te split lines and find the common character
# add the common character to a list

outcome = []

for line in contents:
    cut = int((len(line) / 2))
    first = line[cut:]
    second = line[:cut]
    for y in first:
        if y in second:
            outcome.append(y)
            break
        else:
            pass

# get number values and letters
numbers = [x for x in range(1, len(string.ascii_letters) + 1)]
letters = [x for x in string.ascii_letters]

# create dict from list comprehensions above
yes = dict(zip(letters, numbers))

# new list with values based on first list's keys

# FOR LOOP
#new_outcome = []
#for x in outcome:
#    new_outcome.append(yes.get(x))

# LIST COMPREHENSION
new_outcome = [yes.get(x) for x in outcome]

# print sum of output for answer
print(sum(new_outcome))

# check
print(len(outcome), len(new_outcome))
