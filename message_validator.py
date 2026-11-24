"""
freeCodeCamp Daily Coding Challenge (24.11.2026)

Question: Message Validator
- Given a message string and a validation string, determine if the message
  is valid.

- A message is valid if each word in the message starts with the corresponding
  letter in the validation string, in order.

- Letters are case-insensitive.

- Words in the message are separated by single spaces.
"""


def is_valid_message(message, validation):

    # Split the string by single spaces and store in word
    # Grab the first character of each word and compare with validation
    # lower() in message and validation so will be treated as lower case,
    # even when user insert uppercase input

    first_character = [word[0] for word in message.lower().split()]

    if validation.lower() == "".join(first_character):
        return True
    else:
        return False

    return message


print(
    is_valid_message(
        "The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT"
    )
)
