import random
while True:
    user_action = input("Enter your choice(rock,paper,scissor): ")
    possible_action = ["rock","paper","scissor"]
    comp_action = random.choice(possible_action)
    print(f"\nYou choose {user_action} and computer choose {comp_action}.\n")
    if user_action == comp_action:
        print("Both choose {user_action}.So it's a tie!")
    elif user_action == "rock":
        if comp_action == "paper":
            print("Paper covers rock.You lose!")
        else:
            print("Rock smashes scissor.You win!")
    elif user_action == "paper":
        if comp_action == "rock":
            print("Paper covers rock.You win!")
        else:
            print("Scissor cuts paper.You lose!")
    elif user_action == "scissor":
        if comp_action == "rock":
            print("Rock smashes scissor.You lose!")
        else:
            print("Scissor cuts paper.You win!")
    play_again = input("play again? (y/n): ")
    if play_again.lower() == "n":
        break

