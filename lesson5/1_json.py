# Particularly useful file format.
# Can be easily read/written because it conveniently encodes data as lists,
# dictionaries, integers and strings.

# To use JSON files, import the JSON module.
import json

# It's possible to convert a JSON string into a JSON object
my_json_string = '{"name": "Bob", "languages": ["Python", "Java"]}'
now_its_an_object = json.loads(my_json_string)

# or a JSON object into a JSON string.
person_dict = {'name': 'Bob', 'age': 12, 'children': None}
person_json = json.dumps(person_dict)

# Read a JSON file.
with open('path_to_file/person.json', 'r') as f:
    data = json.load(f)

# Write a JSON file.
with open('path_to_file/person.json', 'w') as f:
    json.dump(data, f, indent=3)

# https://www.programiz.com/python-programming/json
