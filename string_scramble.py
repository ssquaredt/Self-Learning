def StringScramble(str1, str2):
    # Question:
    # Have the function StringScramble(str1, str2) take both parameters being passed
    # return the string true if a portion of str1 characters can be rearranged to match str2, otherwise return the string false. 
    # For example: if str1 is "rkqodlw" and str2 is "world" the output should return true. 

    # Step 1: Pseudocode (The "Scrabble Tiles" method)
    # 1. Convert `str1` into a list of characters (our pool of Scrabble tiles).
    char_list = list(str1)

    # 2. Loop through every letter in `str2` (the word we want to spell).
    for letter in str2:
    
    # 3. Inside the loop, check IF the letter is IN our `tile_pool`.
    # 4. If it IS in the pool:
        # a. Remove it from the pool so we don't use the same tile twice!
        if letter in char_list:
            char_list.remove(letter)
    
    # 5. If it is NOT in the pool:
        # a. We can't spell the word! Return the string "false" immediately.
        else:
            return "false"
    
    # 6. If the loop finishes checking every letter successfully, return "true".
    return "true"

print(StringScramble(input(), input()))
