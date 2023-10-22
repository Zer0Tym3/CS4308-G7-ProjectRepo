# from itertools import islice
from Scanner import *
# from Token import *
# import json


class TreeNode:
    def __init__(self, data):  # Constructor for TreeNode Class, Stores Data, Left & Right Pointers, and its own count.
        self.data = data
        self.left = str()
        self.right = str()
        self.count = 0
        self.lineCount = 0
        self.last_data = str()

    def updateCounts(self, lineCount):  # Update Counts function correctly iterates the line counts for display.
        self.data = "Line #: " + str(lineCount)
        lineCount += 1
        if self.left is not str():
            self.left.updateCounts(lineCount)

    def printTree(self):  # Self-explanatory, Prints the tree
        print(self.data)
        if self.right is not str():
            self.right.printTree()
        if self.left is not str():
            self.left.printTree()

    def iterate(self, num):  # Iterates through the tokens for use in the insert function
        if self.count != 0:
            if self.left is not str():
                self.left.iterate(num)
            num = num + 1
        return num

    def insert(self, data):  # Inserts a token from the list 
        iterations = self.iterate(0)
        if iterations > 0:
            self.left.insert(data)
        else:
            if data == "EOS":  # Filters out the EOS (EndOfStatement) Tokens
                if self.left is not str():
                    self.left.insert(self.count + 1)
                else:
                    self.left = TreeNode(self.count + 1)
                self.count += 1
            elif self.right is not str():
                self.right.insert(data)
            elif self.right is str():
                self.right = TreeNode(data)


tokenCount = -1


# noinspection PyShadowingNames
def getNextToken(tokenCount, tokenList):
    tokenCount += 1
    return tokenList[tokenCount]


if __name__ == '__main__':
    sysArgv = sys.argv

    tokenList = GenerateTokenList(sysArgv[1])

    rootNode = TreeNode(0)
    countIterate = -1
    for item in tokenList:
        rootNode.insert(getNextToken(countIterate, tokenList).value)
        countIterate = countIterate + 1

    rootNode.updateCounts(0)
    rootNode.printTree()
