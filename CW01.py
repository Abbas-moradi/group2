import sys
import datetime
import os


def create_user():
    name = input('enter your user name :')
    password = input('enter your password :')
    with open('user.txt', 'a') as user:
        user.write(f'\nuser name: {name}\npassword: {password}')

def create_superuser():
    name = input('enter your user name :')
    password = input('enter your password :')
    with open('user.txt', 'r') as user:
        lines = user.readlines()
        user.seek(0)  # go back to the beginning of the file
        with open('user.txt', 'w') as user:
            user.write(f'super user: {name}\npassword: {password}\n')
            for line in lines:  # write old content after new
                user.write(line)


def show_list():
    with open('user.txt', 'r') as user:
        user = user.readlines()
        for line in user:
            if 'user name' in line:
                print(line, end='')

def backup():
    now = datetime.date.today().strftime("%Y%m%d")
    with open('user.txt', 'r') as user:
        user = user.read()
        name = f'{now}_backup.txt'
        with open(name, 'w') as back:
            back.write(user)

def restore():
    f_name = input('enter file name: ')
    if os.path.isfile(f_name):
        with open(f_name, 'r') as f:
            print(f.read())
    else:
        print('file not found!')


if sys.argv[1] == "create":
    create_user()
elif sys.argv[1] == 'createsuperuser':
    with open('user.txt', 'r') as suser:
        first_line = suser.readline().strip('\n')
        if 'super user' in first_line:
            print('the super user exist!')
        else:
            create_superuser()

elif sys.argv[1] == 'show':
    show_list()

elif sys.argv[1] == 'backup':
    backup()
elif sys.argv[1] == 'restore':
    restore()