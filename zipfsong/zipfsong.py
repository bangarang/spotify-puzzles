import sys

def read_in():
    lines = sys.stdin.readlines()

    first = lines[0].split()

    totalTracks = int(first[0])
    outputNumber = int(first[1])

    qualityArray = []

    for i in range(1,totalTracks+1):
        lines[i] = lines[i].replace('\n','')
        currentLine = lines[i].split()

        frequency = int(currentLine[0])
        quality = i * frequency
        tempTrack = [currentLine[1], quality ]
        qualityArray.append( tempTrack )

    out = sorted(qualityArray, compare_columns)


    for x in range(0, outputNumber):
        temp = out[x]
        print temp[0]

def compare_columns(a, b):
    # sort on ascending index 0, descending index 2
    return cmp(b[1], a[1])

    
def main():
    read_in()

if __name__ == '__main__':
    main()