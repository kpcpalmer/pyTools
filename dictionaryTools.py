def mergeDictionaries( dictA, dictB ):
    # Description:
    #   Merges two dictionaries into one with all keys from both
    #   If a key is shared, the value from dictB will be used
    #
    # inputs:
    #   dictA:  A dictionary
    #   dictB:  Another dictionary
    #
    # outputs:
    #   mergedDict: Merged dictionary with all keys from both inputs

    mergedDict = {}
    
    for key in dictA:
        mergedDict[key] = dictA[key]

    for key in dictB:
        mergedDict[key] = dictB[key]

    return mergedDict
