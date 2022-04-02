def to_dictionary():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    dict_res = dict()
    for el in list_of_tuples:
        if el[1] not in dict_res:
            dict_res[el[1]] = [el[0]]
        else:
            dict_res[el[1]].append(el[0])
    for key_d, vals_d in dict_res.items():
        for val in vals_d:
            print(f'\'{key_d}\' : \'{val}\'')


if __name__ == '__main__':
    to_dictionary()