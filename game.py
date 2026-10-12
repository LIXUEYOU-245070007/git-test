import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            # Get user input
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess (1-100): "))
            
            # Validate input range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
                
            attempts += 1
            
            # Check the guess
            if guess == target_number:
                print(f"🎉 Congratulations! You guessed the number {target_number} in {attempts} attempts!")
                return True
            elif guess < target_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
                
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
            continue
    
    # If all attempts are used
    print(f"\n😔 Game Over! The number was {target_number}.")
    return False

def main():
    while True:
        number_guessing_game()
        
        # Ask if user wants to play again
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()