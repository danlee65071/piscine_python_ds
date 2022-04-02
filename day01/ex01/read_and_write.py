import csv


def change_delimiter():
    rows = []
    with open('ds.csv', 'r') as ds_csv:
        reader = csv.reader(ds_csv, delimiter=',')
        for row in reader:
            rows.append(row)
    with open('ds.tsv', 'w') as ds_tsv:
        writer = csv.writer(ds_tsv, quoting=csv.QUOTE_NONE, delimiter=';', quotechar='',escapechar='\\')
        for row in rows:
            tsv_row = []
            for x in row:
                if x != 'false' and x != 'true':
                    x = '"' + x + '"'
                tsv_row.append(x)
            writer.writerow(tsv_row)
        

if __name__ == '__main__':
    change_delimiter()
