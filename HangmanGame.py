import random

def play_hangman():
    # Predefined list of words
    words = ["developer", "programming", "technology", "keyboard", "algorithm"]
    secret_word = random.choice(words)

    guessed_letters = []
    max_attempts = 6
    wrong_attempts = 0

    print("=== Welcome to Hangman Game! ===")

    # Difficulty selection loop
    while True:
        print("\nChoose difficulty level:")
        print("1. Easy (3 letters revealed)")
        print("2. Medium (2 letters revealed)")
        print("3. Hard (1 letter revealed)")

        level = input("Enter choice (1, 2, or 3): ").strip()

        if level == "1":
            reveal_count = 3
            print("You chose Easy mode!")
            break
        elif level == "2":
            reveal_count = 2
            print("You chose Medium mode!")
            break
        elif level == "3":
            reveal_count = 1
            print("You chose Hard mode!")
            break
        else:
            print("Invalid selection! Please enter 1, 2, or 3.")

    # Find unique letters in the secret word manually
    unique_letters = []
    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters.append(letter)

    # Shuffle unique letters to pick hints randomly
    random.shuffle(unique_letters)
    for i in range(reveal_count):
        if i < len(unique_letters):
            guessed_letters.append(unique_letters[i])

    print("Initial revealed letters:", guessed_letters)

    # Main game loop
    while wrong_attempts < max_attempts:
        # Build the hidden word presentation
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word.strip())
        print("Remaining attempts:", max_attempts - wrong_attempts)

        # Check if the player has uncovered every letter
        won = True
        for letter in secret_word:
            if letter not in guessed_letters:
                won = False
                break

        if won:
            print("\nCongratulations! You solved the word:", secret_word)
            break

        # Receive player guess
        guess = input("Guess a letter: ").lower().strip()

        # Validate input format
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("You have already used this letter. Try another one.")
            continue

        guessed_letters.append(guess)

        # Evaluate the guess
        if guess in secret_word:
            print(f"Correct guess! '{guess}' is present in the word.")
        else:
            wrong_attempts += 1
            print(f"Wrong guess! '{guess}' is not in the word.")

    # Check for loss condition
    if wrong_attempts == max_attempts:
        print(f"\nGame Over! You ran out of attempts. The word was: {secret_word}")

# Run the program directly
play_hangman()