"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    Model.py
    Last edited: 2024-04-18 (YYYY-MM-DD)
    Version: 1.1

"""

import Node
import Link

import data

import random
import numpy as np

startNodes = []
endNodes = []

NO_OF_EPOCHS = 5
TESTING_STRICTNESS = 0.51
TRAINING_STRICTNESS = 0.60

def setup():
    """
    Setup the model with startNodes, endNodes and links between them.
    """
    # setup start nodes
    for startNodeId in range(data.inputDim):
        startNodes.append(Node.Node())
    # setup end nodes
    for endNodeId in range(data.outputDim):
        endNodes.append(Node.Node())

    # setup links between all nodes
    for startNodeId in range(data.inputDim):
        for endNodeId in range(data.outputDim):
            startNodes[startNodeId].addOutgoingLink(Link.Link(endNodes[endNodeId]))

def trainingEpochs(trainingSet):
    """
    Train the model with trainingSet.
    """
    epochId = 0
    while True:
        print("epoch:", epochId)
        ##############################################################
        
        correctnessCounter = 0
        for trainingSymbol in trainingSet:
            evaluation = evaluateWithNetwork(trainingSymbol[0])

            for evalItemSymbol, evalItemValue in evaluation.items():
                if evalItemValue > TRAINING_STRICTNESS and evalItemSymbol == trainingSymbol[1]:
                    # guessed correctly
                    correctnessCounter += 1
            
        correctnesBeforeChangingWeight = correctnessCounter

        ##############################################################

        # adjust one weight of links to look for a more acurate outcome
        randomStartNodeId = random.choice(range(data.inputDim))
        randomLink = random.choice(startNodes[randomStartNodeId].outgoingLinks)
        randomLink.reCalculateWeight()

        ##############################################################

        correctnessCounter = 0
        for trainingSymbol in trainingSet:
            evaluation = evaluateWithNetwork(trainingSymbol[0])

            for evalItemSymbol, evalItemValue in evaluation.items():
                if evalItemValue > TRAINING_STRICTNESS and evalItemSymbol == trainingSymbol[1]:
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

def evaluateWithNetwork(symbol):
    """
    Evaluate a symbol (made up out of 3 times 3 times a '1' or '0') with the current Neural Network. Guess whether it is a 'X' or 'O'.
    """
    # reset start
    for startNodeId in range(data.inputDim):
        startNodes[startNodeId].hardReset()
    # reset end
    for endNodeId in range(data.outputDim):
        endNodes[endNodeId].hardReset()

    # assign value to startNodes
    s = denestNestedList(symbol)
    for startNodeId in range(data.inputDim):
        startNodes[startNodeId].addValue(s[startNodeId])

    # activate links (which automatically assign values to endNodes)
    for startNodeId in range(data.inputDim):
        startNodes[startNodeId].activateLinks()

    # use softmax function for determining endNode values
    endNodeValues = [endNodes[0].value, endNodes[1].value]
    normalizedEndNodeValues = np.exp(endNodeValues) / np.sum(np.exp(endNodeValues))
    # print(endNodeValues)

    # return value endNodes
    return {'O': normalizedEndNodeValues[0], 'X': normalizedEndNodeValues[1]}

def denestNestedList(xss):
    """
    Remove nested lists in list.
    source: https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
    """
    return [x for xs in xss for x in xs]

def testAndPrintResults(testSet):
    results = []
    for testcase in data.testSet:
        outcome = evaluateWithNetwork(testcase[0])
        
        print("Testcase:", testcase)
        if outcome['X'] >= TESTING_STRICTNESS and outcome['O'] < TESTING_STRICTNESS:
            print("Identified as 'X' (with a certainty of", round(outcome['X'], 2), ")")
            if testcase[1] == 'X':
                print("Identified correctly!")
                results.append(True)
            else:
                print("Identified wrongly!")
                results.append(False)
        elif outcome['O'] >= TESTING_STRICTNESS and outcome['X'] < TESTING_STRICTNESS:
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
            results.append(False)

    # model outcome
    print("SUCCESSFUL OUTOCME:", all(results))
    print("SCORE:", results)

##########################################################################

# setup the model
setup()

trainingEpochs(data.trainingSet)

# testing
testAndPrintResults(data.testSet)

