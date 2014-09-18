#! /usr/bin/python 

__author__ = "Haibo Jin"

from sympy.mpmath import mp
import binascii

#exercise 1.3 of information theoretic modeling
#generating random characters without any random number generators

def rand_text():
    """generate random bits of 1kB, using the 8*1024 digits of pi."""
    file_out = open('random.file', 'wb')
    mp.dps = 8 * 1024  + 1 
    #get the 8*1024 digits of pi
    digits = str(mp.pi)[2:]
    #get binary value as ascii
    digits_binary = ''
    for d in digits:
        if d in '01234': digits_binary += '0'
        else: digits_binary += '1'
    #transform to hex as ascii
    hexes = hex(int(digits_binary, 2))[:-1]
    #transform from hex to binary
    binaries = binascii.a2b_hex(hexes[2:])
    file_out.write(binaries)
    file_out.close()

if __name__ == '__main__':
    rand_text()
