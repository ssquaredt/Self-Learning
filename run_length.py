def RunLength(strParam):
    # Question
    # Have the function RunLength (str) take the str parameter being passed and return a compressed version of the string using the Run-length encoding algorithm. 
    # This algorithm works by taking the occurrence of each repeating character and outputting that number along with a single character of the repeating sequence. 
    # For example: "wwwggopp" would return 3w2g1o2p. 
    # The string will not contain any numbers, punctuation, or symbols.

    # 1. Create an empty string `answer = ""` to store our final result.
    answer = ""

    # 2. Keep track of the `current_char` (start with the first letter `strParam[0]`).
    current_char = strParam[0]
    
    # 3. Keep track of the `count` of how many times we've seen it in a row (start with 1).
    count = 1
    
    # 4. Loop through the string, starting from the SECOND letter (index 1).
    # We must slice the string to start from the second letter!
    for letter in strParam[1:]:
    
    # 5. Inside the loop, if the letter is the SAME as `current_char`, add 1 to `count`.
        if current_char == letter:
            count += 1
    
    # 6. If the letter is DIFFERENT:
    #   a. ADD TO the `answer` string (use +=, not =).
        else:
            answer += str(count) + current_char
    
    #      b. Reset `current_char` to be this new letter.
            current_char = letter
    
    #      c. Reset `count` back to 1.
            count = 1
    
    # 7. (Edge Case): When the loop finishes, we still need to add the very last group to the `answer`!
    answer += str(count) + current_char
    
    # 8. Return `answer`.
    return answer

print(RunLength(input()))
