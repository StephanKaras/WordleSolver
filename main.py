from lib2to3.pgen2 import grammar
import random
from types import GeneratorType

class WordleSolver:

    def __init__(self, wordsList, grayLetters, greenLetters, orangeLetters):
        self.wordsList = []
        self.grayLetters = []
        self.greenLetters = ['','','','','']
        self.orangeLetters = ['','','','','']
    
    def run(self):
        self.copyWordsToList()

        stillSearching = True
        print("Input ", "\"", self.randomWord(),"\"", " in Wordle.", sep="")
        while stillSearching:
            print(len(self.wordsList), "words remaining.")
            # dealing with gray letters
            gray = input("Enter gray letters without spaces. (if none, type 0): ")
            if gray != '0':
                self.grayLetters = list(gray)

                

            # dealing with green letters
            green = input('Enter green letters. "-" for anything else: ')
            if green != "0":
                for index, letter in enumerate(green):
                    if letter != '-':
                        self.greenLetters[index] = letter

            # dealing with orange letters
            orange = input('Enter orange letters. "-" for anything else: ')
            if orange != "0":
                self.orangeLetters = list(orange)
            
            self.removeWrongWords()

            # checking if goal state is reached
            '''if "-" in self.greenLetters:
                found = False
                #recommend word from current list
                print("Input ", "\"", self.randomWord(),"\"", " in Wordle.", sep="")
            else:
                found = True'''
            if "" not in self.greenLetters and "-" not in self.greenLetters:
                stillSearching = False
            print("Input ", "\"", self.randomWord(),"\"", " in Wordle.", sep="")

    def copyWordsToList(self):
        with open("words") as words:
            for i, line in enumerate(words):
                self.wordsList.append(line.strip())
    
    def randomWord(self):
        randomInt = random.randint(0, len(self.wordsList) - 1)
        print(randomInt)
        return self.wordsList[randomInt]

    def removeWrongWords(self):
        # Removing all words that contain gray
        if len(self.grayLetters) >= 0:
            wordsListC2 = self.wordsList.copy()
            for word in wordsListC2:
                for grayLetter in self.grayLetters:
                    if grayLetter in word:
                        if word in self.wordsList:
                            self.wordsList.remove(word)
            self.grayLetters.clear()

        # Removing words without green & with green in the wrong index
        wordsListC1 = self.wordsList.copy()
        for index, letter in enumerate(self.greenLetters):
            if letter != "-" and letter != '':
                for word in wordsListC1:
                    if word[index:index+1] != letter:
                        if word in self.wordsList:
                            self.wordsList.remove(word)
        
        # Removing words with letters in wrong index
        if len(self.orangeLetters) >= 0:
            wordsListC3 = self.wordsList.copy()
            for index, letter in enumerate(self.orangeLetters):
                if letter != "-" and letter != '':
                    for word in wordsListC3:
                        if word[index:index+1] == letter:
                            if word in self.wordsList:
                                self.wordsList.remove(word)
                        
                        if letter not in word:
                            if word in self.wordsList:
                                self.wordsList.remove(word)
            self.orangeLetters.clear()
            self.orangeLetters = ['','','','','']


words = []
greenL = ["", "", "", "", ""]
grayL = [""]
orangeL = []

solver = WordleSolver(words, grayL, greenL, orangeL)
solver.run()
