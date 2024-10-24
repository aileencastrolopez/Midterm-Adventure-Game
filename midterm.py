def start_game():
    """Start the game with the initial scenario."""
    print("You wake up in a cold, dark cave...")
    first_choice()

def first_choice():
    """First decision point for the player to choose a path."""
    choice = input("Do you want to go Left (towards the icy abyss) or Right (towards the shimmering light)? ").strip().lower()
    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    else:
        print("Invalid choice. Please enter 'Left' or 'Right'.")
        first_choice()

def left_path():
    """Path when the player chooses to go left."""
    print("You enter the narrow tunnel, and the air becomes frigid...")
    choice = input("Do you want to Rescue someone trapped in the Ice Cavern or Freeze in place? ").strip().lower()
    if choice == 'rescue':
        ending1()
    elif choice == 'freeze':
        ending2()
    else:
        print("Invalid choice. Please enter 'Rescue' or 'Freeze'.")
        left_path()

def right_path():
    """Path when the player chooses to go right."""
    print("You walk into the wider passage, where the light dances around you...")
    choice = input("Do you want to enter the Crystal Chamber or venture into the Luminous Garden? ").strip().lower()
    if choice == 'crystal chamber':
        crystal_chamber()
    elif choice == 'luminous garden':
        luminous_garden()
    else:
        print("Invalid choice. Please enter 'Crystal Chamber' or 'Luminous Garden'.")
        right_path()

def crystal_chamber():
    """Path through the Crystal Chamber."""
    print("In the Crystal Chamber, a majestic guardian stands before you!")
    choice = input("Do you want to Battle the guardian or Flee? ").strip().lower()
    if choice == 'battle':
        ending3()
    elif choice == 'flee':
        ending4()
    else:
        print("Invalid choice. Please enter 'Battle' or 'Flee'.")
        crystal_chamber()

def luminous_garden():
    """Path through the Luminous Garden."""
    print("The Luminous Garden is filled with vibrant colors and intoxicating scents...")
    choice = input("Do you want to Find Treasure hidden in the garden or Lose Yourself in its beauty? ").strip().lower()
    if choice == 'find treasure':
        ending5()
    elif choice == 'lose yourself':
        ending6()
    else:
        print("Invalid choice. Please enter 'Find Treasure' or 'Lose Yourself'.")
        luminous_garden()

def ending1():
    """Ending for rescuing someone in the Ice Cavern."""
    print("You rescue a trapped adventurer who helps you escape with treasure! You win!")
    end_game()

def ending2():
    """Ending for freezing in the Ice Cavern."""
    print("You are frozen in time, becoming part of the icy landscape forever. Game Over.")
    end_game()

def ending3():
    """Ending for battling the guardian in the Crystal Chamber."""
    print("You battle the guardian and emerge victorious, claiming a magical gem! You are a hero!")
    end_game()

def ending4():
    """Ending for fleeing the Crystal Chamber."""
    print("You flee from the guardian, escaping with your life but leaving behind your chance for glory.")
    end_game()

def ending5():
    """Ending for finding treasure in the Luminous Garden."""
    print("You discover a hidden treasure that grants you incredible powers. You are now a legend!")
    end_game()

def ending6():
    """Ending for losing yourself in the beauty of the Luminous Garden."""
    print("You lose yourself in the beauty of the garden, wandering aimlessly into eternity. Game Over.")
    end_game()

def ending7():
    """Ending for making a deal in the Whispering Shadows (optional)."""
    print("You make a deal with a shadowy figure, gaining power at a terrible cost. What will you do with it?")
    end_game()

def ending8():
    """Ending for finding a portal in the Luminous Garden (optional)."""
    print("You find an ancient portal that transports you to a new, unknown world. Adventure awaits!")
    end_game()

def end_game():
    """End the game and thank the player for playing."""
    print("Game Over. Thanks for playing!")

if __name__ == "__main__":
    start_game()