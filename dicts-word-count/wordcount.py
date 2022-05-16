"""Count words in file."""

import sys

def count_words(filename):


    filename = open(sys.argv[2])

    word_count = {}

#tokenize
    for line in open(filename):

        line = line.rstrip()
        words = line.split(" ")

#count words
        for word in words:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
        

    filename.close()

#print count words
    for word in word_count:
        print(word, word_count[word])



count_words(filename)