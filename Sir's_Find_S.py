with open('EnjoySport.csv') as f:
	lst = [line.rstrip('\n').split(',') for line in f]
	print(lst)
	length = len(lst[0]);print(length)

f.close()

f = open('EnjoySport.csv', 'r')
count = 1
hypo = ['0'] * (length - 1)
print("Initial Hypothesis is = ", hypo)

for value in f:
	lst = value.rstrip('\n').split(',')
	if lst[-1].lower() == "yes":
		for i in range(0, length - 1):
			if hypo[i] != lst[i] and hypo[i] != '0':
				hypo[i] = '?'
			else:
				hypo[i] = lst[i]
	print("Hypothesis after row", count, " ", hypo)
	count = count + 1
f.close()
