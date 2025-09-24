import random

def number_guesser():
    """
    This function implements a number guessing game where the AI tries to guess a number
    chosen by the user using a binary search algorithm.
    """
    print("Welcome to the Number Guessing AI!")
    print("Think of a number between 1 and 100, and I will try to guess it.")
    print("After each guess, tell me if my guess was too high (h), too low (l), or correct (c).")

    low = 1
    high = 100
    feedback = ''

    while feedback != 'c':
        if low > high:
            print("Something went wrong! You might have given me incorrect feedback.")
            return

        # Classic binary search guess
        guess = (low + high) // 2
        
        feedback = input(f"Is your number {guess}? (h/l/c): ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Great! I guessed your number, which was {guess}.")

if __name__ == "__main__":
    number_guesser()