"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    main.py
    Last edited: 2024-05-09 (YYYY-MM-DD)
    Version: 5.0

"""

import numpy as np
import NeuralNetwork

import data

import HelpFunctions

# define X (trainingset)
X = np.array(HelpFunctions.retrieveInputSets(data.trainingSet))

# define y (expected outcomes)
y = np.array(HelpFunctions.retrieveOutputSets(data.trainingSet))
print(X)
print(y)

nn = NeuralNetwork.NeuralNetwork(input_size=9, hidden_size=4, output_size=2)
nn.train(X, y, epochs=10000, learning_rate=0.1)

# define Z (testset)
Z = np.array([HelpFunctions.retrieveInputSets(data.testSet)])

# Test the trained model
output = nn.feedforward(Z)
print("Predictions after training:")
print(output)
