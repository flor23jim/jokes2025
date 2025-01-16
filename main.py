# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes
# joke = input("Do you want to hear a joke? ")

# if joke == "no":
#     print("Okay suit yourself!")
# while joke == "yes":
#     print("Great, Let's Play")
#     question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#     if question == "robbers":
#         input("Knock Knock ")
#         input("Calder")
#         print("Calder police - I've been robbed!")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "tanks":
#         input("Knock Knock ")
#         input("Tank ")
#         input("You are welcome! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "pencils":
#         input("Knock Knock ")
#         input("Broken pencil ")
#         input("Nevermind, it's pointless! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
# if joke == "finished":
#     rate = int(input("Please rate our game 1-10! "))
#     final_score = int(rate * 10)
#     print(str(final_score) + " percent satisfaction rate")
#     friend = input("Would you recommend this game to a friend? ")

#     if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it. ")
#     else:
#         print("Sorry you did not enjoy it. ")
###########################################################################################
typej=['robbers','tanks',' or pencils'] # sequence/task stats with a list of jokes for the user to chose from 

def tell_joke(joke): # defines the argument and parameter
    if joke =='robbers':# Utilize selection :if the joke chosen is robbers the following outputs will be given to the user waiting for there input
        input("Knock Knock ")
        input("Calder")
        print("Calder police - I've been robbed!")# by printing out the last function of the joke the user can either chose to end the jokes or continue on with another joke. Because previouse code had an input statement the user would have to insert something to continue the code. 

    elif joke== 'tanks':# if the joke chosen is tanks the following outputs will be given to the user waiting for there input
        input("Knock Knock ")
        input("Tank ")
        print("tank you ") # ends function for the code #output

    elif joke=='pencil':# if the joke chosen is pencile the following outputs will be given to the user waiting for there input
        input("Knock Knock ")
        input("Broken pencil ")
        print("Nevermind, it's pointless! ")# ends function for code #output
    else:#Utilize selection
        print('you have enter an invalid choice, please choose a joke from the list')#output
def game():
    question = input("Do you want to hear a joke? (yes/no) ").lower() # lowercases everything the user proviedes
    if question == "no": # Utilize selection :if no is selected game ends and will print out "ok suit yourself"
        print("Okay, suit yourself!")#output
        return
    elif question == "yes": # will depend on output given from the user
        print("Great, let's play!")#output
    else:#Utilize selection
        print("Invalid input. Exiting game.") # output
        return
    while question == "yes":# depends on user output
        print("Here are your joke options:") # output 
        print(f'{typej}')
        choice=(input("Select the joke you want to hear: "))    # asks user what joke they want to hear
        if choice.lower() in [option.lower() for option in typej]:  # Validate the input
            tell_joke(choice)  # Call the function to tell the joke
        else:
            # Handle invalid input
            print("Invalid choice. Please select a joke from the list.")

    question= input("Do you want to hear another joke? (yes/no) ").lower()
    
    if question == "no":#Utilize selection
        review = int(input("Please rate our game from 1-10: "))
        score = review * 10 # put the users output into a percentage 
        print(f"{score}% satisfaction rate.") # varies with user output,but print out score from 1-10 into a % 
    friend = input("Would you recommend this game to a friend? (yes/no) ").lower()
    if friend =="yes":#Utilize selection
        print("Thanks, we appreciate it!")
    else:#Utilize selection
      print("Sorry you didn't enjoy it.")
game()