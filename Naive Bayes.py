import csv
import math
import random
import statistics as st


def loadCsv(filename):
	lines = csv.reader(open(filename, "r"))
	dataset = list(lines)
	for i in range(1, len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	dataset = dataset[1:]
	return dataset


dataset = loadCsv('Diabetes.csv')

print('Diabetes Dataset loaded......\n')
print('Total instances available :', len(dataset))
print('Total attributes present  :', len(dataset[1]) - 1)


def splitDataset(dataset, splitRatio):
	testSize = int(len(dataset) * splitRatio)
	trainSet = list(dataset)
	testSet = []
	while len(testSet) < testSize:
		# randomly pic on instance from training data
		index = random.randrange(len(trainSet))
		testSet.append(trainSet.pop(index))

	return [trainSet, testSet]


# create a dictionary of classes 1 & 0 where the instances belonging to each class
def separateByClass(dataset):
	separated = {}
	for i in range(1, len(dataset)):
		x = dataset[i]
		if x[-1] not in separated:
			separated[x[-1]] = []
		separated[x[-1]].append(x)

	return separated


def compute_mean_std(dataset):
	mean_std = [(st.mean(attribute), st.stdev(attribute)) for attribute in zip(*dataset)];
	del mean_std[-1]  # exclude label

	return mean_std


def summarizeByClass(dataset):
	separated = separateByClass(dataset)
	summary = {}  # to store mean & std of positive & negative instances
	for classValue, instances in separated.items():
		# summaries is a dictionary of tuples(mean, std) for each class value
		summary[classValue] = compute_mean_std(instances)

	return summary


# For continuous attributes p is estimated using Gaussian distribution
def estimateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))

	return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent


def calculateClassProbabilities(summaries, testVector):
	p = {}
	# class &attributes p is estimated using Gaussian distribution
	for classValue, classSummaries in summaries.items():
		p[classValue] = 1

		for i in range(1, len(classSummaries)):
			mean, stdev = classSummaries[i]
			x = testVector[i]  # testVector's first attribute
			# use normal distribution
			p[classValue] *= estimateProbability(x, mean, stdev)

	return p


def predict(summaries, testVector):
	all_p = calculateClassProbabilities(summaries, testVector)
	bestLabel, bestProb = None, -1
	for lbl, p in all_p.items():  # assigns that class which has the highest prob
		if bestLabel is None or p > bestProb:
			bestProb = p
			bestLabel = lbl

	return bestLabel


def perform_classification(summaries, testSet):
	predictions = []
	for i in range(len(testSet)):
		result = predict(summaries, testSet[i])
		predictions.append(result)

	return predictions


def getAccuracy(testSet, predictions):
	correct = 0
	for i in range(1, len(testSet)):
		if testSet[i][-1] == predictions[i]:
			correct += 1

	return (correct / float(len(testSet))) * 100.0


splitRatio = 0.2
trainingSet, testSet = splitDataset(dataset, splitRatio)
print('\nDataset is split into training and testing set\n')
print('Training examples = {0}\nTesting examples  = {1}'.format(len(trainingSet), len(testSet)))

summaries = summarizeByClass(trainingSet)
# print('\nSummaries :\n')
# print(summaries)
# print()

predictions = perform_classification(summaries, testSet)
# print('\nPredictions :\n')
# print(predictions)

accuracy = getAccuracy(testSet, predictions)
print('\nAccuracy of the Naive Baysian Classifier is :', accuracy)
