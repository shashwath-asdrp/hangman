import random


print("Let's play hangman!")
words = ["hang", "man", "fly", "fruit", "banana", "apple", "frog", "toad", "lion", "deer"]


lives = 6
correct = random.choice(words)
guess = ""


while lives > 0:
    display = ""
    for letter in correct:
        if letter in guess:
            display += letter + " "
        else:
            display += "_ "
    
    print(display.strip())
    
    if "_" not in display:
        print("Word guessed, you've won!")
        break


    print("Lives left:", lives)
    
    guessed = input("Guess a letter: ").lower()
    print("")
    
    if len(guessed) != 1 or not guessed.isalpha():
        print("Not a valid guess. Please enter a single letter.")
    elif guessed in guess:
        print("You already guessed that letter!")
    elif guessed in correct:
        guess += guessed
    else:
        lives = lives - 1
        print("Letter not found!")


    
    if lives == 0:
        print("Out of lives, Game over! The word was", correct)
        break