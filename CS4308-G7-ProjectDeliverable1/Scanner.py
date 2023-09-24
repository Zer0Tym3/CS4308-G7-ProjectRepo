from Token import *
import json
import sys


# Group 7: Zach Morning, Phillip Ngo, David Nguyen, Armando Ortiz

# filterAndLex attempted to open a file, lex and tokenize desired text, and filter out anything else.
def filterAndLex(fileN):
    try:
        file = open(fileN, "r")
    except:
        print("Unable to open file, please try again.")
        exit(2)
    comment = False
    lines = []
    for line in file:
        lineTokens = []


text = 'import "tests.scl"'
start = text.index('"')
end = text.index('"', start + 1)
substring = text[start + 1:end]
print(substring)

# Comment to test push on Git: Phillip
# Comment Armando Ortiz
