import json
import random
import requests
from os.path import dirname, join


def absolute_path(relative_path):
    current_dir = dirname(__file__)

    return join(current_dir, relative_path)


def albums_number(artist_name):
    with read(r"data\artists.json") as artists_ids:
        artists_ids = json.load(artists_ids)

    URL = "https://api.deezer.com/artist/" + str(artists_ids[artist_name])
    return requests.get(URL).json()["nb_album"]


def answer_is_correct(answer, first_artist, second_artist):
    if answer not in ("1", "2"):
        raise Exception("The answer should be either 1 or 2, but is", answer)

    first_artist_albums = albums_number(first_artist)
    second_artist_albums = albums_number(second_artist)

    correct_answer = "1" if first_artist_albums > second_artist_albums else "2"

    return answer == correct_answer


def continue_quiz():
    print("Continue?")
    answer = input()

    return True if answer in ("y", "Y") else False


def quiz_question(first_artist, second_artist):
    print("Who published more albums between", first_artist,
          "(1) and", second_artist, "(2)?", end=" ")

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

        another_question = continue_quiz()


if __name__ == "__main__":
    main()
