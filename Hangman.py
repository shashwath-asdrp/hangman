print("Let's play hangman!")
words = ["hang", "man", "fly", "fruit", "banana", "apple", "frog", "toad", "lion", "deer"]
n = 0

while n < len(words):
    lives = len(words[n]) + 1
    correct = words[n]
    guess = ""
    
    while lives > 0:
        guessed = input("Guess a letter: ").lower()
        if len(guessed) != 1 or not guessed.isalpha():
            print("Enter a single letter")
        elif guessed in correct:
            guess += guessed
            print("Good guess!")
        else:
            lives = lives - 1
            print("Wrong guess!")
            
        display = ""
        for letter in correct:
            if letter in guess:
                display += letter + " "
            else:
                display += "_ "
        print(display.strip())
        print("Lives left:", lives)
        
        if "_" not in display:
            print("You won!")
            n = n + 1
            break
            
    if lives == 0:
        print("Out of lives, Game over! The word was", correct)
        n = n + 1  # Move to next word if they choose to play again

    # Ask to play again after each word finishes
    while True:
        play_again = input("Play again? (yes/no): ").lower()
        if play_again == "yes":
            print("New game!")
            break
        elif play_again == "no":
            print("Exiting program.")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
