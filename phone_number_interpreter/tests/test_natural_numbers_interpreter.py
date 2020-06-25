"""Tests for natural_numbers_interpreter module"""
import unittest
from phone_number_interpreter.natural_numbers_interpreter import NaturalNumbersInterpreter, PossibleInterpretation


class TestNaturalNumbersInterpreter(unittest.TestCase):

    def test_create_possible_interpretations(self):
        # Data
        input_number = '2336'
        expected_output = [
            PossibleInterpretation(interpretation_elements=['23', '36'],
                                   ambiguity_indexes={0, 1, 2, 3}),
            PossibleInterpretation(interpretation_elements=['2', '33', '6'],
                                   ambiguity_indexes={1, 2}),
        ]

        # When
        result = NaturalNumbersInterpreter().create_possible_interpretations(input_number)

        # Then
        assert result == expected_output

    def test_create_possible_interpretations_2(self):
        # Data
        input_number = '2303600333'
        expected_output = [
            PossibleInterpretation(interpretation_elements=['23', '0', '36', '0', '0', '33', '3'],
                                   ambiguity_indexes={0, 1, 3, 4, 7, 8}),
            PossibleInterpretation(interpretation_elements=['2', '303', '6', '0', '0', '33', '3'],
                                   ambiguity_indexes={1, 2, 3, 7, 8}),
            PossibleInterpretation(interpretation_elements=['23', '0', '36', '0', '0', '3', '33'],
                                   ambiguity_indexes={0, 1, 3, 4, 8, 9}),
            PossibleInterpretation(interpretation_elements=['2', '303', '6', '0', '0', '3', '33'],
                                   ambiguity_indexes={1, 2, 3, 8, 9})
        ]

        # When
        result = NaturalNumbersInterpreter().create_possible_interpretations(input_number)

        # Then
        assert result == expected_output

    def test_create_possible_interpretations_3(self):
        # Data
        input_number = '2220'
        expected_output = [
            PossibleInterpretation(interpretation_elements=['22', '2', '0'],
                                   ambiguity_indexes={0, 1}),
            PossibleInterpretation(interpretation_elements=['2', '22', '0'],
                                   ambiguity_indexes={1, 2}),
        ]

        # When
        result = NaturalNumbersInterpreter().create_possible_interpretations(input_number)

        # Then
        assert result == expected_output

    def test_get_all_possible_interpretations_of_number(self):
        # Data
        input_number = '2336'
        expected_output = {'2336', '23306', '20336', '203306', '23036'}

        # When
        result = NaturalNumbersInterpreter().get_all_possible_interpretations_of_number(input_number)

        assert result == expected_output
