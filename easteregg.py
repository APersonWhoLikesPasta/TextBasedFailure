import sys

def user_name_check(user_name):
    if user_name.upper() == "THANOS":
        print('A snap is heard, and you are turned to dust.')
        sys.exit()