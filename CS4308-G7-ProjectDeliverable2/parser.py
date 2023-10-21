from Scanner import *
import json
from itertools import islice
from Scanner import *
from Token import *
import json

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = str()
        self.right = str()
        self.count = 0
        self.lineCount = 0
        self.last_data = str()

    def UpdateCounts(self, lineCount):
        self.data = "Line: " + str(lineCount)
        lineCount += 1
        if self.left is not str():
            self.left.UpdateCounts(lineCount)

    def PrintTree(self):
        print(self.data)
        if self.right is not str():
            self.right.PrintTree()
        if self.left is not str():
            self.left.PrintTree()

    def iterate(self, num):
        if self.count != 0:
            if self.left is not str():
                self.left.iterate(num)
            num = num + 1
        return num

    def insert(self, data):
        if data == "EOS":
            if not self.left:
                self.left = TreeNode(self.count+1)
                self.count += 1
            else:
                self.left.insert(data)
        elif not self.right:
            self.right = TreeNode(data)
        else:
            self.right.insert(data)
        
def GetNextToken(countTk, tokenList):
    countTk += 1
    return tokenList[countTk]

if __name__ == '__main__':
    sysArgv = sys.argv

    tokenList = GenerateTokenList(sysArgv[1])

    root = TreeNode(0)
    countIterate = -1
    for item in tokenList:
        root.insert(GetNextToken(countIterate, tokenList).value)
        countIterate = countIterate+1

    root.UpdateCounts(0)
    root.PrintTree()

