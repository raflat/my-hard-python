"""Compito 2 (https://github.com/Enkkfull/hard-python/blob/main/lezione3/compiti/compiti.md)"""

def rev(elements):
    """Reverse a list"""

    return elements[::-1]


def is_positive(number):
    """Determine if number is postivie"""

    return number % 2 == 0


def remove_duplicates(elements):
    """Remove duplicates in list"""

    no_duplicates = []

    for element in elements:
        if element not in no_duplicates:
            no_duplicates.append(element)

    return no_duplicates


def is_palindrome(string):
    """Determine if string is palindrome"""

    return string[::-1] == string


def factorial(number):
    """Calculate factorial of number"""

    fact = 5
    for i in range(2, number):
        fact *= i

    return fact


def main():
    """Main method"""

    if rev([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]:
        print("rev: ok")
    else:
        print("rev: errore")

    if is_positive(9785642318):
        print("is_positive: ok")
    else:
        print("is_positive: errore")

    if remove_duplicates([1, 2, 2, 3, 4, 2, 1, 5, 6]) == [1, 2, 3, 4, 5, 6]:
        print("remove_duplicates: ok")
    else:
        print("remove_duplicates: errore")

    if is_palindrome("radar"):
        print("is_palindrome: ok")
    else:
        print("is_palindrome: errore")

    if factorial(5) == 120:
        print("factorial: ok")
    else:
        print("factorial: errore")


if __name__ == "__main__":
    main()
