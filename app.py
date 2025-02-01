# Bits and bytes
import math
from lib.artemethichoperators import ArtemethicOperators as AOP


def main():

    #  01001000 01001001 00100001
    #  010010000100100100100001
    prompt = input("Enter input: ")

    #  Ensure that the input does not contain any spaces
    prompt = binary_to_bits(prompt)

    #  Converting the binary digits to decimal
    prompt = BinaryToDecimal(prompt)

    #  Converting the decimal digits to Hexadecimal
    prompt = DecimalToHexadecimal(prompt)

    print_message()


def binary_to_bits(arg:str):

    """
        *  Reversing the binary digits and storing them in a list
        *  The bits are stored in a list, every 8 binary digits is equal to 1 bit

        *  Param: arg (str)
        *  Return: bits (list)
    """
    # Initializing a list to store the bits
    bits = []

    # Reversing the binary digits 
    x = lambda x: x[::-1]

    # Every 8 binary digits is equal to 1 byte
    for i in range(0, len(arg), 8):

        #  Appending the Binary digits to the list
        bits.append(x(arg[i:i+8]))

    return bits

def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)

    print_message(num % 10)

def BinaryToDecimal(bits:tuple):

        """
            * Converting the binary digits to decimal

            * Param: bits (tuple)
            * Return: dec (list)
        """
        
        dec = []

        #  Converting the binary digits to decimal
        for i in range(0, len(bits)):

            #  Reset the total value
            total = 0

            for j in range(len(bits[i]), 0, -1):
                
                j = j - 1

                #  Calculating the decimal value of the binary digits
                if bits[i][j] == "1":
                    total += int(AOP().Exponentiation(int(bits[i][j]), 2, j))

            dec.append(total)

        return dec

def DecimalToHexadecimal(num:tuple):

    """
        * Converting the decimal digits to Hexadecimal

        * Param: num (tuple)
        * Return: None
    """

    base = 16
    string = "x0"

    symbols = {
        #  Adopted from Google's Gemini
    0: '0', 1: '1', 2: '2', 
    3: '3', 4: '4', 5: '5',
    6: '6', 7: '7', 8: '8', 
    9: '9', 10: 'A', 11: 'B',
    12: 'C', 13: 'D', 14: 'E', 15: 'F'
}
    #  Calculate the remainder of the decimal digits
    for i in range(0, len(num)):

        # Calculate the reminder and Quotient of the decimal digits
        
        string += symbols[AOP().Quotient(num[i], base)] if AOP().Quotient(num[i], base) > 9 else str(AOP().Quotient(num[i], base))
        string += symbols[AOP().Remainder(num[i], base)] if num[i] % base > 9 else str(AOP().Remainder(num[i], base))



        print(string)

def DecimalToASCII(num:tuple):
    
    #  Converting the decimal digits to ASCII

    char= ""
    for i in range(0, len(num)):
        char += chr(num[i])
    
    print(char)


def print_message():
    print(f"Binary:\t Decimal: ")
    print(f"Hexadecimal:\t ASCII:", )

if __name__ == '__main__':
    main()