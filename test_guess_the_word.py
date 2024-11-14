# Dante Solorzano
# CIS256 Fall 2024
# EX 3.4(EX 3.4)

from guess_the_word import Hangman

# I've never used a testing library before, so this is a basic implementation.

testing_pool = ["foobar"]

def test_guess_correct():
    game = Hangman(testing_pool)
    game.new()
    res = game.guess('b')
    assert "Correct guess!" in res
    assert game.vanity().count('b') == 1

def test_guess_wrong():
    game = Hangman(testing_pool)
    game.new()
    res = game.guess('2') # using a number since that is gaurenteed VERY wrong
    assert "Wrong!" in res