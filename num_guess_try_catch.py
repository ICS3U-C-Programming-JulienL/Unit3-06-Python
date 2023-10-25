#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: October 25, 2023
# This program is a random number guessing game for a whole number between 0 and 9
import random


def main():
    # get the user guess and set the answer to a random number
    print(
        "In this game, a correct integer has been randomly chosen from 0 to 9. Try to guess the correct integer."
    )
    random_answer = random.randint(0, 9)
    user_guess_string = input("What is your guess for the correct integer: ")

    try:
        # convert user guess to an integer
        user_guess_int = int(user_guess_string)

        # if the user gets the number right, tell them they were right
        if user_guess_int == random_answer:
            print("Your guess was right!")
        else:
            # otherwise, tell them they were wrong
            print(
                "Your guess was wrong! The right answer was {}.".format(random_answer)
            )
    except:
        # if user guess cannot become an integer, then tell the user to enter an integer.
        print("{} is not an integer between 0 and 9.".format(user_guess_string))


if __name__ == "__main__":
    main()
