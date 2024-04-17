"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    Node.py
    Last edited: 2024-04-17 (YYYY-MM-DD)
    Version: 1.0

"""

import Node
import Link

import data

startNodes = []
endNodes = []

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

def runEpoch(trainingSet):
    # reset nodes
    for startNodeId in range(data.inputDim):
        startNodes[startNodeId].hardReset()
    
    # assign value to startNodes
    s = denestNestedList(trainingSet[0])
    for startNodeId in range(data.inputDim):
        startNodes[startNodeId].addValue(s[startNodeId])

    # activate links
    for startNodeId in range(data.inputDim):
        startNodes[startNodeId].activateLinks()

    # print outcome
    print("chance of symbol being 'O' is:", endNodes[0].value)
    print("chance of symbol being 'X' is:", endNodes[1].value)

    # run 
    
def test(testSet):
    return {'O': 1, 'X': 0}

def denestNestedList(xss):
    # source: https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
    # tested! --> Works!
    return [x for xs in xss for x in xs]

##########################################################################

setup()

# training
for epochId in range(len(data.trainingSet)):
    print("epoch:", epochId)

    runEpoch(data.trainingSet[epochId])
    print()

# testing
STRICTNESS = 0.85 # allowing a 15% error margin
wronglyIdentifiedSymbolExists = False
for testcase in data.testSet:
    outcome = test(testcase)
    
    print("Testcase:", testcase)
    if outcome['X'] >= STRICTNESS and outcome['O'] < STRICTNESS:
        print("Identified as 'X'")
        if testcase[1] == 'X':
            print("Identified correctly!")
        else:
            print("Identified wrongly!")
            wronglyIdentifiedSymbolExists = True
    elif outcome['O'] >= STRICTNESS and outcome['X'] < STRICTNESS:
        print("Identified as 'O'")
        if testcase[1] == 'O':
            print("Identified correctly!")
        else:
            print("Identified wrongly!")
            wronglyIdentifiedSymbolExists = True
    else:
        print("Could not identify symbol with certainty.")
        wronglyIdentifiedSymbolExists = True

    print()

# model outcome
print("SUCCESSFUL OUTOCME:", not wronglyIdentifiedSymbolExists)