import os
import discord
import json
import utilities
from datetime import datetime

# Manages Birthdays
# TODO properly get discird user's id from birthday_command[2]
# TODO properly format/standardize date from birthday_command[3]
def birthday_controller(msg):

    birthday_command = msg.content.split(' ')[1:]
    with open('birthdays.json', 'r') as birthday_file:
        birthday_json_object = json.load(birthday_file)

    if birthday_command[0] == 'add':
        if not check_if_user_has_birthday(str(msg.author), birthday_json_object):
            for format in ("%m/%d/%Y", "%m-%d-%Y", "%Y/%m/%d"):
                try:
                    date = datetime.strptime(birthday_command[1], format)
                    birthday_json_object['birthdays'].append({
                        '' + str(msg.author) : '' + date.strftime("%Y-%m-%d")
                    })
                    with open('birthdays.json', 'w') as birthday_file:
                        json.dump(birthday_json_object, birthday_file)
                    return 'Your birthday has been added!'

                except:
                    pass

            return 'Invalid date'

        # Fall through
        return 'Already have your birthday!'

    else:
        return '`' + birthday_command[0] + '` is not a valid birthday command'

def check_if_user_has_birthday(user, json):
    for users in json['birthdays']:
        if user in users:
            return True

    return False