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