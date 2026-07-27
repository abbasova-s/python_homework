def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        word = ""
        for character in secret_word:
            if character in guesses:
                word += character
            else:
                word += "_"
        print(word)

        if "_" in word:
            return False
        else:
            return True
    return hangman_closure


game1 = make_hangman(input("Secret word:"))
while True:
    guess = input("Guess a letter: ")

    if game1(guess):
        print("Hooooray!")
        break