# import helper libraries
import sys

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


# Get input from the command line
# argv[0] is the name of the script, first input starts at argv[1]
str_input = sys.argv[1]


# main routine

# todo: preprocess string to remove punctuation
# todo: preprocess string to normalize casing

TotalWords = TotalWords(str_input)
PhraseLength = PhraseLength(str_input)
WordCount = WordCount(str_input)

print "Total Words: %d" % TotalWords
print "Phrase Length: %d" % PhraseLength

# todo: format output better
print WordCount
