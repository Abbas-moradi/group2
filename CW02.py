import sys

if len(sys.argv) == 3:
    print('Hello', *sys.argv[1:3])
elif len(sys.argv) < 3:
    print('the last name not input')
elif len(sys.argv) == 4:
    if sys.argv[3].isdigit():
        print('Hello', *sys.argv[1:3], 'your age is', sys.argv[3])
    else:
        print('invalid age')
