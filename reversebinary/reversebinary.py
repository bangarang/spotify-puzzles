__author__ = "Alex Rock"
__email__ = "hi@lxrck.com"
__date__ = "2013-9-9"

import sys
 
def reverseBinary():
    line = sys.stdin.readline()
    output = toDecimal(reverseString(toBinary(int(line.replace('\n','')))))
    return output
 
def toBinary(i):
    if i == 0:
        return "0"
    part = ''
    while i:
        if i & 1 == 1:
            part = "1" + part
        else:
            part = "0" + part
        i >>= 1
    return part

def reverseString(i):
	return i[::-1]

def toDecimal(i):
	return int(str(i),2)

def main():
    print reverseBinary()
 
if __name__ == '__main__':
    main()