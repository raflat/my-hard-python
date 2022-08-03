import requests
from prettytable import PrettyTable


def request_as_json(url):
    return requests.get(url).json()


def cross_check_mark(completed):
    return "\u2713" if completed else "\u2717"


def main():
    todos = request_as_json("https://jsonplaceholder.typicode.com/todos")
    users = request_as_json("https://jsonplaceholder.typicode.com/users")

    table = PrettyTable()
    fields = ["username", "TODOs"]
    for user in users:
        username = user["username"]
        fields[0] = username
        table.field_names = fields
        table.align[username] = "l"

        for task in todos:
            if task["userId"] == user["id"]:
                table.add_row([task["title"],
                              cross_check_mark(task["completed"])])

        print(table)

        table.clear_rows()


if __name__ == "__main__":
    main()
