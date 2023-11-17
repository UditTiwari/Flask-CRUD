import json

def read_file():
    with open("football.json") as file:
        data = json.load(file)

        return data

        