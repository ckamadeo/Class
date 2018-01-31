# import helper libraries
import sys

# returns the total number of words in an input phrase
def TotalWords(str_input):
    words = str_input.split()
    return len(words)


def PhraseLength(str_input):
    # Todo: fill in
    return null

def WordCount(str_input):
    # Todo: fill in
    return null


# Get input from the command line
# argv[0] is the name of the script, first input starts at argv[1]
str_input = sys.argv[1]


# main routine
TotalWords = TotalWords(str_input)
print(TotalWords)
