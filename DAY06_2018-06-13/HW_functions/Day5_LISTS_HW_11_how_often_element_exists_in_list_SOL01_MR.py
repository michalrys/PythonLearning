# 2018-06-17
# Autor: Michał Ryś
# InfoShare: day 06: funkcje. Homework
#
# He recently became interested in squares as well, and formed the definition of
# a fair and square number - it is a number that is a palindrome and the square
# of a palindrome at the same time. For instance, 1, 9 and 121 are fair and
# square (being palindromes and squares, respectively, of 1, 3 and 11),
# while 16, 22 and 676 are not fair and square: 16 is not a palindrome,
# 22 is not a square, and while 676 is a palindrome and a square number,
# it is the square of 26, which is not a palindrome.
#
# Now he wants to search for bigger fair and square numbers. Your task is,
# given an interval Little John is searching through, to tell him how many
# fair and square numbers are there in the interval, so he knows when he has
# found them all.
#
# Example data:
# range(from, to(including) ) output(number of fair and square numbers in range)
# 1 4 2
# 10 120 0
# 100 1000 2
# ------------------------------------------------------------------------------
# functions
def get_square_root(number):
    squeare_root = number ** 0.5
    return squeare_root

def get_is_palindrome(number: int) -> bool:
    """Check if number is palindrome.

    :rtype: bool
    :param int number: User integer number.
    :return: Number is or is not palindrome.
    """
    number_reversed = str(number)[::-1]
    number_reversed = int(number_reversed)
    if number == number_reversed:
        return True
    else:
        return False

def get_is_square(number: int) -> bool:
    """Check if number is square.

    :rtype: bool
    :param int number: User integer number.
    :return: Number is or is not square.
    """
    square_root = get_square_root(number)
    if square_root.is_integer():
        return True
    else:
        return False

def get_is_fair_and_square_number(number: int) -> bool:
    """Get if number is fair and square.

    :rtype: bool
    :param int number: Integer number.
    :return: Number is or is not fair and square.
    """
    number_is_palindrome = get_is_palindrome(number)
    number_is_square = get_is_square(number)

    square_root = get_square_root(number)
    if square_root.is_integer():
        square_root = int(square_root)
    else:
        return False

    if number_is_palindrome == number_is_square == True:
        square_root_is_palindrome = get_is_palindrome(square_root)
        if square_root_is_palindrome == True:
            return True
        else:
            return False
    else:
        return False

def get_how_many_fair_and_square_numbers_are_in_range(range_start: int,
                                                      range_end: int) -> int:
    """Count how many numbers in defined range are fair and square.

    :rtype: int
    :param int range_start: Beginning of range.
    :param int range_end: End of range.
    :return: Amount of fair and square numbers in range.
    """
    fair_and_square_numbers_are_in_range = 0

    for number in range(range_start, range_end+1):
        if get_is_square(number):
            if get_is_palindrome(number):
                if get_is_fair_and_square_number(number):
                    fair_and_square_numbers_are_in_range += 1
                    # print(number)
    # print(fair_and_square_numbers_are_in_range)
    return fair_and_square_numbers_are_in_range

# ------------------------------------------------------------------------------
# constants
MESSAGE_OUT = 'Wynik sprawdzenia: {result}'

# check for functions
# user_number = 4

# print(get_square_root(user_number))
# print(get_is_palindrome(user_number))
# print(get_is_palindrome(user_number))
# print(get_is_fair_and_square_number(user_number))

check_01 = get_how_many_fair_and_square_numbers_are_in_range(1, 4)
check_02 = get_how_many_fair_and_square_numbers_are_in_range(10, 120)
check_03 = get_how_many_fair_and_square_numbers_are_in_range(100, 1000)
check_04 = get_how_many_fair_and_square_numbers_are_in_range(1000, 1000000)
check_05 = get_how_many_fair_and_square_numbers_are_in_range(1, 1000000)

# printout
print(MESSAGE_OUT.format(result=check_01))
print(MESSAGE_OUT.format(result=check_02))
print(MESSAGE_OUT.format(result=check_03))
print(MESSAGE_OUT.format(result=check_04))
print(MESSAGE_OUT.format(result=check_05))

