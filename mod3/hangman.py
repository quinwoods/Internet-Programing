word_to_guess = ["F","O","X"]
word_guessed = ["","",""]


def guess_letter(letter):
    try:
        return word_to_guess.index(letter)
    except ValueError:
        print("Thats not in the list! Try again...")
        return -1

while True:
    letter_guessed = input("Guess a Letter: ")
    print("The letter you guessed is " + letter_guessed)
    if(guess_letter(letter_guessed) != -1):
        print("holy shit")
        word_guessed[guess_letter(letter_guessed)] = letter_guessed
    print("Your Guessed Letters are ", word_guessed)


