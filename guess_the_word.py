import random

words = ["Apple", "Peach", "Blueberry", "Strawberry", "Mango", "Durian", "Tomato"]
guessed_letters = []
word = random.choice(words).lower() #ensures that guesses are not case sensitive
available_attempts = 5 
attempts = 0

def build_word():
    built_word= ''
    return built_word.join(x if x in guessed_letters else '_' for x in word)


def start():
    global attempts
    print("Start!")
    while True:
        if (available_attempts != attempts):
            built_word = build_word()
            print(built_word)
            if ("_" in built_word):
                print("Guesses remaining: " + str(available_attempts - attempts))
                user_letter = input("Make a guess! Please only insert a letter: ").lower()
                if (len(user_letter) == 1):
                    attempts += 1
                    guessed_letters.append(user_letter)
                    
                    print('wa')
                else:
                    print('Please only insert a letter!')
            else:
                print("You win!")
        else:
            print("You lost!")
            break


if __name__ == "__main__":
    start()