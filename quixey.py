
import re
import sys

# Mapping between numbers and characters
CODES = {'0': '0',
         '1': '1',
         '2': 'abc',
         '3': 'def',
         '4': 'ghi', 
         '5': 'jkl',
         '6': 'mno',
         '7': 'pqrs',
         '8': 'tuv',
         '9': 'wxyz'}

def tel_words_rec(num, res = ""):
    """
    Recursive solution:
    Returns a list of letter combinations that can represent the given telephone number.
    
    num: string of numbers
    res: string that accumulates each combination
    return: list of strings
    """
    if not num:
        return [res]

    words = []
    fst, rst = num[0], num[1:]
    for character in CODES[fst]:
        words += tel_words_rec(rst, res + character)
    return words
    
def tel_words_iter(num):
    """
    Iterative solution:
    Returns a list of letter combinations that can represent the given telephone number.
    
    num: string of numbers
    return: list of strings
    """
    words = [letter for letter in CODES[num[0]]]
    for digit in num[1:]:
        letters = CODES[digit]
        words = [ w+l for w in words for l in letters]
    return words
    
#--------------------------------
# Main code: reads file, checks input
#
test_cases = open(sys.argv[1], 'r')
for line in test_cases:
    # ignore test if it is an empty line
    if line:
        assert re.match(r'^[0-9]{7}$', line), "Input should be a 7 digit number"
        line = line.split()[0]        
        ls = tel_words_iter(line)
        print ','.join(ls)
test_cases.close()

