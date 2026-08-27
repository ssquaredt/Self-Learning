def BracketMatcher(strParam):
# Question:
# Have the function BracketMatcher (str) take the str parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for. Otherwise return 0. 
# For example: if str is "(hello (world))", then the output should be 1, but if str is "((hello (world))" the the output should be 0 because the brackets do not correctly match up. 
# Only "(" and ")" will be used as brackets. If str contains no brackets return 1.
  
    # intialize count = 0 which will be used to calculate the occurence
    count = 0

    # Loop through each character of the string input
    for i in strParam:
        # if open bracket detected, count + 1
        if i == "(":
            count = count + 1
        # if close bracket detected, count - 1, show correctly matched
        elif i == ")":
            count = count - 1

        # if close bracket detected before open bracket, return 0
        if count < 0:
            return 0

    # if count = 0, show every open bracket has its own respected close bracket and matched, return 1
    if count == 0:
        return 1
    # else, the brackets do not match so return 0
    else:
        return 0    

print(BracketMatcher(input()))