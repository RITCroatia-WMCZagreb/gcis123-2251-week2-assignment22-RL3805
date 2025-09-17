'''
@ASSESSME.USERID: rl3805
@ASSESSME.AUTHOR: Roko Lovrecek
@ASSESSME.DESCRIPTION: Assignment 2.2
@ASSESSME.ANALYZE: YES
'''

def add_chars(char1,char2):
    val1 = ord(char1)
    val2 = ord(char2)

    sum = val1 + val2
    print("Sum of a and b = "+str(sum)+ "\nCharacter = " + chr(sum)+"\n")

    


def subtract_chars(c1,c2):
    value1 = ord(c1)
    value2 = ord(c2)

    subtraction = value1 - value2
    print("Difference of "+c1+" and "+c2+" = "+str(subtraction)+ "\nCharacter = " + chr(subtraction)+"\n")


def main():
    add_chars("a","b")
    subtract_chars("b","a")


if __name__ == "__main__":
    main()


#odd characters or nothing appears when the sum exceeds the range of ASCII(0-127)
#ord() and chr() are only able to hold one character; if more are entered syntax error occurs