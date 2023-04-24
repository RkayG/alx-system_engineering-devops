#!/usr/bin/python3
"""Uses REST Api to get to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    done = [t.get('title') for t in todos if t.get("done") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(done), len(todos)))
    [print("\t {}".format(d)) for d in done]
