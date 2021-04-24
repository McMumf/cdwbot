import os
import json
import re
from datetime import datetime

# For basic env initialization
def bot_init():
    if os.path.isfile('./birthdays.json') == False:
        json_object = {}
        json_object['birthdays'] = []
        json_object['birthdays'].append({
            'CDW Bot#9650': format_date('4/20/2021')
        })
        with open('birthdays.json', 'w') as birthday_file:
            json.dump(json_object, birthday_file)
            print("The json file has been created")

