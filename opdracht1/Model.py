"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    Node.py
    Last edited: 2024-04-15 (YYYY-MM-DD)
    Version: 1.0

"""

import Node
import Link

import data

startNodes = []
endNodes = []
links = []

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
    for startNodeId in range(data.inputDim):
        startNodes[startNodeId].hardReset()
    
    for startNodeId in range(data.inputDim):
        print(denestNestedList(trainingSet))
        startNodes[startNodeId].addValue(denestNestedList(trainingSet)[startNodeId])

def denestNestedList(xss):
    # source: https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
    # tested! --> Works!
    return [x for xs in xss for x in xs]

##########################################################################

setup()

# training
for epochId in range(len(data.trainingSet)):
    print("epoch:", epochId)

    runEpoch(data.trainingSet[epochId][0])


