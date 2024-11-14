import random

words = ["Apple", "Peach", "Blueberry", "Strawberry", "Mango", "Durian", "Tomato"]
guessed_letters = []
word = '' # start blank
available_attempts = 5
attempts = 0

def build_word():
    built_word= ''
    return built_word.join(x if x in guessed_letters else '_' for x in word)

def start():
    while True:
        global word
        print("Start!")
        word = random.choice(words).lower() #ensures that guesses are not case sensitive
        print(build_word())

if __name__ == "__main__":
    start()