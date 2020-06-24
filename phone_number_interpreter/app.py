import sys
from phone_number_interpreter.natural_numbers_interpreter import NaturalNumbersInterpreter


def run():
    print(sys.argv)

    # input_number = sys.argv[1] if len(sys.argv) > 1 else input('Please insert the number:')

    input_number = '2106930664'

    input_number = ''.join(input_number.split())

    interpreter = NaturalNumbersInterpreter()
    possible_interpretations = interpreter.get_all_possible_interpretations_of_number(input_number)
    print(len(possible_interpretations))
    print('\n'.join(possible_interpretations))
