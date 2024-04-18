"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    Model.py
    Last edited: 2024-04-17 (YYYY-MM-DD)
    Version: 1.0

"""

import Node
import Link

import data

import random
import numpy as np

startNodes = []
endNodes = []

NO_OF_EPOCHS = 5
STRICTNESS = 0.99 # allowing a 15% error margin

def setup():
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
    epochId = 0
    while True:
        # print("epoch:", epochId)
        
        correctnessList = []
        for trainingSymbol in trainingSet:
            evaluation = evaluateWithNetwork(trainingSymbol[0])

            # print value endNodes
            # print("chance of symbol being 'O' is:", evaluation['O'])
            # print("chance of symbol being 'X' is:", evaluation['X'])

            # adjust correctness by lowest
            correctnessList.append(max(evaluation["O"], evaluation["X"]))
            
        correctnesBeforeChangingWeight = sum(correctnessList) / len(correctnessList)

        # adjust one weight of links to look for a more acurate outcome
        randomStartNodeId = random.choice(range(data.inputDim))
        randomLink = random.choice(startNodes[randomStartNodeId].outgoingLinks)
        randomLink.reCalculateWeight()

        correctnessList = []
        for trainingSymbol in trainingSet:
            evaluation = evaluateWithNetwork(trainingSymbol[0])

            # print value endNodes
            # print("chance of symbol being 'O' is:", evaluation['O'])
            # print("chance of symbol being 'X' is:", evaluation['X'])

            # adjust correctness by lowest
            correctnessList.append(max(evaluation["O"], evaluation["X"]))
            
            if evaluation["O"] > evaluation["X"] and trainingSymbol[1] == 'O':
                pass
            # where is the learning? in this system there is none
            
        correctnesAfterChangingWeight = sum(correctnessList) / len(correctnessList)

        if correctnesAfterChangingWeight < correctnesBeforeChangingWeight:
            # revert weight change because it did nothing good
            randomLink.weight = randomLink.previousWeights[-1]
            #print("Weight change didn't do good!")
        else:
            print("Weight change did do good!")
            print(correctnesAfterChangingWeight)

        if correctnesAfterChangingWeight >= STRICTNESS:
            break
        #print()

        epochId += 1

def evaluateWithNetwork(symbol):
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
    # source: https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
    # tested! --> Works!
    return [x for xs in xss for x in xs]

##########################################################################

# setup the model
setup()

# training
# for epochId in range(NO_OF_EPOCHS):
#     print("epoch:", epochId)

#     trainingEpoch(data.trainingSet)
#     print()

trainingEpochs(data.trainingSet)


# testing
results = []
for testcase in data.testSet:
    outcome = evaluateWithNetwork(testcase[0])
    
    print("Testcase:", testcase)
    if outcome['X'] >= STRICTNESS and outcome['O'] < STRICTNESS:
        print("Identified as 'X'")
        if testcase[1] == 'X':
            print("Identified correctly!")
            results.append(True)
        else:
            print("Identified wrongly!")
            results.append(False)
    elif outcome['O'] >= STRICTNESS and outcome['X'] < STRICTNESS:
        print("Identified as 'O'")
        if testcase[1] == 'O':
            print("Identified correctly!")
            results.append(True)
        else:
            print("Identified wrongly!")
            results.append(False)
    else:
        print("Could not identify symbol with certainty.")
        results.append(False)

    print()

# model outcome
print("SUCCESSFUL OUTOCME:", all(results))
print("SCORE:", results)