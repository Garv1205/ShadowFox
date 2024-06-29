print("Hangman Word Guesser Game")
import random
# List of words
word_list = ["apple", "banana", "orange"]

# Choose a random word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Game state variables
end_of_game = False
lives = 6
display = ["_"] * word_length

# Hint state variables
hint_limit = 2
hints_used = 0

#print(logo)

while not end_of_game:
    use_hint = input("Do you want to use a hint? (yes/no): ").lower()
    
    if use_hint == "yes":
        if hints_used < hint_limit:
            hints_used += 1
            for i, letter in enumerate(chosen_word):
                if display[i] == "_":
                    display[i] = letter
                    print(f"Hint: One of the letters is '{letter}'")
                    break
        else:
            print("You've used all your hints.")
    
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was '{chosen_word}'.")

    print(' '.join(display))

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(f"{lives} lives are left. You have {hint_limit - hints_used} hints left.")