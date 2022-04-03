import sys
from random import randint, random


class Research:
    def __init__(self, data_path):
        self.data_path = data_path
        self.calc = self.Calculations(self.file_reader())
        self.analytics = self.Analytics(self.file_reader())

    def file_reader(self, has_header=True):
        with open(self.data_path, 'r') as infile:
            rows = infile.readlines()
        if has_header:
            header = rows[0].split(',')
            if len(header) != 2:
                raise Exception('File has wrong header')
            rows = rows[1:]
        if len(rows) == 0:
                raise Exception('File has no data')
        res = []
        for row in rows:
            row = row.strip()
            if row != '0,1' and row != '1,0':
                raise Exception('File has wrong data')
            res.append([int(n) for n in row.split(',')])
        return res
        
    class Calculations:
        def __init__(self, data):
            self.data = data
        
        def counts(self):
            return [sum([el[0] for el in self.data]), sum([el[1] for el in self.data])]

        def fractions(self, heads, tails):
            return [heads / (heads + tails) * 100, tails / (heads + tails) * 100]

    class Analytics(Calculations):
        def __init__(self, data):
            super().__init__(data)

        def predict_random(self, n):
            res = []
            for i in range(n):
                tmp = randint(0, 1)
                res.append([tmp, (tmp + 1) % 2])
            return res

        def predict_last(self):
            return self.data[-1]
        

if __name__ == '__main__':
    if len(sys.argv) == 2:
        research = Research(sys.argv[1])
        data = research.file_reader()
        print(data)
        counts = research.calc.counts()
        print(counts[0], counts[1])
        fractions = research.calc.fractions(counts[0], counts[1])
        print(fractions[0], fractions[1])
        predict_random = research.analytics.predict_random(3)
        print(predict_random)
        predict_last = research.analytics.predict_last()
        print(predict_last)
