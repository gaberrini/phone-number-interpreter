"""
Create a runner for the tests and being able to trigger them from code

Attributes:
    run.run_tests(): Function to run the tests
"""
import unittest
import phone_number_interpreter.tests.test_natural_numbers_interpreter as test_natural_numbers_interpreter
import phone_number_interpreter.tests.test_phone_number_validator as test_phone_number_validator


def run_tests():
    """
    Add TestCases to the TestSuite and run them

    :return:
    """
    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # add tests to the test suite
    suite.addTests(loader.loadTestsFromModule(test_natural_numbers_interpreter))
    suite.addTests(loader.loadTestsFromModule(test_phone_number_validator))

    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)
