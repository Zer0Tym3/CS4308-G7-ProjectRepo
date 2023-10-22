import json
import sys


# Group 7: Zach Morning, Phillip Ngo, David Nguyen, Armando Ortiz
# Final Scanner Build

def remove_items(test_list, item):
    return [i for i in test_list if i != item]


# filterAndLex attempted to open a file, lex and tokenize desired text, and filter out anything else.
# noinspection PyBroadException
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
            sString1 = (line[:start - 1])

            if sString1[0] == ' ':
                sList1 = sString1.split(' ')
                correctS = (sList1[sList1.__len__() - 1])
                lineTokens.append(correctS)
            else:
                lineTokens.append(sString1)
            lineTokens.append(substring)
            endText = (line[end + 1:])
            try:
                sList2 = endText.split(' ')
                if tA is False:
                    tA = True
            except:
                continue
            if tA is True:
                for s in sList2:
                    lineTokens.append(s)

            if '\n' in lineTokens:
                lineTokens.remove('\n')
            lineList.append(lineTokens)
            continue
        lineTokens = line.split(' ')

        if "/*" in line:
            Comment = True

        if not Comment:
            lineList.append(lineTokens)

        if "*/" in line:
            Comment = False

    loopCount = 0
    for line in lineList:
        lineList[loopCount] = remove_items(line, '')
        loopCount += 1

    loopCount = 0
    for line in lineList:  # \n filter
        if '\n' in line[len(line) - 1]:
            mStr = line[len(line) - 1]
            mStr = mStr[:-1]
            line[len(line) - 1] = mStr
            lineList[loopCount] = line
        loopCount += 1

    loopCount = 0
    for line in lineList:  # Line Comment Filter
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
    return dict(zip(a[::2], a[1::2]))


def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}


# noinspection PyUnusedLocal
def GenerateTokenList(file):
    from Token import Token
    from Token import tokenList

    sysArgv = sys.argv

    tokenListUsed = tokenList

    ItemList = filterAndLex(sysArgv[1])

    finalTokenList = []
    mDict = {}

    for Items in ItemList:
        for tItem in Items:
            if "\n" in tItem:
                tItem = tItem[0]
            if tItem in tokenList["keywords"]:
                newToken = Token('keywords', tokenListUsed["keywords"][tItem], tItem)
            elif tItem in tokenList["identifiers"]:
                newToken = Token('identifiers', tokenListUsed["identifiers"][tItem], tItem)
            elif tItem in tokenList["operators"]:
                newToken = Token('operators', tokenListUsed["operators"][tItem], tItem)
            elif tItem in tokenList["specialSymbols"]:
                newToken = Token('specialSymbols', tokenListUsed["specialSymbols"][tItem], tItem)
            elif tItem[0] == '"' and tItem[len(tItem) - 1] == '"':
                newToken = Token('literals', 600, tItem)
            elif isfloat(tItem):
                newToken = Token('literals', 600, tItem)
            else:
                newToken = Token('UNKNOWN', 1200, tItem)

            finalTokenList.append(newToken)
            print("New Token created: ", newToken.getData())

        newToken = Token('EndOfStatement', 1000, 'EOS')
        finalTokenList.append(newToken)
        print("New Token created: ", newToken.getData())

    jsonFile = open("OutputTokens.json", "w")

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

    json_object = json.dumps(mDict, indent=4)
    jsonFile.write(json_object)

    return finalTokenList
