"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    main.py
    Last edited: 2024-04-19 (YYYY-MM-DD)
    Version: 3.0

"""

import random

import data
import NeuralNetwork

# constants
TESTING_STRICTNESS = 0.51
TRAINING_STRICTNESS = 0.60

# decide how the hidden layers are structured
hiddenLayers = []
# # uncomment lines below to get a random number of nodes in the hidden dimensions
# for dimension in range(data.hiddenDim):
#     hiddenLayers.append(random.randint(1, 30))

# create a Neural Network with noOfInputs and noOfOutputs
nn = NeuralNetwork.NN(data.inputDim, data.outputDim, hiddenLayers)

# train Neural Network
nn.trainingEpochs(data.trainingSet, TRAINING_STRICTNESS)

print()

# test Neural Network
# nn.testAndPrintResults(data.testSet, TESTING_STRICTNESS)