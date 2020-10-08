import csv

# open the CSVFile and keep all rows as list of tuples
with open('EnjoySport.csv') as csvFile:
	examples = [tuple(line) for line in csv.reader(csvFile)]
# print(examples)


def get_domains(examples):
	# set function returns the unordered collection of items with no duplicates
	d = [set() for i in examples[0]]
	for x in examples:
		# Enumerate() function adds a counter to an iterable and returns it in a form of enumerate object i.e(index,value)
		for i, xi in enumerate(x):
			d[i].add(xi)
	return [list(sorted(x)) for x in d]


# Test the get_domains function
get_domains(examples)


def g_0(n):
	return ('?',) * n


def s_0(n):
	return ('0',) * n


def more_general(h1, h2):
	more_general_parts = []
	for x, y in zip(h1, h2):
		mg = x == '?' or (x != '0' and (x == y or y == '0'))
		more_general_parts.append(mg)
	return all(more_general_parts)  # Returns true if all elements of list or tuple are true


# Function to check whether train examples are consistent with hypothesis
def consistent(hypothesis, example):
	return more_general(hypothesis, example)


def min_generalizations(h, x):
	h_new = list(h)
	for i in range(len(h)):
		if not consistent(h[i:i + 1], x[i:i + 1]):
			if h[i] != '0':
				h_new[i] = '?'
			else:
				h_new[i] = x[i]
	return [tuple(h_new)]


# Function to generalize Specific hypto
def generalize_S(x, G, S):
	S_prev = list(S)
	for s in S_prev:
		if s not in S:
			continue
		if not consistent(s, x):
			S.remove(s)
			Splus = min_generalizations(s, x)
			# Keep only generalizations that have a counterpart in G
			S.update([h for h in Splus if any([more_general(g, h)
											   for g in G])])
			# Remove from S any hypothesis more general than any other hypothesis in S
			S.difference_update([h for h in S if
								 any([more_general(h, h1)
									  for h1 in S if h != h1])])
	return S


def min_specializations(h, domains, x):
	results = []
	for i in range(len(h)):
		if h[i] == '?':
			for val in domains[i]:
				if x[i] != val:
					h_new = h[:i] + (val,) + h[i + 1:]
					results.append(h_new)
		elif h[i] != '0':
			h_new = h[:i] + ('0',) + h[i + 1:]
			results.append(h_new)
	return results


def specialize_G(x, domains, G, S):
	G_prev = list(G)
	for g in G_prev:
		if g not in G:
			continue
		if consistent(g, x):
			G.remove(g)
			Gminus = min_specializations(g, domains, x)
			# Keep only specializations that have a counterpart in S
			G.update([h for h in Gminus if any([more_general(h, s)
												for s in S])])
			# Remove hypothesis less general than any other hypothesis in G
			G.difference_update([h for h in G if
								 any([more_general(g1, h)
									  for g1 in G if h != g1])])
	return G


def candidate_elimination(examples):
	domains = get_domains(examples)[:-1]

	G = set([g_0(len(domains))])
	S = set([s_0(len(domains))])
	i = 0
	print('All the hypotheses in General and Specific boundary are:\n')
	print('\n G[{0}]:'.format(i), G)
	print('\n S[{0}]:'.format(i), S)
	for xcx in examples:
		i = i + 1
		x, cx = xcx[:-1], xcx[-1]  # Splitting data into attributes and decisions
		if cx == 'Yes':  # x is positive example
			G = {g for g in G if consistent(g, x)}
			S = generalize_S(x, G, S)
		else:  # x is negative example
			S = {s for s in S if not consistent(s, x)}
			G = specialize_G(x, domains, G, S)
		print('\n G[{0}]:'.format(i), G)
		print('\n S[{0}]:'.format(i), S)
	return


candidate_elimination(examples)
