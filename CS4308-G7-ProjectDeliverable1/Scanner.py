from Token import *
import json
import sys


# Group 7: Zach Morning, Phillip Ngo, David Nguyen, Armando Ortiz


def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res
# filterAndLex attempted to open a file, lex and tokenize desired text, and filter out anything else.
def filterAndLex(fName):
    try:
        file = open(fName, 'r')
    except:
        print("Unable to open file, please try again.", fName)
        exit(2)
    Comment = False
    lineList = []
    for line in file:
        lineTokens = []
        if '"' in line:
            tA = False
            start = line.index('"')
            end = line.index('"', start + 1)
            substring = '"' + line[start + 1:end] + '"'
            sString1 = line.split(' ')[0]
            endText = (line[end + 1:])
            try:
                sList2 = endText.split(' ')
                tA = True
            except:
                if tA == True:
                    lineTokens.append(sList2)
            lineTokens.append((sString1))
            lineTokens.append((substring))
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
        lineList[loopCount] = remove_items(line, '')
        loopCount += 1

    loopCount = 0
    for line in lineList:
        if '\n' in line[len(line) - 1]:
            mStr = line[len(line) - 1]
            mStr = mStr[:-1]
            line[len(line) - 1] = mStr
            lineList[loopCount] = line
        loopCount += 1

    loopCount = 0
    for line in lineList:
        if '//' in line:
            line = line[:line.index('//')]
            lineList[loopCount] = line
        loopCount += 1


    currentLineNum = 0
    while currentLineNum < len(lineList):
        if lineList[currentLineNum][0] == '':
            lineList.remove(lineList[currentLineNum])
        else:
            currentLineNum += 1

    lineList = list(filter(None, lineList))

    return lineList


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

if __name__ == "__main__":
    sysArgv = sys.argv

    ItemList = filterAndLex(sysArgv[1])

    finalTokenList = []
    mDict = {}


    for Items in ItemList:
        for tItem in Items:
            if tItem in tokenList["keywords"]:
                newToken = Token('keywords', tokenList["keywords"][tItem], tItem)
            elif tItem in tokenList["identifiers"]:
                newToken = Token('identifiers', tokenList["identifiers"][tItem], tItem)
            elif tItem in tokenList["operators"]:
                newToken = Token('operators', tokenList["operators"][tItem], tItem)
            elif tItem in tokenList ["specialSymbols"]:
                newToken = Token('specialSymbols', tokenList["specialSymbols"][tItem], tItem)
            elif tItem[0] == '"' and tItem[len (tItem) - 1] == '"':
                newToken = Token('literals', 600, tItem) 
            elif isfloat (tItem):
                newToken = Token('literals', 600, tItem) 
            else:
                newToken = Token('UNKNOWN', 1200, tItem) 
                
            finalTokenList.append(newToken)
            print("New Token created: ", newToken.getData())

        newToken = Token('EndOfStatement', 1000, 'EOS') 
        finalTokenList.append (newToken)
        print("New Token created: ", newToken.getData())


    jsonFile = open ("OutputTokens.json", "w")

    loopCounter = 0
    for Token in finalTokenList:
        tokenStr = "Token_" + loopCounter.__str__()
        mDict.update({tokenStr: {}})
        loopCounter += 1

    loopCounter = 0
    for Token in finalTokenList:
        tokenData = Token.getData()
        lst = ['Type', tokenData[0], 'id', tokenData[1], 'value', tokenData[2]]
        newList = Convert(lst)

        tokenStr = "Token_" + loopCounter.__str__()

        mDict[tokenStr].update(newList)
        loopCounter += 1

    json_object = json.dumps(mDict, indent = 4)
    jsonFile.write(json_object)
