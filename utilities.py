import os
import json

# For basic env initialization
def bot_init():
    if os.path.isfile('./birthdays.json') == False:
        json_object = {}
        json_object['birthdays'] = []
        json_object['birthdays'].append({
            'CDW Bot#9650': '2021-4-20'
        })
        with open('birthdays.json', 'w') as birthday_file:
            json.dump(json_object, birthday_file)
            print("The json file has been created")

