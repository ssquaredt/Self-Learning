"""
Question: Bracket Matcher
- Have the function BracketMatcher (str) take the str parameter being passed
and return 1 if the brackets are correctly matched and each one is accounted
for. Otherwise return 0.

- For example: if str is "(hello (world))", then the output should be 1, but
if str is "((hello (world))" the the output should be 0 because the brackets
do not  correctly match up. Only "(" and ")" will be used as brackets. If str
contains no brackets return 1.
"""


def bracket_matcher(text):
    # Stack to store character "("
    is_match = []

    # for loop to check if the bracket is match or not
    for character in text:
        if character == "(":
            is_match.append(character)
        elif character == ")":
            # Removes "(" from is_match, meaning that brackets are matched
            if "(" in is_match:
                is_match.pop()
            else:
                return 0

    # Return 1 when no element in is_match, showing brackets are correctly
    # matched, 0 when vice versa
    return 1 if len(is_match) == 0 else 0


user_input = input("Please enter a string: ")
print(bracket_matcher(user_input))
