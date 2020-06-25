"""
Module with the logic to detect all the possible interpretations of a spelled number in english,
    taking in count all the possible ambiguities of the english language.

For example, if someone says 'twenty five' this could be transcribed as '25' or '205'.
    ‘75’, may be: ‘705’ or ‘75’ Etc..


Classes:
    PossibleInterpretation
    NaturalNumbersInterpreter
"""
from dataclasses import dataclass
from typing import List, Set, Optional
from phone_number_interpreter.natural_numbers_ambiguities import LANGUAGE_AMBIGUITIES


@dataclass
class PossibleInterpretation:
    """
    Representation of a number, split in elements.

    The elements are numbers as string, some of them can be possible ambiguities in english language.

    The indexes of the elements that are ambiguities are going to be stored in a set to detect exclusive ambiguities.
    To determinate the index we are considering the join of all the elements.

    Example:
        $ self.interpretation_elements=['2', '33', '6']
        $ self.ambiguity_indexes={1, 2}
    If we join all the elements we get '2336', begin '33' an ambiguity, they are in the indexes {1, 2}

    Attributes:
        interpretation_elements: List of numbers as string, with possible ambiguities
        ambiguity_indexes: Index of possibles ambiguities (considering join of interpretation_elements)
    """
    interpretation_elements: List[str]
    ambiguity_indexes = Set[int]

    def __init__(self, interpretation_elements: Optional[List[str]] = None, ambiguity_indexes: Optional[Set] = None):
        self.interpretation_elements = interpretation_elements if interpretation_elements else list()
        self.ambiguity_indexes = ambiguity_indexes if ambiguity_indexes else set()

    def add_ambiguity_element(self, element: str, indexes_set: Set[int]) -> None:
        """
        Add a new ambiguity element and the indexes involved

        :param element:
        :param indexes_set:
        :return:
        """
        self.interpretation_elements.append(element)
        self.ambiguity_indexes.update(indexes_set)

    def index_in_ambiguities(self, index: int) -> bool:
        """
        Check if an index is in the `ambiguity_indexes` set

        :param index:
        :return: True if is in the set, False otherwise
        """
        return index in self.ambiguity_indexes

    def indexes_intersect(self, indexes_set: Set[int]) -> bool:
        """
        Check if the indexes set intersect

        :param indexes_set:
        :return: True if they intersect, False otherwise
        """
        return bool(self.ambiguity_indexes.intersection(indexes_set))

    def add_interpretation_element(self, element: str) -> None:
        """
        Add an element to `interpretation_elements`
        :param element:
        :return:
        """
        self.interpretation_elements.append(element)


class NaturalNumbersInterpreter:
    """
    Class with the logic to detect the possible ambiguities in a spelled number and generate all the possible
    interpretations of the number
    """

    @staticmethod
    def generate_interpretations(possible_interpretation: PossibleInterpretation) -> Set[str]:
        """
        Generate all possible interpretations of a PossibleInterpretation, making all possible permutations of the
            possible ambiguities in the interpretation.

        :param possible_interpretation:
        :return: Set of possible interpretations
        """
        _interpretations = [[possible_interpretation.interpretation_elements[0]]]
        try:
            _interpretations.append([LANGUAGE_AMBIGUITIES[possible_interpretation.interpretation_elements[0]]])
        except KeyError:
            pass

        # Todo: time performance, creating strings instead of lists of elements and joining at the end
        for element in possible_interpretation.interpretation_elements[1:]:
            # Using range and len, because the list is being extended in the loop dynamically
            for interpretation_n in range(len(_interpretations)):  # pylint: disable=consider-using-enumerate
                # If the interpretation element have an ambiguity we create all possible interpretations with the
                # ambiguity and without it
                try:
                    ambiguity = LANGUAGE_AMBIGUITIES[element]
                    new_interpretation = _interpretations[interpretation_n].copy()
                    new_interpretation.append(ambiguity)
                    _interpretations.append(new_interpretation)
                # Element is not an ambiguity
                except KeyError:
                    pass
                _interpretations[interpretation_n].append(element)

        # Return the interpretations as a set of strings
        interpretations = [''.join(interpretation) for interpretation in _interpretations]
        return set(interpretations)

    def process_possible_interpretations(self, possible_interpretations: List[PossibleInterpretation]) -> Set[str]:
        """
        Create all possible interpretations of a number from a List of PossibleInterpretation, we will have more than
            one `possible_interpretations` if they are exclusive ambiguities in the number

        :param possible_interpretations:
        :return: Set of possible interpretations
        """
        interpretations = set()
        for possible_interpretation in possible_interpretations:
            interpretations.update(self.generate_interpretations(possible_interpretation))
        return interpretations

    @staticmethod
    def add_number_to_interpretations(number: str, index: int, possible_interpretations: List[PossibleInterpretation]):
        """
        Add a simple number to the interpretations elements, when the number is not part of an ambiguity

        We validate if the number has been included in a previous ambiguity

        :param number:
        :param index:
        :param possible_interpretations:
        :return:
        """
        for possible_interpretation in possible_interpretations:
            # Add the number to the interpretation elements if it is NOT already included in an ambiguity
            if not possible_interpretation.index_in_ambiguities(index):
                possible_interpretation.add_interpretation_element(number)

    def add_ambiguity_to_possible_interpretations(self,
                                                  text_number: str,
                                                  possible_interpretations: List[PossibleInterpretation],
                                                  start_index: int,
                                                  last_index: int) -> None:
        """
        This method update `possible_interpretations` in place!

        Add a possible ambiguity to the lists of possible interpretations elements, to detect exclusive
            ambiguities we store the indexes involved in the ambiguities

        The `possible_interpretations` is a list of PossibleInterpretation, where we track the elements of the possible
            interpretations and the indexes of the considered ambiguities

        Example of `possible_interpretations`:
        For `text_number='2336'`
        possible_interpretations = [
            PossibleInterpretation(interpretation_elements=['23', '36'], ambiguity_indexes={0, 1, 2, 3}),
            PossibleInterpretation(interpretation_elements=['2', '33', '6'], ambiguity_indexes={1, 2})
        ]
        We have 2 possible interpretations because there are exclusive ambiguities (indexes of ambiguities intersect)

        :param text_number:
        :param possible_interpretations:
        :param start_index: first element of ambiguity
        :param last_index: last element of ambiguity
        :return:
        """
        possible_ambiguity = text_number[start_index:last_index + 1]
        ambiguity_indexes = set(range(start_index, last_index + 1))
        exclusive_ambiguity = True

        for _possible_interpretation in possible_interpretations:
            # If the ambiguity is not exclusive with an existing ambiguity of the possible interpretation
            if not _possible_interpretation.indexes_intersect(ambiguity_indexes):
                _possible_interpretation.add_ambiguity_element(possible_ambiguity, ambiguity_indexes)
                exclusive_ambiguity = False

        # If the ambiguity is exclusive with all the previous possible interpretations,
        # we create a new possible interpretation to include this ambiguity
        if exclusive_ambiguity:
            # Todo: enhance performance build previous_possible_interpretations from possible_interpretations?
            # previous_possible_interpretations will not include the exclusive ambiguity that conflict with the new
            # current ambiguity, because the `last_index` to create possible interpretations is set to
            # not include the elements of the current new ambiguity.
            previous_possible_interpretations = self.create_possible_interpretations(text_number[:start_index],
                                                                                     last_index=start_index)
            for _previous_possible_interpretation in previous_possible_interpretations:
                _previous_possible_interpretation.add_ambiguity_element(possible_ambiguity, ambiguity_indexes)
                possible_interpretations.append(_previous_possible_interpretation)

    def create_possible_interpretations(self,
                                        text_number: str,
                                        last_index: Optional[int] = None) -> List[PossibleInterpretation]:
        """
        Receive a number as text, search all possible interpretations of the number searching for ambiguities in it,
         based on english language.

        The number will be process until `last_index`, if not provided all `text_number` will be processed

        To create the list of elements of a possible interpretation we are considering the exclusive ambiguities.

        This will give us more than one possible interpretation, creating all the possible combinations of exclusive
         ambiguities.

        Explanation of exclusive ambiguities:

        Input: 2336
        Possibles ambiguities: 23, 33, 36
        Exclusive: 23 and 33, 33 and 36

        Why Exclusive? If we consider that 23 is an ambiguity, is because the user input was "twenty three" or
         "twenty-three", making impossible the fact that the user could had spell "thirty three" or "thirty-three".
         When there are exclusive ambiguities their indexes of intersect, as shown in the following example

        Example:
            $ text_number = '2336'
            $ returns [
                PossibleInterpretation(interpretation_elements=['23', '36'], ambiguity_indexes={0, 1, 2, 3}),
                PossibleInterpretation(interpretation_elements=['2', '33', '6'], ambiguity_indexes={1, 2})
            ]

        :param text_number:
        :param last_index: Last index of the text_number to process, if not provided all the number is processed

        :raises ValueError: if `text_number` contains non numeric characters
        :return: List of PossibleInterpretations
        """
        # Init values
        last_index = last_index if last_index else len(text_number)
        possible_interpretations = [PossibleInterpretation()]
        index = 0
        number = text_number[0]

        try:
            for (index, number) in enumerate(text_number[:last_index]):

                # Possible ambiguities start with [2-9]
                if 1 < int(number) < 10:

                    # And continue with [1-9]
                    if 0 < int(text_number[index + 1]) < 10:
                        self.add_ambiguity_to_possible_interpretations(text_number,
                                                                       possible_interpretations,
                                                                       start_index=index,
                                                                       last_index=index + 1)
                        continue

                    # Or continue with 0 + [1-9]
                    if text_number[index + 1] == '0' and 1 < int(text_number[index + 2]) < 10:
                        self.add_ambiguity_to_possible_interpretations(text_number,
                                                                       possible_interpretations,
                                                                       start_index=index,
                                                                       last_index=index + 2)
                        continue

                # If not ambiguity is found, the number is added to the interpretations
                self.add_number_to_interpretations(number, index, possible_interpretations)

        except IndexError:
            # When we go out of index we must add the last element to the interpretations
            self.add_number_to_interpretations(number, index, possible_interpretations)

            # If the next index is inside the len of the number we must also add it to the interpretations
            if index + 1 < len(text_number):
                self.add_number_to_interpretations(text_number[index + 1], index + 1, possible_interpretations)

        return possible_interpretations

    def get_all_possible_interpretations_of_number(self, text_number: str) -> Set[str]:
        """
        Create all the possible interpretations of a number and return them in a Set of strings

        :param text_number:
        :raises ValueError: if `text_number` contains non numeric characters
        :return:
        """
        possible_interpretations = self.create_possible_interpretations(text_number)
        return self.process_possible_interpretations(possible_interpretations)
