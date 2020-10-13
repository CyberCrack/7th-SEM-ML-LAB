import numpy as np
import pandas as pd

df = pd.read_csv("Find_S_data.csv", header=None)
X = np.array(df.values)[:, :-1]
y = np.array(df.values)[:, -1]


def findSAlgo(features: np.ndarray, target: np.ndarray):
	specificHypothesis = ['ϕ'] * features.shape[1]
	fromIndex = 0
	# Get first positive item as the hypothesis
	for index, value in enumerate(target):
		print("Item: ", index, "specificHypothesis: ", specificHypothesis)
		fromIndex = index
		if value.lower() == 'yes':
			specificHypothesis = list(features[index])
			break
	# Normal Find-S Algorithm
	for index in range(fromIndex + 1, len(features)):
		if target[index].lower() == 'yes':
			for attribute_index in range(features.shape[1]):
				if features[index][attribute_index] != specificHypothesis[attribute_index]:
					specificHypothesis[attribute_index] = '?'

		print("Item: ", index, "specificHypothesis: ", specificHypothesis)
	return specificHypothesis


print("Final: ", findSAlgo(X, y))
