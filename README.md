# Index

* [Introduction](#introduction)
    * [Natural Number Ambiguities](#natural-number-ambiguities)
    * [Phone Numbers Validation](#phone-number-validation)
* [Requirements](#requirements)
    * [Docker requirements](#docker-requirements)
    * [Local requirements](#local-requirements)
    * [Development requirements](#development-requirements)
* [Usage instructions](#usage-instructions)
    * [Docker execution](#docker-execution)
    * [Local execution](#local-execution)
    * [Development tools](#development-tools)
        * [Run unittests from Docker](#run-unittests-from-docker)
        * [Run unittests and test coverage](#run-unittests-and-test-coverage)
        * [Pylint execution](#pylint-execution)

# Introduction

This application will process natural numbers verbally obtained in the English language, and validate if they are a valid Greek phone number.

The application have two main logic:

* [Natural Number Ambiguities](#natural-number-ambiguities)
* [Phone Numbers Validation](#phone-number-validation)

## Natural Number Ambiguities

Because the number is generated verbally, we could have possible ambiguities in the interpretation of the numbers.

The application must detect all possible ambiguities in the natural numbers and generate all possible interpretations of the number.

For example, if the speaker says `twenty five` this could be transcribed as `25` or `205`, if the number contains `73`, the number may be: `703` or `73`, etc.

We also need to consider that ambiguities can be exclusive.

Explanation of exclusive ambiguities:

```
Input: 2336

Possibles ambiguities: 23, 33, 36

Exclusive: 23 and 33, 33 and 36
```

Why Exclusive? If we consider that 23 is an ambiguity, is because the user input was "twenty three" or "twenty-three", making impossible the fact that the user could had spell "thirty three" or "thirty-three".

For example, all the possible interpretations for `2336` will be:

```
Input: "2336"
Interpretation 1: "2336" (No ambiguities)
Interpretation 2: "23306" (Ambiguity: "36")
Interpretation 3: "20336" (Ambiguity: "23")
Interpretation 4: "203306" (Ambiguities: "23" and "36")
Interpretation 5: "23036" (Ambiguity: "33")
```

## Phone Number Validation

After the application generate all the possible interpretations of a number it will validate if they are a valid Greek phone number and `print` the output.

A valid Greek phone numbers may have `10 digits` or `14 digits`.

If they have `10 digits`, they must start with `2` or `69`.

If they have `14 digits`, the must start with `00302` or `003069`.

For example:

```
If input is: 0 0 30 69 70 24 1 3 50 2, then output should be:
Interpretation 1: 003069702413502 [phone number: INVALID]
Interpretation 2: 00306970241352 [phone number: VALID]
...
Interpretation n: 00306972413502 [phone number: VALID]
...
Interpretation m: 00306097241352[phone number: INVALID]
```

# Requirements

You can run the application using [Docker] or from your local machine using [Python 3.8]

## Docker requirements

You can run the application using [Docker]

Requirements:
 * [Docker]

## Local requirements

You can run the application from your local machine

Requirements:
* [Python 3.8]

## Development requirements

To use the development tools you have an extra requirement

Requirements:
* [Python 3.8]
* [Pipenv]

To install the development requirements on your local machine you need to run the following command

```
pipenv install --dev
```

This will install the dev dependencies defined in the `Pipfile`

# Usage instructions

## Docker execution

To run the application using [Docker].

First you will need to build the Docker Image with the following command

```
docker build -t phone-interpreter-app .
```

Then you can run the application creating a Docker container

You can define the number as an argument when executing the command, if not it will be asked as user input.

When the number is defined as argument, if it contains spaces it needs to be between `" "`

```
docker run phone-interpreter-app "00306 9 702 4 13 52"
```

or to define the number as input, you need to add the command options `-i` when creating the container, to allow an interactive session with the container

```
docker run -i phone-interpreter-app
```

## Local execution

To run the application from your local machine using [Python 3.8]

You can define the number as an argument when executing the command, if not it will be asked as user input.

When the number is defined as argument, if it contains spaces it needs to be between `" "`

```
python -m phone_number_interpreter "00306 9 702 4 13 52"
```

or to provide the number as user input

```
python -m phone_number_interpreter
```

## Development tools

During development there are two tools that you can use [Pylint] and [Coverage]

To use the development tools on your local machine, you first need to install the [Development requirements](#development-requirements)

### Run unittests from Docker

To run the [unittests] from the Docker image, you need to run the following command

```
docker run phone-interpreter-app tests
```

### Run unittests and test coverage

To run the [unittests] you just need to have installed [Python 3.8], but to get the tests coverage you will need to install the [Development requirements](#development-requirements)

To run the tests without getting the [Coverage] you need to run the following command:

```
python -m unittest --verbose
```

To generate the tests [Coverage] you need to run the following command

```
pipenv run python -m coverage run -m unittest --verbose
```

The last command will run the tests, show the results and create a `.coverage` file with the tests [Coverage] result.

To see the results in the terminal you can run the following command

```
pipenv run python -m coverage report
```

You can also create a `HTML report` running the following command

```
pipenv run python -m coverage html
```

After running it a `HTML report` will be created, you can find it in the following path `./htmlcov/index.html`

### Pylint execution

To run [Pylint] you need to run the following command

```
pipenv run python -m pylint phone_number_interpreter
```

docker run --entrypoint=python -m unittest --verbose phone-interpreter-app

[Python 3.8]: https://www.python.org/downloads/
[Docker]: https://www.docker.com/
[Pipenv]: https://pipenv.pypa.io/en/latest/install/#installing-pipenv
[Coverage]: https://coverage.readthedocs.io/en/coverage-5.1/
[Pylint]: https://www.pylint.org/
[unittests]: https://docs.python.org/3/library/unittest.html
