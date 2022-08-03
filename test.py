import sqlite3, json

with open(f"users.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
    for dict in data:
        print(dict)