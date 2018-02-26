import string


# make strings more uniform for comparison
def PrepString(str_input):

    # brute force replacement
    # there are more optimized ways of doing this
    for character in string.punctuation:
        str_input = str_input.replace(character,"")

    # convert everything to lower case to make it case insensitive
    str_input = str_input.lower()

    return str_input


# returns the total number of words in an input phrase
def TotalWords(str_input):
    words = PrepString(str_input).split()
    return len(words)

# returns the total number of characters in an input phrase
def PhraseLength(str_input):
    return len(PrepString(str_input))

# returns an array of words and their count in a phrase
def WordCount(str_input):

    # initialize dictionary of results
    dict_WordSet = {}

    words = PrepString(str_input).split()
    for word in words:
        if word in dict_WordSet:
            dict_WordSet[word] += 1
        else:
            dict_WordSet[word] = 1

    # todo: order results from largest to smallest values
    return dict_WordSet

# returns a list of the distinct words in a phrase
def DistinctWords(str_input):

    dict_WordSet = WordCount(str_input)

    return dict_WordSet.keys()

# returns the count of the distinct number of words in a phrase
def DistinctWordCount(str_input):

    dict_WordSet = WordCount(str_input)

    return len(dict_WordSet.keys())
