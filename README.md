# Phone Number Interpreter

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
