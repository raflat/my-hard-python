# A program in Python terminates if it encounters an error.
# There are two families of errors: syntax errors and exceptions.
# Syntax errors are generated because of badly written code, e.g.
# "print('ciao'))", that causes a "SyntaxError: invalid syntax" message. While
# exceptions are generated when something like "print(0/0)" is executed.

# Python allows the programmer to handle exceptions. In particular, in Python
# exceptions can be raised and caught.

# In the following example the code expects the user to input an integer grater
# than five. Thanks to "raise Exception()" a generic exception with a custom
# message can be raised.
x = int(input("Insert a value greater than five: "))
if x <= 5:
    raise Exception("Exception: the value inserted must be greater than five.")

# Assertions can be made so that if they are false the program stops.
# The following lines of comments are an example.

# import sys
# assert ('linux' in sys.platform), "This code runs on Linux only."

# The try-catch clause is used to catch exceptions.
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)

# For additional uses of this clause see
# https://realpython.com/python-exceptions/
