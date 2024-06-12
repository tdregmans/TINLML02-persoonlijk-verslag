"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    NeuralNetwork.py
    Last edited: 2024-06-12 (YYYY-MM-DD)
    Version: 6.0

"""

import numpy as np

class NeuralNetwork:
    def __init__(self, noOfInputs, noOfHiddenNodes, noOfOutputs):
        """
        Set up a Neural Network with a number of inputs, hidden nodes and outputs.
        The weights of the links between the nodes are randomly set.
        """
        self.noOfInputs = noOfInputs
        self.noOfHiddenNodes = noOfHiddenNodes
        self.noOfOutputs = noOfOutputs

        # setup the network with random weights
        self.weightsLayer1 = np.random.randn(self.noOfInputs, self.noOfHiddenNodes)
        self.weightsLayer2 = np.random.randn(self.noOfHiddenNodes, self.noOfOutputs)

        # start with no biases
        self.biasesLayer1 = np.zeros((1, self.noOfHiddenNodes))
        self.biasesLayer2 = np.zeros((1, self.noOfOutputs))
        
    def __denestNestedList(xss):
        """
        Remove nested lists in list.
        source: https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
        """
        return [x for xs in xss for x in xs]

    def __retrieveInputSets(sets):
        """
        Retrieve all inputs from a trainingset or testset and denest the inputs.
        """
        out = []
        for item in sets:
            out.append(NeuralNetwork.__denestNestedList(item[0]))
        
        return out

    def __retrieveOutputSets(sets):
        """
        Retrieve all outputs from a trainingset and convert output symbol to a list with probability for each symbol.
        """
        out = []
        for item in sets:
            if item[1] == 'O':
                out.append([0, 1])
            elif item[1] == 'X':
                out.append([1, 0])

        return out

    def activation(x):
        """
        Activation function, used to calulate the activation in a numpy matrix.
        """
        return 1 / (1 + np.exp(-x))

    def activationDerivative(x):
        """
        Activation derivative function, used to calulate the derivative of the activation to determine the delta of the value.
        """
        return x * (1 - x)

    def feedforward(self, X):
        """
        Use the network to predict a outcome, or a set of outcomes.
        """
        # calulate the activation and values of the first layer
        self.activationLayer1 = np.dot(X, self.weightsLayer1) + self.biasesLayer1
        self.valuesLayer1 = NeuralNetwork.activation(self.activationLayer1)

        # calulate the activation and values of the second layer
        self.activationLayer2 = np.dot(self.valuesLayer1, self.weightsLayer2) + self.biasesLayer2
        self.valuesLayer2 = NeuralNetwork.activation(self.activationLayer2)

        return self.valuesLayer2

    def backwardPropagation(self, X, y, learningRate):
        """
        Use the backward propagation algorithm to adjust the weights and biases of the network.
        """
        # calulate the activation and values of the second layer
        errorLayer2 = y - self.valuesLayer2
        differenceErrorLayer2 = errorLayer2 * NeuralNetwork.activationDerivative(self.valuesLayer2)

        # calulate the activation and values of the first layer
        errorLayer1 = np.dot(differenceErrorLayer2, self.weightsLayer2.T)
        differenceErrorLayer1 = errorLayer1 * NeuralNetwork.activationDerivative(self.valuesLayer1)

        # update the weights and biases
        self.weightsLayer2 += np.dot(self.valuesLayer1.T, differenceErrorLayer2) * learningRate
        self.biasesLayer2 += np.sum(differenceErrorLayer2, axis=0, keepdims=True) * learningRate
        
        self.weightsLayer1 += np.dot(X.T, differenceErrorLayer1) * learningRate
        self.biasesLayer1 += np.sum(differenceErrorLayer1, axis=0, keepdims=True) * learningRate

    def trainNetwork(self, trainData, noOfEpochs, learningRate):
        """
        Train the network with train data in a given no of epochs.
        """
        X = np.array(NeuralNetwork.__retrieveInputSets(trainData))
        y = np.array(NeuralNetwork.__retrieveOutputSets(trainData))
        
        for epoch in range(noOfEpochs):
            
            # make prediction and use back propagation algorithm
            output = self.feedforward(X)
            self.backwardPropagation(X, y, learningRate)
            
            # calculate loss
            loss = np.mean(np.square(y - output))
            print(f"Epoch {epoch}, Loss:{loss}")

    def predict(self, Z):
        """
        Use the network to predict whether a symbol is a 'X' or 'O'.
        """
        return self.feedforward(np.array(NeuralNetwork.__retrieveInputSets(Z)))
    
    def print(self, outputs, testset):
        """
        Print the results in a clear way.
        """
        results = []
        expectedOutputs = NeuralNetwork.__retrieveOutputSets(testset)

        for outputId in range(len(outputs)):
            output = outputs[outputId]
            expectedOutput = expectedOutputs[outputId]
            
            print("Testcase", outputId)

            if output[0] > output[1]:
                print("Identified as 'O' (with a certainty of", round(max(output), 2), ")")
                if expectedOutput[0] > expectedOutput[1]:
                    print("Identified correctly!")
                    results.append(True)
                else:
                    print("Identified wrongly!")
                    results.append(False)
            elif output[0] < output[1]:
                print("Identified as 'X' (with a certainty of", round(max(output), 2), ")")
                if expectedOutput[0] < expectedOutput[1]:
                    print("Identified correctly!")
                    results.append(True)
                else:
                    print("Identified wrongly!")
                    results.append(False)
            else:
                print("Could not identify symbol.")
                print("Outcome was 50/50!")
                results.append(False)

        print()
        
        # model outcome
        print("SUCCESSFUL OUTCOME:", all(results))
        print("SCORE:", results)