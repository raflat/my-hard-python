import json
from os.path import dirname, join


def absolute_path(relative_path):
    current_dir = dirname(dirname(__file__))
    return join(current_dir, relative_path)


def print_friends_number(email, data):
    i = 0
    while i < len(data) and email != data[i]["email"]:
        i += 1

    if i == len(data):
        print("User not found.")
    else:
        print("User with email '{}' has {} friends."
              .format(email, len(data[i]["friends"])))


def open_read(path):
    return open(absolute_path(path), "r")


def print_emails(data):
    print("Emails:")
    for user in data:
        print(user["email"])


def main():
    with open_read(r"data\01_data.json") as file:
        data = json.load(file)

        print_emails(data)
        print_friends_number("hollandoliver@electonic.com", data)


if __name__ == "__main__":
    main()
