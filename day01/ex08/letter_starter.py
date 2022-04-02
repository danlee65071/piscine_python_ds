import sys


def letter_scatter():
    if len(sys.argv) != 2:
        return
    with open('employees.tsv', 'r') as infile:
        rows = infile.readlines()
        for row in rows[1:]:
            mail = row.strip().split('\t')[2]
            name = row.strip().split('\t')[0]
            if sys.argv[1] == mail:
                print(f'Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you.' +
                         ' That’s a precondition for the professionals that our company hires.')


if __name__ == '__main__':
    letter_scatter()
