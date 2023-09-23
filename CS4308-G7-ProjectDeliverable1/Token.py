tokenList = {
    "keywords": {
        'import': 0,
        'implementation': 1,
        'function': 2,
        'main': 3,
        'return': 4,
        'type': 5,
        'integer': 6,
        'double': 7,
        'char': 8,
        'num': 9,
        'is': 10,
        'variables': 11,
        'define': 12,
        'of': 13,
        'begin': 14,
        'display': 15,
        'set': 16,
        'exit': 17,
        'endfun': 18,
        'symbol': 19,
        'end': 20,
        'input': 21,
        'structures': 22,
        'pointer': 23,
        'head': 24,
        'last': 25,
        'NULL': 26,
        'ChNode': 27,
        'using': 28,
        'reverse': 29,
        'while': 30,
        'endWhile': 31,
        'call': 32,
        'constants': 33,
        'float': 34,
        'array': 35,
        'for': 36,
        'to': 37,
        'do': 38,
        'endfor': 39
    },
    "identifiers": {
        'x': 100,
        'r': 101,
        'area': 102,
        'cir': 103,
        'pchar': 104,
        'j': 105,
        'N': 106,
        'sum': 107,
        'ave': 108,
        'svalue': 109,
        'num': 110,
        'varr': 111,
        'varr[j]': 212
    },
    "operators": {
        '+': 200,
        '-': 201,
        '*': 202,
        '/': 203,
        '^': 204,
        '>': 205,
        '<': 206,
        '"': 207,
        '_': 208,
        'add': 209
    },
    "specialSymbols": {
        ',': 300,
        '.': 301
    }
}

class Token:
    def __init__(self, type, id, value):
        self.type = type
        self.id = id
        self.value = value
    def getData(self):
        return [self.type,self.id,self.value]