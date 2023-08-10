import random

def choose_word():
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    return random.choice(words)

def play_hangman():
    word = choose_word()
    guessed_letters = []
    tries = 6

    while tries > 0:
        # Display the current state of the word with blanks for unguessed letters
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("Current word:", display_word)

        # Prompt the player for a letter
        guess = input("Enter a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add the guessed letter to the list
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print("Correct guess!")
        else:
            print("Incorrect guess!")
            tries -= 1

        # Check if the player has guessed all the letters
        if set(word) == set(guessed_letters):
            print("Congratulations! You guessed the word:", word)
            break

    if tries == 0:
        print("You ran out of tries. The word was:", word)
        
# Start the game
play_hangman()
