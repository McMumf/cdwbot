import os
import json

# For basic env initialization
def bot_init():
    if os.path.isfile('./birthdays.json') == False:
        json_object = {}
        json_object['birthdays'] = []
        json_object['birthdays'].append({
            'user_id' : 'CDW Bot#9650',
            'birthday' : '2021-4-20'
        })
        with open('birthdays.json', 'w') as birthday_file:
            json.dump(json_object, birthday_file)
            print("The json file is created")

# Manages Birthdays
# TODO properly get discird user's id from birthday_command[2]
# TODO properly format/standardize date from birthday_command[3]
def birthday_control(msg):

    birthday_command = msg.split(' ')
    birthday_json_object = json.load("./birthdays.json")

    if birthday_command[1] == "add":
        birthday_json = '{ "userId" : ' + birthday_command[2] + ' "birthday" : ' + birthday_command[3] + '}'
        birthday_json_object['birthdays'].append({
            'user_id' : birthday_command[2],
            'birthday' : birthday_command[3]
        })
        with open('birthdays.json', 'rw') as birthday_file:
            json.dump(birthday_json_object, birthday_file)
            print("The json file is created")