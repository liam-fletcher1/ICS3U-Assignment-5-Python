#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Oct 2021
# This program asks the user for two numbers
# Then the programs find the LCM of the two numbers


def main():
    # this tells the user the LCM of two numbers

    # input
    number1 = input("Please enter the first number: ")
    number2 = input("Please enter the second number: ")

    # process and output
    try:
        number1_as_integer = int(number1)
        number2_as_integer = int(number2)
        if (
            number1_as_integer > number2_as_integer
        ):  # This finds the greatest number among the two.
            max = number1_as_integer
        else:
            max = number2_as_integer
        while True:
            if max % number1_as_integer == 0 and max % number2_as_integer == 0:
                max = max + 1
                print(
                    "The LCM of the two numbers is {0}".format(
                        number1_as_integer, number2_as_integer
                    )
                )
                break

    except Exception:
        print("This is an invalid number!")
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
