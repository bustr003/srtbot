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
- fileLines
'''
def getFileLines( infileName ):
    infile = open( infileName, 'r' )
    fileLines = infile.readlines() #make a list of all lines
    infile.close()
    return fileLines
#end of FN getFileLines

'''
FN2: writeLine
PURPOSE: print a line in srt format
PARAMETERS:
- lineNumber: the number of the line in the transcript
- outfile: the file to write to
- lineContent: one line of the transcript
'''
def writeLineAsSRT( lineNumber, outfile, lineContent ):
    outfile.write( str(lineNumber) ) #line number
    outfile.write( '\n00:00:00,000 --> 00:00:00,000\n' ) #timestamp
    outfile.write( lineContent )
    outfile.write( '\n' )
#end of FN writeLines

'''
FN3: writeSrtFormat
PURPOSE: print a transcript in srt format
PARAMETERS:
- lineNumber: the number of the line in the transcript
- outfile: the file to write to
- lineContent: one line of the transcript
'''
def writeFileAsSRT( infileContent, outfile ): 
    lineNumber = 0
    #for loop to print the input file line by line
    for lineContent in infileContent:
        line_end = re.search( '\Z|\n', lineContent ) #end of string is at string_end.start()
        
        #if the line is not just a blank line
        if line_end.start() != 0:
            lineNumber += 1
            writeLineAsSRT( lineNumber, outfile, lineContent )

#end of FN writeSrtFormat

#EOF srtbotFN.py