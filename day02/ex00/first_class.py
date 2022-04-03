class FirstClass:
    with open('data.csv', 'r') as infile:
        print(infile.read())


if __name__ == '__main__':
    FirstClass()