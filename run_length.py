"""
Question: Run Length
- Have the function RunLength (str) take the str parameter being passed and
  return a compressed version of the string

- Using the Run-length encoding algorithm. This algorithm works by taking the
  occurrence of each repeating character and outputting that number along with
  a single character of the repeating sequence. For example: "wwwggopp" would
  return 3w2g1o2p. The string will not contain any numbers, punctuation, or
  symbols.
"""


def run_length(string):
    # Split the string input into characters and store in word
    word = list(filter(str.isalpha, string))

    # Store occurence of each character in list name occurence
    # count = 1 means first occurence of each character
    occurrence = []
    count = 1

    # Iterate through each character, count += 1 when multiple occurence
    for i in range(len(word)):
        if i + 1 < len(word) and word[i] == word[i + 1]:
            count += 1
        # When there is no more occurence of the current character
        # Reset count = 1 for the occurence of next character
        else:
            occurrence.append(str(count) + word[i])
            count = 1

    # Combine all element in the occurence list into a single string
    return "".join(occurrence)


print(run_length("wwgg  , wopp"))
