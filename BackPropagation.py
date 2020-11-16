import numpy as np  # numpy is commonly used to process number

X = np.array([[2, 9], [3, 6], [4, 8]])  # Features ( Hrs Slept, Hrs Studied)
print(X)
y = np.array([[92], [86], [89]])  # Labels (Marks obtained)
print(y)
X = X / np.amax(X, axis=0)  # Normalize
y = y / 100


def sigmoid(x):
	return 1 / (1 + np.exp(-x))


def sigmoid_grad(x):
	return x * (1 - x)


# variable initialization

epoch = 1000  # Setting training iterations
eta = 0.1  # Setting Learning rate (eta)
input_neurons = 2  # number of features in data set 
hidden_neurons = 3  # number of hidden Layers neurons
output_neurons = 1  # number of neurons at output layer
# weight and bias Random initialization

wh = np.random.uniform(size=(input_neurons, hidden_neurons))  # 2x3
bh = np.random.uniform(size=(1, hidden_neurons))  # 1x3 
wout = np.random.uniform(size=(hidden_neurons, output_neurons))  # 3x1
bout = np.random.uniform(size=(1, output_neurons))  # 1*1
output = np.ndarray([])
for i in range(epoch):
	# Forward Propagation
	h_ip = np.dot(X, wh) + bh  # Dot product + bias
	h_act = sigmoid(h_ip)  # Activation function
	o_ip = np.dot(h_act, wout) - bout
	output = sigmoid(o_ip)
	# Error at output Layer
	Eo = y - output  # Error at op 
	outgrad = sigmoid_grad(output)
	d_output = Eo * outgrad  # Errj-Oj(1-Oj)(Tj:Oj) 
	# Error at Hidden Later
	Eh = np.dot(d_output, wout.T)  # .T Means transpose 
	hiddengrad = sigmoid_grad(h_act)  # How much hidden layer wts contributed to error
	d_hidden = Eh * hiddengrad

	wout += np.dot(h_act.T, d_output) * eta  # Dot product of nextLayerError and currentLayerOutput
	wh += np.dot(X.T, d_hidden) * eta

print("Normalized Input: \n", X)
print("Actual Output: \n", y)
print("Predicted Output: \n", output)
