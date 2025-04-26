import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the images
def load_images():
    """Load the images for rock, paper, and scissors."""
    images = {
        0: mpimg.imread('rock.png'),
        1: mpimg.imread('paper.png'),
        2: mpimg.imread('scissors.png')
    }
    return images

def get_computer_choice():
    """Randomly select between 0 (rock), 1 (paper), or 2 (scissors) for the computer."""
    return random.choice([0, 1, 2])

def get_user_choice():
    """Prompt the user to enter their choice: 0 (rock), 1 (paper), or 2 (scissors)."""
    try:
        user_input = int(input("Enter your choice (0 for Rock, 1 for Paper, 2 for Scissors): "))
        if user_input not in [0, 1, 2]:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please choose again.")
        return get_user_choice()
    return user_input

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's and computer's choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 1 and computer_choice == 0):
        return "You win!"
    else:
        return "Computer wins!"

def display_choices(user_choice, computer_choice, images):
    """Display the images of the user's and computer's choices."""
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    
    # Display user choice
    axes[0].imshow(images[user_choice])
    axes[0].set_title("Your Choice")
    axes[0].axis('off')  # Hide the axes

    # Display computer choice
    axes[1].imshow(images[computer_choice])
    axes[1].set_title("Computer's Choice")
    axes[1].axis('off')  # Hide the axes

    plt.show()

def play_game():
    """Play a single round of Rock, Paper, Scissors."""
    images = load_images()
    
    print("Welcome to Rock, Paper, Scissors game1!")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    display_choices(user_choice, computer_choice, images)
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()

