import numpy as np
import pandas as pd

df = pd.read_csv("Find_S_data.csv", header=None)
X = np.array(df.values)[:, :-1]
y = np.array(df.values)[:, -1]


def findSAlgo(features: np.ndarray, target: np.ndarray):
	specificHypothesis = ['ϕ'] * features.shape[1]
	# Get first positive item as the hypothesis
	for index, value in enumerate(target):
		print("Item: ", index, "specificHypothesis: ", specificHypothesis)
		if value.lower() == 'yes':
			specificHypothesis = list(features[index])
			break
	# Normal Find-S Algorithm
	for index in range(len(features)):
		print("Item: ", index, "specificHypothesis: ", specificHypothesis)
		if target[index].lower() == 'yes':
			for attribute_index in range(features.shape[1]):
				if features[index][attribute_index] != specificHypothesis[attribute_index]:
					specificHypothesis[attribute_index] = '?'
	return specificHypothesis


print("Final: ", findSAlgo(X, y))
