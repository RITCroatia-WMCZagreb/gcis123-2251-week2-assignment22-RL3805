'''
@ASSESSME.USERID: userID
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''

STRING_GLOBAL: str="Hello World"
INT_GLOBAL: int=1215
FLOAT_GLOBAL: float=21.43

def print_param():
    print(STRING_GLOBAL)
    print(INT_GLOBAL)
    print(FLOAT_GLOBAL)

def print_local():
    a = "local variable."
    print(a)

def print_which():
    STRING_GLOBAL: int=123
    print(STRING_GLOBAL)

def main():
    print_param()
    print_local()
    print_which()


if __name__ == "__main__":
    main()