import json
import wikipediaapi
from os.path import dirname, join


def main():
    data = {}
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    years = [str(year) for year in range(1992, 1993)]
    for year in years:
        data[year] = {}
        print("Fetching deaths in", year)
        for month in months:
            data[year][month] = deaths_in_date(year, month)

    with write(r"deaths.json") as file:
        json.dump(data, file, indent=3)


def absolute_path(relative_path):
    current_dir = dirname(__file__)

    return join(current_dir, relative_path)


def deaths_in_date(year, month):
    deaths = {}
    wiki = wikipediaapi.Wikipedia("en")

    day = 1
    start = False
    page_text = wiki.page("Deaths_in_" + month + "_" + year).text
    text_divided_by_day = page_text.split("\n")
    for line in text_divided_by_day:
        if line == str(day):
            deaths[day] = []
            day += 1
            start = True
        elif line != "" and not line.startswith("=") and start:
            person_data = extract_person_data(line)
            if person_data is not None:
                deaths[day - 1].append(person_data)

    return deaths


def write(relative_path):
    return open(absolute_path(relative_path), "w+")


def extract_person_data(record):
    data = record.split(", ")
    person = {}

    if len(data) > 1:
        person["name"] = data[0]
        try:
            person["age"] = int(data[1].split("-")[0].strip())
        except ValueError:
            return None
        person["info"] = data[2:]

        return person
    else:
        return None


if __name__ == "__main__":
    main()
