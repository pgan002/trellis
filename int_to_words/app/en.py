#!/usr/bin/python3
import argparse
import sys

import large_int

DESCRIPTION = """Convert an integer number into words in English.\n
For large numbers, use the short scale used in US, Canada, and modern British 
English.\n
The largest number is 10**%s-1.""" % large_int.MAX

UNITS_AND_TEENS = [
    'zero', 'one', 'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine',
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen'
]
TENS = [
    '', 'ten', 'twenty', 'thirty', 'forty', 'fifty',
    'sixty', 'seventy', 'eighty', 'ninety'
]


def int_to_words(n):
    """Convert integer `n` to words in English"""
    if not isinstance(n, (int, str)):
        raise ValueError('Expected an integer')
    n = str(n)
    if n.startswith('-'):
        sign = 'minus '
        n = n[1:]
    else:
        sign = ''

    if len(n) >= large_int.MAX:
        raise ValueError('Error: %s: Maximum absolute number is 10**%s-1' 
                         % (n, large_int.MAX))

    # Units and teens
    if int(n) <= 19:
        return sign + UNITS_AND_TEENS[int(n)]
    
    # Tens
    if len(n) <= 2:
        result = sign + TENS[int(n[0])]
        if n[1] != '0':
            result += '-' + UNITS_AND_TEENS[int(n[1])]
        return result
        
    # Hundreds, thousands and greater
    if len(n) <= 3:
        _, boundary = divmod(len(n) - 1, 2)
        unit = 'hundred'
    elif len(n) <= 6:
        _, boundary = divmod(len(n) - 1, 3)
        unit = 'thousand'
    else:
        exp, boundary = divmod(len(n) - 1, 3)
        unit = large_int.large_int_word(exp - 1)

    prefix = n[:boundary + 1]
    suffix = n[boundary + 1:].lstrip('0')
    result = sign + int_to_words(prefix) + ' ' + unit
    if suffix:
        if len(suffix) <= 2:
            result += ' and'
        result += ' ' + int_to_words(suffix)
    return result


def test_ok():
    # TODO: Add unittest integration
    cases = [
        (12, 'twelve'),
        (20, 'twenty'),
        (99, 'ninety-nine'),
        (101, 'one hundred and one'),
        (1001, 'one thousand and one'),
        (10093, 'ten thousand and ninety-three'),
        (1234, 'one thousand two hundred and thirty-four'),
        (12345, 'twelve thousand three hundred and forty-five'),
        (100000000, 'one hundred million'),
        (0, 'zero'),
        (12345678, 'twelve million three hundred and forty-five thousand six '
                   'hundred and seventy-eight'),
        (-10, 'minus ten'),
    ]
    for n, expected in cases:
        actual = int_to_words(n)
        assert actual == expected, (actual, expected)


def test_errors():
    cases = ['hello', 1.0, '', None]
    for x in cases:
        try:
            int_to_words(x)
        except ValueError:
            continue
        raise 'Expected ValueError: %s' % x


parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument('integer', nargs='*', type=int)
parser.add_argument('-t', '--test', action='store_true', help='Run tests')


if __name__ == '__main__':
    args = parser.parse_args()
    if args.test:
        test_ok()
        test_errors()
    else:
        for n in args.integer:
            try:
                print(int_to_words(n))
            except ValueError as e:
                print(e, file=sys.stderr)
