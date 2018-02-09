# returns the total number of words in an input phrase
def TotalWords(str_input):
    words = str_input.split()
    return len(words)

# returns the total number of characters in an input phrase
def PhraseLength(str_input):
    return len(str_input)

# returns an array of words and their count in a phrase
def WordCount(str_input):

    # initialize dictionary of results
    dict_WordSet = {}

    words = str_input.split()
    for word in words:
        if word in dict_WordSet:
            dict_WordSet[word] += 1
        else:
            dict_WordSet[word] = 1

    # todo: order results from largest to smallest values
    return dict_WordSet
