import os
import json
import re
from datetime import date

# For basic env initialization
def bot_init():
    if os.path.isfile('./birthdays.json') == False:
        json_object = {}
        json_object['birthdays'] = dict()
        json_object['birthdays']['CDW Bot#9650'] = date(2021, 4, 20).strftime("%Y-%m-%d")

        with open('birthdays.json', 'w') as birthday_file:
            json.dump(json_object, birthday_file)
            print("The json file has been created")

