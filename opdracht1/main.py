"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    main.py
    Last edited: 2024-06-12 (YYYY-MM-DD)
    Version: 6.0

"""

import data
import NeuralNetwork

nn = NeuralNetwork.NeuralNetwork(data.inputDim, data.hiddenDim, data.outputDim)
nn.trainNetwork(data.trainingSet, noOfEpochs=5000, learningRate=0.1)

# Test the trained model
output = nn.predict(data.testSet)

print("Predictions after training:")
nn.print(output, data.testSet)
