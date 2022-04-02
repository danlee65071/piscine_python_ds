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
    input = sys.argv[1].lower()
    cmp_name = ''
    for i in range(len(input)):
        if i == 0:
            cmp_name += input[i].upper()
        else:
            cmp_name += input[i]
    cmps_names = [*COMPANIES]
    if cmp_name not in cmps_names:
        print('Unknown company')
        return
    cmp_stock_name = COMPANIES[cmp_name]
    print(STOCKS[cmp_stock_name]) 
    


if __name__ == '__main__':
    stock_prices()
