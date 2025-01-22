from telljoke_function import tell_joke
joke_list=[{"type": "robbers", "setup": "Knock Knock", "punchline": "Calder police - I've been robbed!"},
{"type": "tanks", "setup": "Knock Knock", "punchline": "Tank you!"},
{"type": "pencils", "setup": "Knock Knock", "punchline": "Nevermind, it's pointless!"}
]
def game():
    """
    Main function to handle the joke-telling game.
    """
    question = input("Do you want to hear a joke? (yes/no): ").strip().lower()  # Ask the user if they want to play
    if question == "no":
        print("Okay, suit yourself!")  # Exit if the user doesn't want to play
        return
    elif question != "yes": # does not equal yes 
        print("Invalid input. Exiting game.")  # Handle invalid inputs
        return

    # Start the game loop
    while question == "yes": # if the user does want to play 
        print("Here are your joke options:")
        print([joke["type"] for joke in joke_list])  # Display available joke types (shows all of the jokes in the list in form of a list)
       
        # Get the user's choice
        choice = input("Select the type of joke you want to hear: ").strip().lower()
       
        # Call the function with the user's choice and the list of jokes
        tell_joke(choice, joke_list)
       
        # Ask if the user wants another joke
        question = input("Do you want to hear another joke? (yes/no): ").strip().lower()

    # Game ending
    if question == "no":
        review = int(input("Please rate our game from 1-10: "))  # Ask for user rating
        score = review * 10  # Convert rating to percentage
        print(f"{score}% satisfaction rate.")
       
        # Ask if they would recommend the game
        friend = input("Would you recommend this game to a friend? (yes/no): ").strip().lower()
        if friend == "yes":
            print("Thanks, we appreciate it!")
        else:
            print("Sorry you didn't enjoy it.")