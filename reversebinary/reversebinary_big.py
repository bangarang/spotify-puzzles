import sys
 
def reverseBinary():
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
        lines[i] = toDecimal(reverseString(toBinary(int(lines[i].replace('\n','')))))
    return lines

def reverseBinarySingle():
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
