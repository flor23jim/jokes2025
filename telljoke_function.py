
joke_list=[{"type": "robbers", "setup": "Knock Knock", "punchline": "Calder police - I've been robbed!"},
{"type": "tanks", "setup": "Knock Knock", "punchline": "Tank you!"},
{"type": "pencils", "setup": "Knock Knock", "punchline": "Nevermind, it's pointless!"}
]

def tell_joke(choice, jokes):
    """
    Tells a knock-knock joke based on the user's choice.
    Parameters:
        - choice (str): The type of joke chosen by the user.
        - jokes (list): A list of jokes, each as a dictionary with 'type', 'setup', and 'punchline'.
    """
    for joke in jokes:  # Iterating through the list of jokes
        if joke["type"] == choice:  # Selection statement to match the user's choice
            input(joke["setup"])  # First part of the joke
            input(joke["type"].capitalize())  # Second part of the joke
            print(joke["punchline"])  # Deliver the punchline
            return  # Exit the function after delivering the joke
    # If no matching joke is found
    print("Invalid choice. Please select a valid joke type.")