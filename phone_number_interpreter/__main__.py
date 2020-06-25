"""
Entry point of application when executed as a module

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
"""
from phone_number_interpreter import app


if __name__ == '__main__':
    app.run()
