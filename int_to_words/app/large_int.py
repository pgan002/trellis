#!/usr/bin/python3
import argparse

# Reference: https://en.wikipedia.org/wiki/Names_of_large_numbers


UNITS = [
    '', 'm', 'b', 'tr', 'quadr', 'quint', 'sext', 'sept', 'oct', 'non'
]
UNIT_PREFIXES = [
    '', 'un', 'duo', 'tre', 'quattuor', 'quinqua', 'se', 'septen', 'octo', 
    'noven'
]
TENS = [
    '', 'dec', 'vigint', 'trigint', 'quadragint', 'quinquagint',
    'sexagint', 'septuagint', 'octoging', 'nonagint'
]
HUNDREDS = [
    '', 'cent', 'ducent', 'trecent', 'quadringent', 'quingent', 'sescent',
    'septigent', 'octigent', 'nongent'
]
MAX = 3 * 10000 + 3
TEST_CASES = [
    (1, 'million'),
    (2, 'billion'),
    (10, 'decillion'),
    (11, 'undecillion'),
    (22, 'duovigintillion'),
    (38, 'octotrigintillion')
]

parser = argparse.ArgumentParser(
    description='Produce the names of large integers')
parser.add_argument('-t', '--test', action='store_true', help='Run tests')
parser.add_argument('index',
                    nargs='*',
                    type=int,
                    help='integer `x` such that `n` = 10 ** (3 * `x` + 3), '
                         'where `n` is the integer whose name this script '
                         'returns')


def large_int_word(x):
    """Return the name of the large integer n = 10 ** (3 * x + 3)"""

    digits = [int(i) for i in str(x)]
    units = tens = hundreds = thousands = ''

    if len(digits) == 1:
        units = UNITS[digits[-1]]
    else:
        units = UNIT_PREFIXES[digits[-1]]
        tens = TENS[digits[-2]]
        if len(digits) >= 3:
            hundreds = HUNDREDS[digits[-3]]
        if len(digits) >= 4:
            thousands = UNITS[digits[-4]] + 'illin'
        if len(digits) >= 5:
            raise

    return units + tens + hundreds + thousands + 'illion'


def test():
    for x, name in TEST_CASES:
        assert large_int_word(x) == name, large_int_word(x)


if __name__ == '__main__':
    args = parser.parse_args()
    for i in args.index:
        print(large_int_word(i))
