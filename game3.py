import time

def introduction():
    print("Welcome to the Space Station Adventure!")
    print("You wake up in a futuristic space station with no memory.")
    print("Your mission is to explore the space station and uncover the truth.")
    print("Choose wisely, as your decisions will shape the outcome!")

def make_choice(choices):
    print("\nChoose your action:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def explore_space_station():
    print("\nYou start exploring the space station.")
    time.sleep(1)
    print("As you walk down the corridor, you encounter an alien creature!")
    choices = ["Attempt to communicate", "Hide and observe", "Attack"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nThe alien seems friendly and guides you to a control room.")
        hacking_puzzle()
    elif choice == 2:
        print("\nYou hide and observe the alien. It leaves peacefully.")
        continue_exploration()
    else:
        print("\nYou attack the alien, but it retaliates. The fight is tough.")
        print("You barely escape, wounded. Game Over.")

def hacking_puzzle():
    print("\nIn the control room, you find a terminal with a hacking puzzle.")
    print("Solve the puzzle to gain access to the station's mainframe.")
    
    # Simulating a simple hacking puzzle (in reality, it could be more complex)
    correct_code = "1234"
    player_code = input("Enter the 4-digit code: ")

    if player_code == correct_code:
        print("\nCongratulations! You successfully hacked into the mainframe.")
        continue_exploration()
    else:
        print("\nIncorrect code. Security alarms are triggered!")
        print("You must find an escape route quickly.")
        escape_choice = make_choice(["Search for escape route", "Confront security personnel"])

        if escape_choice == 1:
            print("\nYou find a hidden passage and escape the security personnel.")
            continue_exploration()
        else:
            print("\nYou confront security personnel, but they overpower you. Game Over.")

def continue_exploration():
    print("\nYou continue exploring the space station.")
    time.sleep(1)
    print("You come across a room with advanced technology.")
    choices = ["Inspect technology", "Proceed cautiously", "Bypass the room"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou inspect the technology and find an advanced weapon.")
        inventory.append("Advanced Weapon")
        continue_exploration()
    elif choice == 2:
        print("\nYou proceed cautiously and avoid triggering security measures.")
        continue_exploration()
    else:
        print("\nYou decide to bypass the room, but an alarm goes off.")
        print("Security personnel are on high alert. You need to act quickly.")
        security_choice = make_choice(["Hide in a vent", "Try to talk your way out"])

        if security_choice == 1:
            print("\nYou hide in a vent until security personnel pass by.")
            continue_exploration()
        else:
            print("\nYou try to talk your way out, but security remains suspicious.")
            print("They detain you for questioning. Game Over.")

def conclusion():
    print("\nCongratulations! You have successfully navigated through the space station.")
    print("You uncover a secret about your identity and the purpose of the space station.")
    print("The truth sets you free, and you escape to a new adventure!")

# Game initialization
inventory = []
introduction()

# Start the game
explore_space_station()
conclusion()
