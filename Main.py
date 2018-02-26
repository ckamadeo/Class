# import helper libraries
import sys
import StringProcessor as sp

# Get input from the command line
# argv[0] is the name of the script, first input starts at argv[1]
str_input = sys.argv[1]


# main routine

# todo: preprocess string to remove punctuation
# todo: preprocess string to normalize casing

TotalWords = sp.TotalWords(str_input)
PhraseLength = sp.PhraseLength(str_input)
WordCount = sp.WordCount(str_input)
DistinctWords = sp.DistinctWords(str_input)
DistinctWordCount = sp.DistinctWordCount(str_input)

print "Total Words: %d" % TotalWords
print "Phrase Length: %d" % PhraseLength
print "Number of Distinct Words: %d" % DistinctWordCount

# todo: format output better
print WordCount

# todo: format output better
print DistinctWords
