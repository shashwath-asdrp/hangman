import random


print("Let's play hangman!")
print("Type only one letter at a time OR type 'help' to see the letters already guessed or 'guess answer' to guess the whole word.")
words = ["hang", "man", "fly", "fruit", "banana", "apple", "frog", "toad", "lion", "deer"]

play_again = "yes"

while play_again == "yes":
    correct = random.choice(words)
    lives = 6
    guess = ""
    used = ""
    
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
        print()
        
        if guessed == "guess answer":
            answer = input("Final guess: ").lower()
            if answer == correct:
                print("Word guessed, you've won!")
                break
            else:
                print("Inccorrect guess, Game over!")
                print("The word was", correct)
                break
        
        if guessed == "help":
            if used == "":
                print("Letters already guessed: None")
                print()
            else:
                print("Letters already guessed:", " ".join(used))
                print()
        
        elif len(guessed) != 1 or not guessed.isalpha():
            print("Not a valid guess. Please enter a single letter.")
        elif guessed in used:
            print("You already guessed that letter!")
        elif guessed in correct:
            guess += guessed
            used += guessed
        else:
            lives = lives - 1
            used += guessed
            print("Letter not found!")
        
    if lives == 0:
        print("Out of lives, Game over!")
        print("The word was", correct)
    
    while True:
        play_again = input("Play again? (yes/no): ").lower()
        if play_again == "yes":
            print()
            print("New game!")
            print()
            break
        elif play_again == "no":
            print()
            print("Thanks for playing!")
            break
        else:
            print("Invalid input.")
