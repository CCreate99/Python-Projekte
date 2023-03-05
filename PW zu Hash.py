import sys
from pathlib import Path
from os import path, getcwd
class Access:
    def __init__(self, any_website, any_username, any_password):
        self.website = any_website
        self.username = any_username
        self.password = any_password

if __name__ == '__main__':
    while True:
        website = input("Where do you want to register? ")
        username = input("What is your Username? ")
        password = input("What is your Password? ")

        access = Access(website, username, password)



        file = open('PasswordManager.txt', 'w')
        file.write('Website: ')
        file.write(access.website)
        file.write('\nUsername: ')
        file.write(access.username)
        file.write('\nPassword: ')
        file.write(access.password)
        file.close()

        file = open('PasswordManager.txt', 'r')
        inhalt = file.read()
        print(inhalt)
        file.close()
        break