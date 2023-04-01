"""Task 8: using context manager, parse text.txt >> list & print how much 'catch me'`s """

import re


def file_parser():
    """parsing results goes in list, print number of repeats"""
    with open('text.txt') as opened_file:
        parse_result = re.findall('catch me', opened_file.read())
        print(len(parse_result))


file_parser()
