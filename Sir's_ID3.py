import numpy as np
import pandas as pd

USE_RANDOM = False


def getEntropy(target_col):
	elements, counts = np.unique(target_col, return_counts=True)
	entropy = np.sum([(-counts[i] / np.sum(counts)) * np.log2(counts[i] / np.sum(counts)) for i in range(len(elements))])
	return entropy


def getInfoGain(data, feature, tname):
	te = getEntropy(data[tname])
	print("entropy", round(float(te), 4))
	vals, counts = np.unique(data[feature], return_counts=True)
	we = np.sum([(counts[i] / np.sum(counts)) * getEntropy(data.where(data[feature] == vals[i]).dropna()[tname]) for i in range(len(vals))])
	Information_Gain = te - we
	print("IG", round(float(Information_Gain), 4))
	return Information_Gain


def ID3(data, f, tname, pnode):
	if len(np.unique(data[tname])) == 1:
		return np.unique(data[tname])[0]
	elif len(f) == 0:
		return pnode
	else:
		pnode = np.unique(data[tname])[np.argmax(np.unique(data[tname])[1])]
		item_values = [getInfoGain(data, feature, tname) for feature in f]
		bfi = np.argmax(item_values)
		bf = f[bfi]
		print(bf)
		tree = {bf: {}}
		f = [i for i in f if i != bf]
		for value in np.unique(data[bf]):
			sub_data = data.where(data[bf] == value).dropna()
			subtree = ID3(sub_data, f, tname, pnode)
			tree[bf][value] = subtree
		return tree


def predict(query, tree, default=1):
	for key in list(query.keys()):
		if key in list(tree.keys()):
			try:
				result = tree[key][query[key]]
			except:
				return default
			if isinstance(result, dict):
				return predict(query, result)
			else:
				return result


dataset = pd.read_csv('PlayTennis.csv')
if USE_RANDOM:
	# Train on Random Samples
	tdata = dataset.sample(frac=0.8)
else:
	# Train on Samples from 1-12 and 13-14 for testing
	tdata = dataset.iloc[:12, :]

print("The Training Dataset:\n", tdata)

f = ['Outlook', 'Temperature', 'Humidity', 'Wind']
tname = "PlayTennis"
pnode = None
tree = ID3(tdata, f, tname, pnode)
print("\nTree:\n", tree)

query = dataset.iloc[:, :].to_dict(orient="records")

# Testing


result = predict(query[12], tree, 1)
print("\n\nTesting sample 1:", query[12], "PREDICTED =>", result)

result = predict(query[13], tree, 1)
print("\nTesting sample 2:", query[13], "PREDICTED =>", result)
