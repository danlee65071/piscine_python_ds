def dict_sorter():
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
    dict_cont = dict()
    for el in list_of_tuples:
        dict_cont[el[0]] = int(el[1])
    dict_cont = {k: v for k, v in sorted(dict_cont.items(), key=lambda item: item[0])}
    sorted_dict = {k: v for k, v in sorted(dict_cont.items(), key=lambda item: item[1], reverse=True)}
    for k, v in sorted_dict.items():
        print(k)


if __name__ == '__main__':
    dict_sorter()
