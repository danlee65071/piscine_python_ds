import sys
import os


class Research:
    def __init__(self, data_path):
        self.data_path = data_path

    def file_reader(self):
        with open(self.data_path, 'r') as infile:
            rows = infile.readlines()
        if len(rows) < 2:
            raise Exception('File has no data')
        header = rows[0].split(',')
        if len(header) != 2:
            raise Exception('File has wrong header')
        for row in rows[1:]:
            if row[0:3] != '0,1' and row[0:3] != '1,0':
                raise Exception('File has wrong data')
        return ''.join(rows)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(Research(sys.argv[1]).file_reader())
