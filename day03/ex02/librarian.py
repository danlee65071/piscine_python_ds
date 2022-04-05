#!hcharlsi/bin/python3

import os


if __name__ == '__main__':
    try:
        if os.environ['VIRTUAL_ENV'][-8:] == 'hcharlsi':
            os.system('pip3 install beautifulsoup4 pytest')
            os.system('pip3 freeze')
            os.system('pip3 freeze > requirements.txt')
    except KeyError:
        print('Wrong enviroment')
