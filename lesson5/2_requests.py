# A program often needs to connect to websites to gather data.
# There are different ways to achieve this. One of the most common ways to do
# it is to use a REST API. It allows to gather data fast and securely.
# The communication provided by a REST API occurs via HTTP. The name of the
# package used to make an HTTP request in Python is, of course, request.

# Import the package.
import requests

# Requests are normal HTTP requests, so they can do more than just use a web
# API. More here: https://pypi.org/project/requests/

# Get a webpage.
response = requests.get('https://github.com')

# Print the response code, if it's 200 then the request was successful.
print(response)

# Access the actual content of the response and the headers.
print(response.content)
print(response.headers)

# Get data from an hypothetical service.
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.content)

# The response to this request is a JSON. As a matter of fact, a REST API
# always communicates via JSONs (that's also another reason why this file
# format is so important). Sure enough, the following operation can be done:
response_but_json = response.json()
print(response_but_json)

# To get the data provided from a website in a JSON that can be directly
# handled in Python is used the get method. To, instead, send data to a
# website a post or put method is typically accepted.

# At last, another important topic: security.
# Naturally, if we want to post a tweet on Twitter or get the numbers of subs
# from a Twitch channel via API, some sort of authentication is required. These
# information are not of public domain.
# The process of authentication can occur in different ways. One of the easiest
# ways to do it consists on having an una API Key that has to be included in
# the header of every call.

# Example:

# Define a token and url
token = "TOKEN"
url = "URL"

# Header as a dictionary
headers = {'Authorization': "Bearer {}".format(token)}

# Carry out the request
response = requests.get(url, headers=headers)

# This topic is very complex and there are many use cases. Here a complete
# guide: https://realpython.com/api-integration-in-python/
