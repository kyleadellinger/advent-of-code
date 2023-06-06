file = "./calories"
with open(file, "r") as ofile:
    calories = ofile.readlines()
temp_count = 0
cal_list = []
for line in calories:
    if line == "\n":
        cal_list.append(temp_count)
        temp_count = 0
    elif line != "\n":
        temp_count += int(line.strip("\n"))
print(max(cal_list))

cal_list.sort()
top_three = [int(cal_list[-1]), int(cal_list[-2]), int(cal_list[-3])]
print(sum(top_three))
