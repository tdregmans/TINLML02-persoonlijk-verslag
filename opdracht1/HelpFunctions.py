def denestNestedList(xss):
    """
    Remove nested lists in list.
    source: https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
    """
    return [x for xs in xss for x in xs]

def retrieveInputSets(sets):
    """
    Retrieve all inputs from a trainingset or testset and denest the inputs.
    """
    out = []
    for item in sets:
        out.append(denestNestedList(item[0]))
    
    return out

def retrieveOutputSets(sets):
    """
    Retrieve all outputs from a trainingset and convert output symbol to a list with probability for each symbol.
    """
    out = []
    for item in sets:
        out.append(symbolToExpectedOut(item[1]))
    
    return out

def symbolToExpectedOut(symbol):
    """
    Convert output symbol to a list with probability for each symbol.
    Hardcoded based on Opdracht1.
    'O' results in [0, 1]
    'X' results in [1, 0]
    """
    if symbol == 'O':
        return [0, 1]
    elif symbol == 'X':
        return [1, 0]
    else:
        ValueError(symbol)

def effectivelyPrintOutput(outputs, expectedOutputs):
    """
    Print the results in a clear way.
    """
    results = []

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