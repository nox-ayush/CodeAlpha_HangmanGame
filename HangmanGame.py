import random

WORDS = [
    "adventure", "beautiful", "breakfast", "chocolate", "watermelon",
    "strawberry", "pineapple", "restaurant", "conversation", "friendship",
    "celebration", "comfortable", "interesting", "experience", "education",
    "knowledge", "information", "newspaper", "television", "photograph",
    "something", "everything", "everywhere", "afternoon", "environment",
    "neighborhood", "community", "government", "university", "classroom",
    "playground", "basketball", "skateboard", "motorcycle", "transportation",
    "destination", "communication", "entertainment", "relationship", "responsibility",
    "opportunity", "imagination", "creativity", "motivation", "confidence",
    "happiness", "kindness", "successful", "wonderful", "excellent",
    "different", "traditional", "necessary", "available", "responsible",
    "surprising", "permission", "attention", "understanding", "remembering",
    "experience", "celebration", "photography", "conversation", "discussion",
    "management", "leadership", "department", "foundation", "collection",
    "generation", "atmosphere", "investment", "reputation", "discipline",
    "population", "conclusion", "instrument", "wilderness", "transition",
    "innovation", "appearance", "efficiency", "importance", "journalism",
    "psychology", "publishing", "accounting", "curriculum", "hypothesis",
    "laboratory", "manuscript", "technology", "programmer", "javascript",
    "frameworks", "algorithms", "dictionary", "expression", "whitespace",
    "resolution", "connection", "navigation", "production", "government",
    "university", "department", "foundation", "collection", "generation",
    "television", "investment", "reputation", "population", "permission",
    "basketball", "skateboard", "restaurant", "reflection", "recreation",
    "enthusiasm", "creativity", "excellence", "innovation", "efficiency",
    "experience", "journalism", "psychology", "publishing", "accounting",
    "curriculum", "laboratory", "manuscript", "architecture", "application",
    "authentication", "authorization", "vulnerability", "virtualization",
    "configuration", "implementation", "documentation", "optimization",
    "intelligence", "development", "cyberattack", "cybercrime", "blockchain",
    "decryption", "encryption", "administrator", "infrastructure", "microprocessor",
    "troubleshooting", "programming", "cryptography", "networking", "database",
    "adventure", "background", "basketball", "collection", "commercial",
    "connection", "construction", "decoration", "direction", "discovery",
    "discussion", "education", "electricity", "employment", "entertainment",
    "equipment", "examination", "excitement", "explanation", "expression",
    "friendship", "generation", "government", "improvement", "independence",
    "individual", "information", "instruction", "introduction", "invitation",
    "knowledge", "landscape", "lifestyle", "literature", "management",
    "membership", "movement", "neighborhood", "newspaper", "opportunity",
    "organization", "permission", "personality", "population", "preparation",
    "presentation", "production", "profession", "relationship", "requirement",
    "reservation", "restaurant", "responsibility", "satisfaction", "schoolwork",
    "technology", "temperature", "transportation", "understanding", "university",
    "vacation", "vegetables", "watermelon", "weather", "workplace",
    "celebration", "certificate", "childhood", "classroom", "confidence",
    "conversation", "creativity", "curiosity", "decision", "determination",
    "development", "difference", "difficulty", "direction", "disappointment",
    "encouragement", "environment", "expectation", "experience", "friendship",
    "happiness", "imagination", "importance", "improvement", "inspiration",
    "intelligence", "knowledge", "motivation", "opportunity", "patience",
    "personality", "possibility", "preparation", "progress", "relationship",
    "successfully", "surprise", "thoughtful", "tradition", "understanding",
    "wonderful", "achievement", "agreement", "announcement", "appointment",
    "application", "attraction", "beautiful", "behaviour", "businessman",
    "celebration", "challenge", "character", "comfortable", "competition",
    "complaint", "concentration", "confusion", "connection", "conversation",
    "cooperation", "description", "determination", "disagreement", "discovery",
    "discussion", "encouragement", "explanation", "expression", "favourite",
    "friendship", "generosity", "gratitude", "importance", "imagination",
    "improvement", "independent", "information", "introduction", "knowledge",
    "leadership", "laughter", "membership", "neighborhood", "organization",
    "performance", "personality", "possibility", "preparation", "protection",
    "recommendation", "relationship", "responsibility", "satisfaction", "selection",
    "situation", "something", "statement", "successful", "suggestion",
    "television", "transportation", "understanding", "university", "vegetarian",
    "admission", "advertisement", "agreement", "appointment", "arrangement",
    "assistance", "attention", "atmosphere", "available", "celebration",
    "certificate", "communication", "comparison", "competition", "conclusion",
    "condition", "connection", "consideration", "construction", "consultation",
    "contribution", "conversation", "cooperation", "coordination", "decoration",
    "delivery", "department", "description", "development", "difference",
    "direction", "education", "electricity", "employment", "environment",
    "equipment", "examination", "explanation", "government", "identification",
    "imagination", "implementation", "improvement", "installation", "instruction",
    "interaction", "introduction", "invitation", "management", "manufacturing",
    "organization", "participation", "permission", "preparation", "presentation",
    "production", "professional", "recommendation", "registration", "relationship",
    "requirement", "responsibility", "transportation", "verification", "volunteer"
]


def play_hangman():
    secret_word = random.choice(WORDS).lower()
    guessed_letters = []
    max_attempts = 6
    wrong_attempts = 0

    print("=" * 115)
    print(r"""
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗     ██████╗  █████╗ ███╗   ███╗███████╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║    ██║  ███╗███████║██╔████╔██║█████╗  
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
""")
    print("=" * 115)
    print("=== Welcome to Hangman Game! ===")

    # Difficulty selection loop
    while True:
        print("\nChoose difficulty level:")
        print("1. Easy   (2 letters revealed)")
        print("2. Medium (1 letter revealed)")
        print("3. Hard   (0 letters revealed)")
        print("4. Exit")

        level = input("Enter choice (1, 2, 3 or 4): ").strip()

        if level == "1":
            reveal_count = 2
            print("You chose Easy mode!")
            break

        elif level == "2":
            reveal_count = 1
            print("You chose Medium mode!")
            break

        elif level == "3":
            reveal_count = 0
            print("You chose Hard mode!")
            break
        elif level == "4":
            print("Exiting the game. Goodbye!")
            return False
        else:
            print("Invalid selection! Please enter 1, 2, 3 or 4.")
            print("Invalid selection! Please enter 1, 2, 3 or 4.")

    # Find unique letters manually using loop
    unique_letters = []

    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters.append(letter)

    # Randomly reveal letters based on difficulty
    random.shuffle(unique_letters)
    for i in range(min(reveal_count, len(unique_letters))):
        guessed_letters.append(unique_letters[i])

    if len(guessed_letters) > 0:
        print("Initial revealed letters:", guessed_letters)
    else:
        print("No hint letters revealed for this level!")

    # Main game loop
    while wrong_attempts < max_attempts:
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word.strip())
        print("Remaining attempts:", max_attempts - wrong_attempts)

        # Check win condition manually
        won = True

        for letter in secret_word:
            if letter not in guessed_letters:
                won = False
                break

        if won:
            print("\n Congratulations! You solved the word:", secret_word)
            return True

        # Take user guess
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter only one letter.")
            continue

        # Check repeated letter
        if guess in guessed_letters:
            print("You already used this letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Correct guess! '{guess}' is present in the word.")
        else:
            wrong_attempts += 1
            print(f"Wrong guess! '{guess}' is not in the word.")

    # Loss condition
    if wrong_attempts == max_attempts:
        print("\n Game Over! You ran out of attempts.")
        print("The correct word was:", secret_word)

    return True


# Run the game loop
while True:
    should_continue = play_hangman()
    if not should_continue:
        break

    choice = input("\nDo you want to play again? (y/n): ").lower().strip()
    if choice != "y":
        print("Thank you for playing! Goodbye!")
        break