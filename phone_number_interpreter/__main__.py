"""
Entry point of application when executed as a module

If the first argv is tests the TestCases are going to be executed.

Examples:
    Number provided as argv:
        $ python -m phone_number_interpreter "20 060 04 0 08"
        $ Input number: 2006004008
        $ Interpretation 1: 2006004008 [phone number: VALID]


    Number asked as input:
        $ python -m phone_number_interpreter
        $ Please insert the number: 20 060 04 0 08
        $ Input number: 2006004008
        $ Interpretation 1: 2006004008 [phone number: VALID]

    Run test cases:
        $ python -m phone_number_interpreter tests
        $ ..
"""
import sys
from phone_number_interpreter import app
from phone_number_interpreter.tests.run import run_tests


if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1] == 'tests':
        run_tests()
    else:
        app.run()
