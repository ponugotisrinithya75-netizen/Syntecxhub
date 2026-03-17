import random

def choose_difficulty():
    print("\nSelect Difficulty Level")
    print("1. Easy (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard (1 - 200)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        return 50
    elif choice == "2":
        return 100
    elif choice == "3":
        return 200
    else:
        print("Invalid choice. Defaulting to Medium.")
        return 100


def play_game():
    max_range = choose_difficulty()
    number = random.randint(1, max_range)
    attempts = 0

    print(f"\nI have selected a number between 1 and {max_range}. Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try a higher number.")
            elif guess > number:
                print("Too high! Try a lower number.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                return attempts

        except ValueError:
            print("Please enter a valid number.")


def main():
    best_score = None

    while True:
        attempts = play_game()

        if best_score is None or attempts < best_score:
            best_score = attempts
            print("🏆 New Best Score!")

        print(f"Best (lowest) attempts so far: {best_score}")

        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()