"""
Module with the logic to print the number interpretations the validation if they are a phone number

Attributes:
    app.print_interpretations_with_phone_validation(interpretations: Set[str], validator: Type[PhoneValidator])
    app.run()
"""
import sys
from typing import Set, Type
from phone_number_interpreter.natural_numbers_interpreter import NaturalNumbersInterpreter
from phone_number_interpreter.phone_number_validator import GreekPhoneNumberValidator, PhoneValidator


VALID = 'VALID'
INVALID = 'INVALID'


def print_interpretations_with_phone_validation(interpretations: Set[str], validator: Type[PhoneValidator]) -> None:
    """
    Go throw a list of numbers as strings and validate if they are a valid phone number, and print the following:

    Interpretation 1: xxxxxxxx [phone number: INVALID]
    ....
    Interpretation n: xxxxxxxxx [phone number: VALID]
    ....
    Interpretation m: xxxxxx [phone number: INVALID]

    :param interpretations:
    :param validator: PhoneValidator
    :return:
    """
    for (index, interpretation) in enumerate(interpretations):
        is_valid_phone_number = VALID if validator.validate(interpretation) else INVALID
        print('Interpretation {}: {} [phone number: {}]'.format(index+1, interpretation, is_valid_phone_number))


def run() -> None:
    """
    Start point of application.

    Number to process can be provided by argv, if not provided it will be asked as user input.

    :return:
    """
    input_number = sys.argv[1] if len(sys.argv) > 1 else input('Please insert the number: ')

    input_number = ''.join(input_number.split())

    print('Input number: {}'.format(input_number))

    try:
        possible_interpretations = NaturalNumbersInterpreter().get_all_possible_interpretations_of_number(input_number)
        print_interpretations_with_phone_validation(possible_interpretations, GreekPhoneNumberValidator)
    except ValueError:
        print('Invalid input number "{}", it must contain only numbers'.format(input_number))
