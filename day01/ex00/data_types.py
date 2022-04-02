def data_types():
    int_var = 1
    str_var = 'str'
    float_var = 1.1
    bool_var = True
    list_var = list()
    dict_var = dict()
    tuple_var = tuple()
    set_var = set()
    print(f'[{type(int_var).__name__}, ' +
            f'{type(str_var).__name__},  ' +
            f'{type(float_var).__name__}, '+
            f'{type(bool_var).__name__}, ' +
            f'{type(list_var).__name__}, ' +
            f'{type(dict_var).__name__}, ' +
            f'{type(tuple_var).__name__}, ' +
            f'{type(set_var).__name__}]')


if __name__ == '__main__':
    data_types()
