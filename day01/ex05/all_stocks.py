import sys


def get_dict_key(dict, val_dict):
    for key_d, val_d in dict.items():
        if val_dict == val_d:
            return key_d


def to_company_str(cmp_name):
    return ''.join([cmp_name[i].upper() if i == 0 else cmp_name[i].lower() for i in range(len(cmp_name))])


def to_stock_str(stock_name):
    return stock_name.upper()


def is_company(cmps_names, cmp_name):
    cmp_name = to_company_str(cmp_name)
    if cmp_name in cmps_names:
        return True
    return False


def is_stocks(stocks_names, stock_name):
    stock_name = to_stock_str(stock_name)
    if stock_name in stocks_names:
        return True
    return False


def check_double_quotes(args):
    for arg in args:
        if arg == '':
            return True
    return False


def all_stocks():
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
    list_args = [s.strip() for s in sys.argv[1].split(',')]
    if check_double_quotes(list_args):
        print()
        return
    cmps_names = [*COMPANIES]
    stocks_names = [*STOCKS]
    for arg in list_args:
        if is_company(cmps_names, arg):
            cmp_name = to_company_str(arg)
            print(cmp_name, 'stock price is', STOCKS[COMPANIES[cmp_name]])
        elif is_stocks(stocks_names, arg):
            stock_name = to_stock_str(arg)
            print(stock_name, 'is a ticker symbol for', get_dict_key(COMPANIES, stock_name))
        else:
            print(arg, 'is an unknown company or an unknown ticker symbol')


if __name__ == '__main__':
    all_stocks()
