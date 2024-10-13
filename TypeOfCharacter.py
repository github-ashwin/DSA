def check_char(c):
    if c.islower():
        print('lowercase')
    elif c.isupper():
        print('uppercase')
    elif c.isdigit():
        print('digit')
    else:
        print(ord(c))

c = input()
check_char(c)