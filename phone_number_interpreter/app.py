import sys
from typing import Set, Type
from phone_number_interpreter.natural_numbers_interpreter import NaturalNumbersInterpreter
from phone_number_interpreter.phone_number_validator import GreekPhoneNumberValidator, PhoneValidator


VALID = 'VALID'
INVALID = 'INVALID'


def print_phones_interpretations(interpretations: Set[str], validator: Type[PhoneValidator]) -> None:
    """
    Go throw a list of numbers as strings and validate if they are a valid phone number

    Print:

    Interpretation 1: xxxxxxxxxxx [phone number: INVALID|VALID]
    ....
    Interpretation m: xxxxxx [phone number: INVALID|VALID]


    :param interpretations:
    :param validator: PhoneValidator
    :return:
    """
    for (index, interpretation) in enumerate(interpretations):
        is_valid = VALID if validator.validate(interpretation) else INVALID
        print('Interpretation {}: {} [phone number: {}]'.format(index+1, interpretation, is_valid))


def run():
    input_number = sys.argv[1] if len(sys.argv) > 1 else input('Please insert the number:\n')

    input_number = ''.join(input_number.split())

    print('Input number: {}'.format(input_number))
    interpreter = NaturalNumbersInterpreter()
    possible_interpretations = interpreter.get_all_possible_interpretations_of_number(input_number)
    print_phones_interpretations(possible_interpretations, GreekPhoneNumberValidator)
