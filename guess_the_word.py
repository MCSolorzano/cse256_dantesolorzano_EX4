# Dante Solorzano
# CIS256 Fall 2024
# EX 3.4(EX 3.4)

import random

class Hangman:
    def __init__(self, testing_pool = None): # Needs a default to prevent crash when not providing for tests
        self.max_attempts = 6
        self.attempts = self.max_attempts
        if (testing_pool != None):
            self.words = testing_pool
        else:
            self.words = ["Apple", "Peach", "Blueberry", "Strawberry", "Mango", "Durian", "Tomato"]
        self.congratulatory_words = ["Nice!", "Awesome,", "Sweet!", "Good job!"] 
        self.word = ''
        self.guessed_letters = set()
        self.won = False
    
    def new(self):
        self.word = random.choice(self.words).lower()
        # self.guessed_letters = set()
        self.attempts = self.max_attempts
        self.won = False
        return self.vanity()
    
    def vanity(self): # meant to be used for the player to see progress of word in terminal
        vanity_word = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                vanity_word = vanity_word + letter
            else:
                vanity_word = vanity_word + '_'
        return vanity_word
    
    def guess(self, letter):
        if letter in self.guessed_letters:
            return "Cannot guess the same letter twice!"
        
        self.guessed_letters.add(letter)
        
        if letter in self.word:
            if set(self.word) <= self.guessed_letters: # a bit of a smart way of using sets to check win status! ONLY supports sets comparing each other.
                self.won = True
                return "Winner! word: " + self.word
            random_celebration = random.choice(self.congratulatory_words)
            return random_celebration + " Correct guess!"
        else:
            self.attempts -= 1
            if self.attempts == 0:
                return f"Match! The word was: '{self.word}'. Better luck next time!"
            return f"Wrong! {self.attempts} attempts left"
    
    def is_over(self):
        return self.won or self.attempts == 0

def play():
    game = Hangman()
    print(game.new()) # generates game and returns vanity for terminal
    
    while not game.is_over():
        print()
        guess = input("Guess a letter, and only a letter: ").strip().lower()
        if len(guess) != 1:
            print("Enter only a single letter!")
            continue
            
        res = game.guess(guess)
        print(res)
        if 'Winner!' in res:
            return
        print("Current word:", game.vanity())

if __name__ == "__main__":
    play()