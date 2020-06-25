"""
Module with the logic used to validate if a number is a valid phone number.

Classes:
    PhoneValidator(metaclass=ABCMeta): Abstract base class of phone validator classes
    GreekPhoneNumberValidator(PhoneValidator): Implementation to validate Greek phone numbers
"""
from abc import ABCMeta, abstractmethod


class PhoneValidator(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
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


class GreekPhoneNumberValidator(PhoneValidator):  # pylint: disable=too-few-public-methods
    """
    Implementation of PhoneValidator for Greek phone numbers

    Attributes:
        GreekPhoneNumberValidator.VALID_PHONES_LEN (List[int]): Valid lengths of Greek phone numbers
        GreekPhoneNumberValidator.VALID_PHONES_START (Dict[int, List[str]]): Dict with valid start of
         Greek phone numbers, the key will be the length and the value contain a List with valid starts for that length
    """
    VALID_PHONES_LEN = [10, 14]
    VALID_PHONES_START = {
        10: ['2', '69'],
        14: ['00302', '003069']
    }

    @staticmethod
    def validate(text_number: str) -> bool:
        """
        Validate if a number is a valid Greek phone number

        :param text_number:
        :return: True if it is, False otherwise
        """
        len_num = len(text_number)
        if len_num in GreekPhoneNumberValidator.VALID_PHONES_LEN:
            for valid_start in GreekPhoneNumberValidator.VALID_PHONES_START[len_num]:
                if text_number.startswith(valid_start):
                    return True
        return False
