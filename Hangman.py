import random

#display game instructions
print("Let's play hangman!")
print("Type only one letter at a time OR type 'help' to see the letters already guessed or 'guess answer' to guess the whole word.")
#list of words
words = ["hang", "man", "fly", "fruit", "banana", "apple", "frog", "toad", "lion", "deer"]

play_again = "yes"

#keeps playing until "no"
while play_again == "yes":
    
    #randomly selects a word and sets starting number of lives
    correct = random.choice(words)
    lives = 6
    #stores correctly guessed letters and all the all guessed letters
    guess = ""
    used = ""
    
    #keep playing while player still has lives
    while lives > 0:
        #creates word display
        display = ""
        for letter in correct:
            if letter in guess:
                display += letter + " "
            else:
                display += "_ "
        
        print(display.strip())
        
        #checks if the player has won
        if "_" not in display:
            print("Word guessed, you've won!")
            break
    
        #displays number of lives left
        print("Lives left:", lives)
        
        #asks player for letter input
        guessed = input("Guess a letter: ").lower()
        print()
        
        #additional input option to guess whole word
        if guessed == "guess answer":
            answer = input("Final guess: ").lower()
            if answer == correct:
                print("Word guessed, you've won!")
                break
            else:
                print("Inccorrect guess, Game over!")
                print("The word was", correct)
                break
        
        #additional input option to display all previously guessed letters
        if guessed == "help":
            if used == "":
                print("Letters already guessed: None")
                print()
            else:
                print("Letters already guessed:", " ".join(used))
                print()
        
        #checks the input is only one letter, if not, repeats loop and asks for input again
        elif len(guessed) != 1 or not guessed.isalpha():
            print("Not a valid guess. Please enter a single letter.")
        elif guessed in used:
            print("You already guessed that letter!")
        elif guessed in correct:
            #checks if guess is correct
            guess += guessed
            used += guessed
        else:
            #removes one life if wrong guess
            lives = lives - 1
            used += guessed
            print("Letter not found!")
    
    #displays game over if player has run out of lives    
    if lives == 0:
        print("Out of lives, Game over!")
        print("The word was", correct)
    
    #asks player if they want to play another round
    while True:
        play_again = input("Play again? (yes/no): ").lower()
        #start new game only when player enters "yes"
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
            #asks again if invalid input
            print("Invalid input.")
