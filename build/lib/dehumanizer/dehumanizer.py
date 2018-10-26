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
    if text[-1] in d:
        num, magnitude = text[:-1], text[-1]
        return int(Decimal(num) * 10 ** d[magnitude])
    else:
        return int(Decimal(text))

# text_to_num('3.17B')
# Decimal('3170000000.00')
# text_to_num('4M')
# Decimal('4000000')
# text_to_num('4.1234567891234B')
# Decimal('4123456789.1234000000000')