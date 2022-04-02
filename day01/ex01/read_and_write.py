def read_and_write():
    with open('ds.csv', 'r') as infile:
        with open('ds.tsv', 'w') as outfile:
            outfile.write(infile.read().replace('",', '"\t').replace('false,', 'false\t').replace('true,', 'true\t'))


if __name__ == '__main__':
    read_and_write()
