"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    main.py
    Last edited: 2024-04-18 (YYYY-MM-DD)
    Version: 1.2

"""

import data
import NeuralNetwork

# constants
TESTING_STRICTNESS = 0.51
TRAINING_STRICTNESS = 0.60

# create a Neural Network with noOfInputs and noOfOutputs
nn = NeuralNetwork.NN(data.inputDim, data.outputDim)

# train Neural Network
nn.trainingEpochs(data.trainingSet, TRAINING_STRICTNESS)

print()

# test Neural Network
nn.testAndPrintResults(data.testSet, TESTING_STRICTNESS)