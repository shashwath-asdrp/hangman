print("Let's play hangman!")
words = ["hang", "man", "fly", "fruit", "banana", "apple", "frog", "toad", "lion", "deer"]
n = 0
lives = 6
correct = words[n]
guess = ""
while lives > 0:
    guessed = input("Guess a letter: ").lower()
    if guessed in correct:
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
        break
if lives == 0:
    print("Game over! The word was", correct)