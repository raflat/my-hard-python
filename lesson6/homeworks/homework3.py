import json
import random
import requests
from os.path import dirname, join

DEEZER_API_URL = "https://api.deezer.com/artist"


def absolute_path(relative_path):
    current_dir = dirname(dirname(__file__))

    return join(current_dir, relative_path)


def add_artist(name):
    with read(r"data\artists.json") as artists_file:
        artists_data = json.load(artists_file)
        artists_names = list(artists_data.keys())

    if name in artists_names:
        print(name, "is already present.")
    else:
        new_artist = requests.get("https://api.deezer.com/search/artist",
                                  params={"q": name, "strict": "on"}).json()

        if len(new_artist["data"]) == 0:
            print("No match found for", name)
        else:
            new_artist_entry = {}
            new_artist_entry[name] = {new_artist["data"][0]["id"]}
            print(new_artist_entry)


def albums_number(artist_name):
    with read(r"data\artists.json") as artists_ids:
        artists_ids = json.load(artists_ids)

    URL = DEEZER_API_URL + "/" + str(artists_ids[artist_name])
    return requests.get(URL).json()["nb_fan"]


def answer_is_correct(answer, first_artist, second_artist):
    if answer not in ("1", "2"):
        raise Exception("The answer should be either 1 or 2, but is", answer)

    first_artist_albums = albums_number(first_artist)
    second_artist_albums = albums_number(second_artist)

    correct_answer = "1" if first_artist_albums > second_artist_albums else "2"

    return answer == correct_answer


def ask_confirmation(question):
    print(question, end=" ")
    answer = input()

    return True if answer in ("y", "Y", "yes", "Yes", "YES") else False


def ask_to_add_artist():
    if ask_confirmation("Want to add an artist?"):
        add_artist(input("Name: "))


def quiz_question(first_artist, second_artist):
    print("Who has more fans,", first_artist,
          "(1) or", second_artist, "(2)?", end=" ")

    return input()


def random_artists_couple():
    with read(r"data\artists.json") as artists_file:
        artists_data = json.load(artists_file)
        artists_names = list(artists_data.keys())

    return random.sample(artists_names, 2)


def read(relative_path):
    return open(absolute_path(relative_path), "r")


def main():
    another_question = True
    while another_question:
        first_artist, second_artist = random_artists_couple()

        answer = quiz_question(first_artist, second_artist)

        try:
            if answer_is_correct(answer, first_artist, second_artist):
                print("Correct!")
            else:
                print("Wrong...")
        except Exception as e:
            print(e)

        ask_to_add_artist()
        another_question = ask_confirmation("Continue?")


if __name__ == "__main__":
    main()
