"""Tests for phone_number_validator module"""
import unittest
from phone_number_interpreter.phone_number_validator import GreekPhoneNumberValidator


class TestGreekPhoneNumberValidator(unittest.TestCase):
    """Test GreekPhoneNumberValidator"""

    def test_greek_phone_number_validator_true_cases(self):
        """
        Test GreekPhoneNumberValidator().validate() for True cases
        :return:
        """
        # Data
        test_data = [('00306970241352', True),
                     ('00302970241352', True),
                     ('2970241352', True),
                     ('6970241352', True)]

        # When/Then
        for data in test_data:
            self.assertEqual(data[1], GreekPhoneNumberValidator().validate(data[0]))

    def test_greek_phone_number_validator_false_cases(self):
        """
        Test GreekPhoneNumberValidator().validate() for False cases
        :return:
        """
        # Data
        test_data = [('00306870241352', False),
                     ('00303970241352', False),
                     ('20303970241352', False),
                     ('69303970241352', False),
                     ('0030241352', False),
                     ('0030691352', False)]

        # When/Then
        for data in test_data:
            self.assertEqual(data[1], GreekPhoneNumberValidator().validate(data[0]))
