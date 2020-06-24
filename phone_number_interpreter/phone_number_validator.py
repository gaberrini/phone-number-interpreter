"""
Module with the logic used to validate if a number is a valid phone number.

Classes:
    PhoneValidator(metaclass=ABCMeta): Abstract base class of phone validator classes
    GreekPhoneNumberValidator(PhoneValidator): Implementation to validate Greek phone numbers
"""
from abc import ABCMeta, abstractmethod


class PhoneValidator(metaclass=ABCMeta):
    """Abstract base class for phone number validator classes"""

    @staticmethod
    @abstractmethod
    def validate(text_number: str) -> bool:
        """
        Validate if the number is a valid phone number

        :param text_number:
        :return: True if it is, False otherwise
        """
        raise NotImplementedError('Missing implementation of .validate(text_number: str)')


class GreekPhoneNumberValidator(PhoneValidator):
    """
    Implementation to of PhoneValidator for Greek phone numbers

    Attributes:
        GreekPhoneNumberValidator.GREEK_PHONE_LEN_10_START_1 (str): Possible start of a Greek phone number of 10 digits
        GreekPhoneNumberValidator.GREEK_PHONE_LEN_10_START_2 (str): Possible start of a Greek phone number of 10 digits
        GreekPhoneNumberValidator.GREEK_PHONE_LEN_14_START_1 (str): Possible start of a Greek phone number of 14 digits
        GreekPhoneNumberValidator.GREEK_PHONE_LEN_14_START_2 (str): Possible start of a Greek phone number of 14 digits
    """
    GREEK_PHONE_LEN_10_START_1 = '2'
    GREEK_PHONE_LEN_10_START_2 = '69'
    GREEK_PHONE_LEN_14_START_1 = '00302'
    GREEK_PHONE_LEN_14_START_2 = '003069'

    @staticmethod
    def validate(text_number: str) -> bool:
        """
        Validate if a number is a valid Greek phone number

        :param text_number:
        :return: True if it is, False otherwise
        """
        len_num = len(text_number)
        if len_num == 10:
            if text_number.startswith(GreekPhoneNumberValidator.GREEK_PHONE_LEN_10_START_1) or text_number.startswith(
                    GreekPhoneNumberValidator.GREEK_PHONE_LEN_10_START_2):
                return True
        if len_num == 14:
            if text_number.startswith(GreekPhoneNumberValidator.GREEK_PHONE_LEN_14_START_1) or text_number.startswith(
                    GreekPhoneNumberValidator.GREEK_PHONE_LEN_14_START_2):
                return True
        return False
