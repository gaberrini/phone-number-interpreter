"""
Dict with all possibles ambiguities when a number is spelled in the english language.

Build up dynamically

LANGUAGE_AMBIGUITIES = {
    '21': '201',
    ..
    '29': '209',
    '201': '21',
    ..
    '209': '29',
    '31': '301',
    ..
    '39': '309',
    '301': '31',
    ..
    '309': '39',
    ..
    '91': '901',
    ..
    '909': '99'
}

Attributes:
    LANGUAGE_AMBIGUITIES (dict): Dict with all possibles ambiguities of a spelled english number
    natural_numbers_ambiguities.build_language_ambiguities_dict()
"""
LANGUAGE_AMBIGUITIES = dict()


def build_language_ambiguities_dict():
    """
    Build the LANGUAGE_AMBIGUITIES dict

    :return:
    """
    for number in range(2, 10):
        for number_2 in range(1, 10):
            str_number = '{}{}'.format(number, number_2)
            str_ambiguity = '{}0{}'.format(number, number_2)
            LANGUAGE_AMBIGUITIES[str_number] = str_ambiguity
            LANGUAGE_AMBIGUITIES[str_ambiguity] = str_number


build_language_ambiguities_dict()
