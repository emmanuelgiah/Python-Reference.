from numpy import exp, array, random, dot

class NeuralNetwork():
	def __init__(self):
		#seed the random number generator, so it generates the same numbers
		#every time the program runs
		random.seed(1)

		#we model a single neuron, with 3 input ocnnections and 1 output connection.
		#we assign random weights to a 3 x 1 matrix with values in the range -1 to 1
		# and mean 0
		self.synaptic_weights = 2 * random.random((3, 1)) - 1;

	def __sigmoid(self, x):
		return 1 /(1 + exp(-x));

	def __sigmoid_derivative(self, x):
		return x * (1-x);

	def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
		for iteration in range(number_of_training_iterations):
			#pass the training set through our neural net
			output = self.predict(training_set_inputs);

			#calculate the error
			error = training_set_outputs - output;

			#multiply the error by the input ad again by the gradient of the sigmoid curve
			adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output));

			#adjust the weights
			self.synaptic_weights += adjustment;

	def predict(self, inputs):
		#pass inputs through our neural netowrk
		return self.__sigmoid(dot(inputs, self.synaptic_weights));


if __name__ == "__main__":
	 #initialize a single neuron neural network
	 neural_network = NeuralNetwork();

	 print ('Random Starting Synaptic weights:')
	 print (neural_network.synaptic_weights)

	 #The training set. We have 4 examples, each consisting of 3 input values
	 # and 1 output value.
	 training_set_inputs = array([[0, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 0]]);
	 training_set_outputs = array([[0, 1, 0, 0]]).T

	 #train the neural network suing a training set
	 #Do it 10,000 times and make small adjustments each time
	 neural_network.train(training_set_inputs, training_set_outputs, 10000);

	 print ('New Synaptic Weights After Training: ')
	 print (neural_network.synaptic_weights)

	 #Test the neural network
	 print ('Considering new situation [1, 1, 0] -> ?: ')
	 print ((neural_network.predict(array([1, 1, 0]))));