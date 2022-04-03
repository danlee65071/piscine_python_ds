from random import randint
import logging
import requests
import json


class Research:
    def __init__(self, data_path):
        self.data_path = data_path
        self.logger = logging.getLogger('logger')
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.FileHandler('analytics.log', mode='w')
        self.logger.addHandler(self.handler)
        self.formatter = logging.Formatter(fmt='%(asctime)s %(message)s')
        self.handler.setFormatter(self.formatter)
        self.__file_reader = 0
        # self.data = self.file_reader()
        # self.calc = self.Calculations(self.data, self.logger)
        # self.analytics = self.Analytics(self.data, self.logger)

    def file_reader(self, has_header=True):
        if self.__file_reader != 0:
            self.logger.debug('Read ' + self.data_path)
        self.__file_reader += 1
        with open(self.data_path, 'r') as infile:
            rows = infile.readlines()
        if has_header:
            header = rows[0].split(',')
            if len(header) != 2:
                self.logger.error('File has wrong header')
                raise Exception('File has wrong header')
            rows = rows[1:]
        if len(rows) == 0:
            self.logger.error('File has no data')
            raise Exception('File has no data')
        res = []
        for row in rows:
            row = row.strip()
            if row != '0,1' and row != '1,0':
                self.logger.error('File has wrong data')
                raise Exception('File has wrong data')
            res.append([int(n) for n in row.split(',')])
        return res

    def send_report(self, message, webhook):
        slack_data = {'text': message}
        requests.post(
            webhook,
            data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
            )
        
    class Calculations:
        def __init__(self, data, logger):
            self.data = data
            self.logger = logger
        
        def counts(self):
            self.logger.debug('Calculating the counts of heads and tails')
            return [sum([el[0] for el in self.data]), sum([el[1] for el in self.data])]

        def fractions(self, heads, tails):
            self.logger.debug('Calculating the fractions of heads and tails')
            return [heads / (heads + tails) * 100, tails / (heads + tails) * 100]

    class Analytics(Calculations):
        def __init__(self, data, logger):
            super().__init__(data, logger)

        def predict_random(self, n):
            self.logger.debug('Predict the random of heads and tails')
            res = []
            for i in range(n):
                tmp = randint(0, 1)
                res.append([tmp, (tmp + 1) % 2])
            return res

        def predict_last(self):
            self.logger.debug('Predict the last of heads and tails')
            return self.data[-1]

        def save_file(self, data, file_name, extension='txt'):
            self.logger.debug('Save data to ' + file_name + '.' + extension)
            with open(file_name + '.' + extension, 'w') as outfile:
                outfile.write(data)
