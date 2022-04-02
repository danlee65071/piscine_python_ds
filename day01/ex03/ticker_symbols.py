import sys


def get_dict_key(dict, val_dict):
    for key_d, val_d in dict.items():
        if val_dict == val_d:
            return key_d


def ticker_symbols():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    if len(sys.argv) != 2:
        return
    cmp_stocks_name = sys.argv[1].upper()
    if cmp_stocks_name not in [*STOCKS]:
        print('Unknown ticker')
        return
    print(get_dict_key(COMPANIES, cmp_stocks_name), STOCKS[cmp_stocks_name])


if __name__ == '__main__':
    ticker_symbols()
