'''
TITLE srtbotFN.py
AUTHOR: Mhealyssah Bustria
DATE CREATED: Wed 08 Jul 2020
List of functions
1: getFileLines( infileName )
2: writeLineAsSRT( lineNumber, outfile, lineContent )
3: writeFileAsSRT( fileContent, outfile )
'''

import re #regular expressions

'''
FN1: getFileLines
PURPOSE: open a file and make a list of all lines
PARAMETERS:
- infileName: the name of the file to open
RETURN VALUES:
- fileLines: a list where each element is a line from the file
'''
def getFileLines( infileName ):
    infile = open( infileName, 'r' )
    fileLines = infile.readlines() #make a list of all lines
    infile.close()
    return fileLines
#end of FN getFileLines

'''
FN2: writeLineAsSRT
PURPOSE: write a line in srt format
PARAMETERS:
- lineNumber: the number of the line in the transcript
- outfile: the file to write to
- lineContent: one line of the transcript
'''
def writeLineAsSRT( lineNumber, outfile, lineContent ):
    outfile.write( str(lineNumber) ) #line number == subtitle number
    outfile.write( '\n00:00:00,000 --> 00:00:00,000\n' ) #timestamp HH:MM:SS,mmm
    outfile.write( lineContent ) #the text to be displayed as a subtitle
    outfile.write( '\n' )
#end of FN writeLineAsSRT

'''
FN3: writeFileAsSRT
PURPOSE: write a transcript in srt format
PARAMETERS:
- outfile: the file to write to
- infileContent: a list of each line in the input file
'''
def writeFileAsSRT( infileContent, outfile ): 
    lineNumber = 0 #the number of the line in the transcript
    #for loop to print the input file line by line
    for lineContent in infileContent:
        endl = re.search( '\n', lineContent ) #endline is at endl.start()
        if endl.start() != 0:
            lineNumber += 1
            writeLineAsSRT( lineNumber, outfile, lineContent )
#end of FN writeFileAsSRT

#EOF srtbot.py
