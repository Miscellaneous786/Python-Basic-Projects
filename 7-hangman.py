import random 
def hangman():
    def choose_word():
        words = ["mango","apple","banana","strawberry","peach"]
        word = random.choice(words)
        return word
    def game():
        print(" \nWelcome to the game")
        name = input("Enter your name: ")
        print(f"Let's begin the game {name}")
        guessed_letters = []
        word_chosen = choose_word()
        display = ["_"]*len(word_chosen)
        attempts = 5
        len_word = len(word_chosen)
        print("-------------------------------------------------")
        print(f"    You have to guess a {len_word} letter Fruit name.")
        print("-------------------------------------------------")
        print("You have 5 attempts to guess the word.")
        while attempts > 0:
            print(" ".join(display))
            guessed_letter = (input(f"Guess a letter, {name}: ")).lower()
            if guessed_letter in word_chosen:
                for index, letter in enumerate(word_chosen):
                    if letter == guessed_letter:
                        display[index] = guessed_letter
                        print("Good Choice, It's a letter of the word")
                        if "_" not in display:
                            print(f"Congratulations!\nYou guessed the correct fruit name, {word_chosen}.")
                            return
            if guessed_letter in guessed_letters:
                print("You have guessed this letter before")  
                print("      ")      
            elif guessed_letter not in word_chosen:
                attempts -= 1
                print(f"Incorrect, You have {attempts} left now.")
                print("      ")      
                pass
            if attempts == 0:
                 print(f"Sorry, {name}. You've run out of attempts. \n\nThe word was '{word_chosen}'. \n\nBetter luck next time!")
                 break
    game()
hangman()        