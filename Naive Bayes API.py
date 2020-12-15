import pandas as pd

msg = pd.read_csv("NaiveText.csv")
X = msg['message']
Y = msg['label']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y)

from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer()
xtrain_dtm = count_vect.fit_transform(X_train)

xtest_dtm = count_vect.transform(X_test)
# print(xtest_dtm)

from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()
clf.fit(xtrain_dtm, y_train)
predicted = clf.predict(xtest_dtm)
print('\nClassification results of testing samples are given below')
for doc, p in zip(X_test, predicted):
	pred = 'pos' if p == 1 else 'neg'
	print(doc, '-->', pred)

from sklearn import metrics

print('\nAccuracy metrics')
print('Accuracy of the classifier is', metrics.accuracy_score(y_test, predicted))
print('Recall :', metrics.recall_score(y_test, predicted), '\nPrecision :', metrics.precision_score(y_test, predicted))
print('Confusion matrix')
print(metrics.confusion_matrix(y_test, predicted))
