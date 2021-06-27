import os
import discord
import json
import utilities
from datetime import datetime

date_formats = ("%m/%d/%Y", "%m-%d-%Y", "%Y/%m/%d")

# Manages Birthdays
# TODO properly get discird user's id from birthday_command[2]
# TODO properly format/standardize date from birthday_command[3]
def birthday_controller(msg):

    birthday_command = msg.content.split(' ')[1:]
    with open('birthdays.json', 'r') as birthday_file:
        birthday_json_object = json.load(birthday_file)

    if birthday_command[0] == 'add':
        #if not check_if_user_has_birthday(str(msg.author), birthday_json_object):
        if str(msg.author) not in  birthday_json_object['birthdays']:
            for format in date_formats:
                try:
                    date = datetime.strptime(birthday_command[1], format)
                    birthday_json_object['birthdays'][str(msg.author)] = date.strftime("%Y-%m-%d")
                    with open('birthdays.json', 'w') as birthday_file:
                        json.dump(birthday_json_object, birthday_file)
                    return 'Your birthday has been added!'

                except:
                    pass

            return 'Invalid date'

        # Fall through
        return 'Already have your birthday!'

    elif birthday_command[0] == 'edit':
        if str(msg.author) in birthday_json_object['birthdays']:
            for format in date_formats:
                try:
                    date = datetime.strptime(birthday_command[1], format)
                    birthday_json_object['birthdays'][str(msg.author)] = date.strftime("%Y-%m-%d")
                    with open('birthdays.json', 'w') as birthday_file:
                        json.dump(birthday_json_object, birthday_file)
                    return 'Your birthday has been updated to ' + birthday_command[1] + '!'
                except:
                        pass
            return 'Invalid date'
        # Fall through
        return 'User not found~\nplease add your birthday using `$birthday add <date>`'
    else:
        return '`' + birthday_command[0] + '` is not a valid birthday command'

def check_birthdays():

    with open('birthdays.json', 'r') as birthday_file:
        birthday_json_object = json.load(birthday_file)

    userBirthdays = []

    for user in birthday_json_object['birthdays']:
        if birthday_json_object['birthdays'][user] == datetime.today().strftime("%Y-%m-%d"):
            print('found user')
            userBirthdays.append(user)

    return userBirthdays
