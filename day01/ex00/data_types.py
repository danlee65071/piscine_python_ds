def data_types():
    int_var = 1
    str_var = 'str'
    float_var = 1.1
    bool_var = True
    list_var = list()
    dict_var = dict()
    tuple_var = tuple()
    set_var = set()
    print('[{}, {}, {}, {}, {}, {}, {}, {}]'.format(
        type(int_var).__name__, 
        type(str_var).__name__, 
        type(float_var).__name__,
        type(bool_var).__name__,
        type(list_var).__name__,
        type(dict_var).__name__,
        type(tuple_var).__name__,
        type(set_var).__name__))


if __name__ == '__main__':
    data_types()
