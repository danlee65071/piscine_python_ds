import sys


def stock_prices():
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
    cmp_name = sys.argv[1].lower().capitalize()
    if cmp_name not in [*COMPANIES]:
        print('Unknown company')
        return
    print(STOCKS[COMPANIES[cmp_name]]) 
    


if __name__ == '__main__':
    stock_prices()
