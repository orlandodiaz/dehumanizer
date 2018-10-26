"""
Parse humanized strings like 128M to 16K to something a machine can understand

"""

from decimal import Decimal

d = {
    'k': 3,
    'K': 3,
    'm': 6,
    'M': 6,
    'b': 9,
    'B': 9,

}


def parse_string(text):
    """ Parse humanized strings like 128M to 16K to something a machine can understand """

    if text[-1] in d:
        num, magnitude = text[:-1], text[-1]
        return int(Decimal(num) * 10 ** d[magnitude])
    else:
        return int(Decimal(text))
