import sys


def caesar():
    if len(sys.argv) != 4:
        raise Exception('Wrong number of arguments')
    text = sys.argv[2]
    try:
        text.encode('ascii')
    except UnicodeEncodeError:
        raise Exception('The script does not support your language yet')
    shift = int(sys.argv[3])
    if sys.argv[1] == 'decode':
        shift *= -1
    elif sys.argv[1] != 'encode':
        raise Exception('Wrong command')
    lower = list('abcdefghijklmnopqrstuvwxyz')
    capital = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    res = ''
    for c in text:
        if c in lower:
            res += lower[(lower.index(c) + shift) % 26]
        elif c in capital:
            res += capital[(capital.index(c) + shift) % 26]
        else:
            res += c
    print(res)


if __name__ == '__main__':
    caesar()
    