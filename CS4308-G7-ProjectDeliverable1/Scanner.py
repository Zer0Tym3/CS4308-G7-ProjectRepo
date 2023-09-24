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
    if '"' in line:
        print("dasdasd")



tA = False
text = 'display "Value of x: ", x'
start = text.index('"')
end = text.index('"', start + 1)
substring = '"' + text[start + 1:end] + '"'
sString1 = text.split(' ')[0]
endText = (text[end+1:])
try:
    sList2 = endText.split(' ')
    tA = True
except:
    print("No Tokens after literal")
print(sString1, ', ', substring)
if tA == True:
    print(sList2)
print(len(sList2))

# sString1 ~~ to Token
# subString ~~ to Token
#


# Comment to test push on Git: Phillip
# Comment Armando Ortiz
# Comment Zach Morning