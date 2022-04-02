import sys


def names_extractor():
    if len(sys.argv) != 2:
        return
    with open(sys.argv[1], 'r') as infile:
        with open('employees.tsv', 'w') as outfile:
            outfile.write('Name\tSurname\tE-mail\n')
            mails = [s.strip() for s in infile.readlines()]
            for mail in mails:
                name, surname = mail.split('@')[0].split('.')
                name, surname = name.capitalize(), surname.capitalize()
                outfile.write(f'{name}\t{surname}\t{mail.strip()}\n')


if __name__ == '__main__':
    names_extractor()
