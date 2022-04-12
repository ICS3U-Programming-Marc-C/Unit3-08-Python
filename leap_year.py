#!/usr/bin/env python3
# Created by Marc Coffi
# Created in April 2022
# Leap year calculator


def main():
    user_input = input("Enter a year: ")
    try:
        user_int = int(user_input)

        user_int_4 = user_int % 4
        user_int_100 = user_int % 100
        user_int_400 = user_int % 400

        if user_int_4 == 0:
            if user_int_100 == 0:
                if user_int_400 == 0:
                    print("{} is a leap year.".format(user_int))
                else:
                    print("{} is not a leap year.".format(user_int))
            else:
                print("{} is a leap year.".format(user_int))

        else:
            print("{} is not a leap year.".format(user_int))

    except:
        print("Invalid Input")


if __name__ == "__main__":
    main()
