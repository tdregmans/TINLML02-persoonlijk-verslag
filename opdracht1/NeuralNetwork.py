"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    NeuralNetwork.py
    Last edited: 2024-04-19 (YYYY-MM-DD)
    Version: 3.0

"""

import random
import numpy as np

STANDARD_TESTING_STRICTNESS = 0.51
STANDARD_TRAINING_STRICTNESS = 0.85 # Allow a 15% error margin

class NN:
    def __init__(self, noOfInputs, noOfOutputs, hiddenLayers = []):
        """
        Neural Network constructor.
        There is an optional parameter `hiddenLayers` which accepts a list with Integers (> 0) representing the hidden layers and the dimension of that layer.
        For example, [3, 4, 9] stands for 3 hidden layers: the first has 3 nodes, the second has 4 nodes and the last hidden layer has 9 nodes.
        """
        self.network = []
        
        self.__setup(noOfInputs, noOfOutputs, hiddenLayers)

    def __setup(self, noOfInputs, noOfOutputs, hiddenLayers):
        """
        Setup the model with matrices in self.network.
        """
        allLayers = [noOfInputs] + hiddenLayers + [noOfOutputs]

        for layerId in range(len(allLayers) - 1):
            matrix = []
            for origin in range(allLayers[layerId]):
                row = []
                for target in range(allLayers[layerId + 1]):
                    row.append(random.random())
                matrix.append(row)
            self.network.append(matrix)
        
        print("Setup completed!")

    def trainingEpochs(self, trainingSet, trainingStrictness = STANDARD_TRAINING_STRICTNESS):
        """
        Train the model with trainingSet.
        """
        epochId = 0
        while True:
            print("Epoch:", epochId)
            ##############################################################
            
            correctnessCounter = 0
            for trainingSymbol in trainingSet:
                evaluation = self.evaluateWithNetwork(trainingSymbol[0])

                for evalItemSymbol, evalItemValue in evaluation.items():
                    if evalItemValue > trainingStrictness and evalItemSymbol == trainingSymbol[1]:
                        # guessed correctly
                        correctnessCounter += 1
                
            correctnesBeforeChangingWeight = correctnessCounter

            ##############################################################

            # adjust one weight of links to look for a more acurate outcome
            allOriginNodes = self.startNodes + self.hiddenNodes
            while True: # use loop to avoid taking 
                randomNode = random.choice(allOriginNodes)
                if isinstance(randomNode, list):
                    randomNode = randomNode[0]
                if len(randomNode.outgoingLinks) > 0:
                    randomLink = random.choice(randomNode.outgoingLinks)
                    randomLink.reCalculateWeight()

                    break
                print("!")

            ##############################################################

            correctnessCounter = 0
            for trainingSymbol in trainingSet:
                evaluation = self.evaluateWithNetwork(trainingSymbol[0])

                for evalItemSymbol, evalItemValue in evaluation.items():
                    if evalItemValue > trainingStrictness and evalItemSymbol == trainingSymbol[1]:
                        # guessed correctly
                        correctnessCounter += 1
                
            correctnesAfterChangingWeight = correctnessCounter

            ##############################################################

            if correctnesAfterChangingWeight < correctnesBeforeChangingWeight:
                # revert weight change because it did nothing good
                randomLink.weight = randomLink.previousWeights[-1]

            if correctnesAfterChangingWeight >= len(trainingSet):
                break
            #print()

            epochId += 1

        print("Training completed in", epochId, "epochs.")

    def evaluateWithNetwork(self, symbol):
        """
        Evaluate a symbol (made up out of 3 times 3 times a '1' or '0') with the current Neural Network. Guess whether it is a 'X' or 'O'.
        """
        # # reset start
        # for startNodeId in range(self.noOfInputs):
        #     self.startNodes[startNodeId].hardReset()
        # # reset end
        # for endNodeId in range(self.noOfOutputs):
        #     self.endNodes[endNodeId].hardReset()

        # # assign value to startNodes
        # s = self.__denestNestedList(symbol)
        # for startNodeId in range(self.noOfInputs):
        #     self.startNodes[startNodeId].addValue(s[startNodeId])

        # # activate links (which automatically assign values to endNodes)
        # for startNodeId in range(self.noOfInputs):
        #     self.startNodes[startNodeId].activateLinks()

        
        # self.network[layerId][origin][target]

        nodeValues = self.__denestNestedList(symbol)

        for layerId in range(len(self.network)):
            layer = self.network[layerId]

            nextNodeValues = None # something with nodeValues and layer

            # use softmax function for determining values
            nodeValues = np.exp(nextNodeValues) / np.sum(np.exp(nextNodeValues))
            # print(endNodeValues)

        # return value endNodes
        return {'O': nodeValues[0], 'X': nodeValues[1]}

    def __denestNestedList(self, xss):
        """
        Remove nested lists in list.
        source: https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
        """
        return [x for xs in xss for x in xs]

    def testAndPrintResults(self, testSet, testStrictness = STANDARD_TESTING_STRICTNESS):
        """
        Test the Neural Network with testSet and print the results.
        """
        results = []
        testcaseId = 0
        for testcase in testSet:
            outcome = self.evaluateWithNetwork(testcase[0])
            
            print("Testcase", testcaseId)
            if outcome['X'] >= testStrictness and outcome['O'] < testStrictness:
                print("Identified as 'X' (with a certainty of", round(outcome['X'], 2), ")")
                if testcase[1] == 'X':
                    print("Identified correctly!")
                    results.append(True)
                else:
                    print("Identified wrongly!")
                    results.append(False)
            elif outcome['O'] >= testStrictness and outcome['X'] < testStrictness:
                print("Identified as 'O' (with a certainty of", round(outcome['O'], 2), ")")
                if testcase[1] == 'O':
                    print("Identified correctly!")
                    results.append(True)
                else:
                    print("Identified wrongly!")
                    results.append(False)
            else:
                print("Could not identify symbol with certainty.")
                print("Best guess:", outcome)
                print("Should have been:", testcase[1])
                results.append(False)
            testcaseId += 1

        print()
        
        # model outcome
        print("SUCCESSFUL OUTCOME:", all(results))
        print("SCORE:", results)


