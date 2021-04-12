'''
3.	Modify the sentence-generator program of Case Study 5.3 so that it
    inputs its vocabulary from a set of text files at startup.
    The filenames are nouns.txt, verbs.txt, articles.txt, and prepositions.txt.
    (Hint: Define a single new function, getWords. This function should expect a
    filename as an argument. The function should open an input file with this name,
    define a temporary list, read words from the file, and add them to the list.
    The function should then convert the list to a tuple and return this tuple.
    Call the function with an actual filename to ini- tialize each of the four
    variables for the vocabulary.)

'''
import random


def getWords(nameFile):
    try:
        reader = open(nameFile+".txt", "r")
        file_content = reader.readlines()
        return tuple(file_content)
        # Further file processing goes here
    except:
        return False


def getRandomWord(nameFile):
    # to use rstrip() to remove line breaks
    tupleWords = getWords(nameFile)
    return random.choice(tupleWords).rstrip()


def sentence():
    return nounPhrase() + " " + verbPhrase()


def nounPhrase():
    return getRandomWord('articles') + " " + getRandomWord('nouns')


def verbPhrase():
    return getRandomWord('verbs') + " " + nounPhrase() + " " + prepositionalPhrase()


def prepositionalPhrase():
    return getRandomWord('prepositions') + " " + nounPhrase()


def main():
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())


main()
