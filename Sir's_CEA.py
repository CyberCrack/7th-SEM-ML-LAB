f = open('Newspaper.csv', 'r')
lst = f.readline().rstrip('\n').split(',')
length = len(lst)
f.close()

f = open('Newspaper.csv', 'r')

count = 1
shypo = ['0'] * (length - 1)
ghypo = ['?'] * (length - 1)
print("Initial Specific Hypothesis S0=", shypo)
print("Initial General Hypothesis G0 =", ghypo, "\n")

for value in f:
	lst = value.rstrip('\n').split(',')
	if lst[length - 1].lower() == "yes":
		for i in range(0, length - 1):
			if shypo[i] != lst[i] and shypo[i] != '0':
				shypo[i] = '?'
			else:
				shypo[i] = lst[i]
	elif lst[length - 1].lower() == "no":
		ghypo.clear()
		for i in range(0, length - 1):

			if shypo[i] != lst[i] and shypo[i] != '?':
				temp_list = ['?'] * i
				temp_list = temp_list + [shypo[i]]
				temp_list = temp_list + (['?'] * (length - 2 - i))
				if temp_list not in ghypo:
					ghypo.append(temp_list)
	print("S Hypothesis after row", count, " = ", shypo)
	print("G Hypothesis after row", count, " = ", ghypo, "\n")
	count = count + 1
temp_ghypo = list()
for i in range(len(ghypo)):
	for j in range(len(ghypo[i])):
		if ghypo[i][j] != '?' and ghypo[i][j] == shypo[j]:
			temp_ghypo.append(ghypo[i])
print("Final SHypothesis:", shypo)
print("Final GHypothesis:", temp_ghypo)
f.close()
