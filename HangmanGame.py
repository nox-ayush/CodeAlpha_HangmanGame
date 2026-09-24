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
    secret_word = random.choice(WORDS)

    guessed_letters = []
    max_attempts = 6
    wrong_attempts = 0
    print("_" * 200)
    print("""
                                ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗     ██████╗  █████╗ ███╗   ███╗███████╗
                                ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
                                ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║    ██║  ███╗███████║██╔████╔██║█████╗  
                                ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
                                ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
                                ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
""")
    print()
    print("_" * 200)

    while True:
        print("""
Choose Your Difficulty Level

1. Easy   - 3 letters revealed
2. Medium - 2 letters revealed
3. Hard   - 1 letter revealed
4. Exit
""")

        level = input("Enter choice (1, 2, 3 or 4): ").strip()

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

        elif level == "4":
            print("Exiting the game. Goodbye!")
            return

        else:
            print("Invalid selection! Please enter 1, 2, 3 or 4.")

    # Find unique letters
    unique_letters = []

    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters.append(letter)

    # Randomly reveal starting letters
    random.shuffle(unique_letters)

    for i in range(min(reveal_count, len(unique_letters))):
        guessed_letters.append(unique_letters[i])

    print("Initial revealed letters:", guessed_letters)

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

        # Check win
        won = True

        for letter in secret_word:
            if letter not in guessed_letters:
                won = False
                break

        if won:
            print("\nCongratulations!")
            print("You solved the word:", secret_word)
            return

        # Take guess
        guess = input("Guess a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter only one letter.")
            continue

        # Check repeated letter
        if guess in guessed_letters:
            print("You already used this letter.")
            continue

        guessed_letters.append(guess)

        # Check guess
        if guess in secret_word:
            print(f"Correct guess! '{guess}' is present in the word.")
        else:
            wrong_attempts += 1
            print(f"Wrong guess! '{guess}' is not in the word.")

    # Game over
    print("\nGame Over!")
    print("The word was:", secret_word)


# Run the game
while True:
    play_hangman()

    choice = input("\nDo you want to play again? (y/n): ").lower().strip()

    if choice != "y":
        print("Thank you for playing! Goodbye!")
        break

    print("\nStarting a new game...")
