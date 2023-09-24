from Token import *
import json
import sys


# Group 7: Zach Morning, Phillip Ngo, David Nguyen, Armando Ortiz

#Scanner Class Created For The Language Processing 
class Scanner: 
    def __init__(self,file_name):
        self.file.name = file_name
        self.token_list = []
        pass

# filterAndLex attempted to open a file, lex and tokenize desired text, and filter out anything else.
def filterAndLex(File_name):
    try:
        file = open(File_name, 'r')
    except:
        print("Unable to open file, please try again.", File_name)
        exit(2)


    Comment = False
    lineList = []

    for line in file:
        lineTokens = []

        if '"' in line:
            splitLocation = line.find('"')
            beforeStr = line[:splitLocation]
            afterStr = line[splitLocation:]
            secondSplitLocation = splitLocation + afterStr[1:].find('"') + 1
            strStatement = line[splitLocation:secondSplitLocation + 1]
            afterStr = line[secondSplitLocation + 1:]

            beforestatementTokens = beforeStr.split(' ')
            for token in beforestatementTokens:
                lineTokens.append (token)

            lineTokens.append(strStatement)

            if afterStr != '\n':
                afterStatementTokens = afterStr.split(' ')
                for token in afterStatementTokens:
                    lineTokens.append (token)


            lineList.append(lineTokens)
            continue


        if '^' in line:
            splitLocation = line.find('^')
            beforeStr = line[:splitLocation]
            afterStr = line[splitLocation:]
            secondSplitLocation = splitLocation + afterStr[1:].find('^') + 1
            strStatement = line[splitLocation:secondSplitLocation + 1]
            afterStr = line[secondSplitLocation + 1:]

            beforestatementTokens = beforeStr.split(' ')
            for token in beforestatementTokens:
                lineTokens.append (token)

            lineTokens.append(strStatement)

            if afterStr != '\n':
                afterStatementTokens = afterStr.split(' ')
                for token in afterStatementTokens:
                    lineTokens.append (token)


            lineList.append(lineTokens)
            continue


        if '<' in line:
            splitLocation = line.find('<')
            beforeStr = line[:splitLocation]
            afterStr = line[splitLocation:]
            secondSplitLocation = splitLocation + afterStr[1:].find('<') + 1
            strStatement = line[splitLocation:secondSplitLocation + 1]
            afterStr = line[secondSplitLocation + 1:]

            beforestatementTokens = beforeStr.split(' ')
            for token in beforestatementTokens:
                lineTokens.append (token)

            lineTokens.append(strStatement)

            if afterStr != '\n':
                afterStatementTokens = afterStr.split(' ')
                for token in afterStatementTokens:
                    lineTokens.append (token)


            lineList.append(lineTokens)
            continue


        lineTokens = line.split(' ')

        commentStart = "/*"
        commentEnd = "*/"

        if commentStart in line:
            Comment = True

        if not Comment:
            lineList.append(lineTokens)

        if commentEnd in line:
            Comment = False

    loopCount = 0
    for line in lineList:
        lineList[loopCount] 



tA = False
text = 'Import "scl.h"'
"""
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
print(len(sList2))"""


splitLocation = text.find('^')
beforeStr = text[:splitLocation]
afterStr = text[splitLocation:]
secondSplitLocation = splitLocation + afterStr[1:].find('^') + 1
strStatement = text[splitLocation:secondSplitLocation + 1]
afterStr = text[secondSplitLocation + 1:]
