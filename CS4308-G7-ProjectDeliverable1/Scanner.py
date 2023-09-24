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


def open_file(self):
    try:
        self.file = open(self.file_name, "r")
    except FileNotFoundError:
        print("Unable to open file. Please Try Again.")
        SystemExit(2)

def is_comment(self, line):
    #Checking To See If A Line Is A Comment (Specifically Stating with the HashTag#)
    return line.strip().startswitch('#')

def tokenized_line(self, line):
    #Sets a Tokened line into key statements such as: Identifiers, operators, and or specialized characters.
    tokens = line.split()
    for token in tokens:
        #Validates for if it is one of the previously stated keywords (We can add more keywords if needed)
        if token in ["print", "if","else", "while"]:
            self.token_list.append(("Keyword", token))
        #Checks to seee if any identifiers exist.
        elif token.isidentifier():
            self.token_list.append(("Identifier", token))
            #Check for operators and special characters
        elif token in ["+", "-", "*", "/", "=", "==", ",", "."]:
            self.token_list.append(("Operator/SpecialChar", token))

    def scan(self):
        self.open_file()
        for line in self.file:
            if not self.is_comment(line) and line.strip():
                self.tokenize_line(line)
        self.file.close()

    def print_tokens(self):
        for token in self.token_list:
            print(token)

    def export_to_json(self, output_file):
        with open(output_file, 'w') as json_file:
            json.dump(self.token_list, json_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    scanner = Scanner(file_name)
    scanner.scan()
    scanner.print_tokens()
    scanner.export_to_json("output.json")


    



# sString1 ~~ to Token
# subString ~~ to Token
#


# Comment to test push on Git: Phillip
# Comment Armando Ortiz
# Comment Zach Morning 