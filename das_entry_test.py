with open("data.csv") as f:
	maximas = []
	i = 0
	num_max = -float("inf")
	for line in f:
		num = float(line)
		if i < 200 and num > num_max:
			num_max = num
			maximas.append(str(num) + "\n")
			i = 0
			continue
		i += 1

with open("output.csv", "w") as f:
	f.writelines(maximas)

