#TITLE: archives.py
#PURPOSE: Hold past code that may be useful again

=== srtbotFN.py ===
'''
def srtWrite( outfile ):
    outfile.write( '1\n00:00:00,000 --> 00:00:00,000' )
'''

'''
def writeFileAsSRT( infileContent, outfileName ): 
    lineNumber = 0
    #for loop to print the input file line by line
    for lineContent in infileContent:
        endl = re.search( '\n', lineContent ) #endline is at endl.start()
        if endl.start() != 0:
            lineNumber += 1
            writeLineAsSRT( lineNumber, outfileName, lineContent )
#end of FN writeSrtFormat
'''

=== srtbot.py ===
'''
#open and load the input file
trans = open( 'sampleTrans.txt', 'r' )
transLines = trans.readlines() #make a list of all lines
trans.close()
'''

'''
#previously, the for loop was directly in the main file
lineNumber = 0
#for loop to print the input file line by line
for lineContent in transLines:
    endl = re.search( '\n', lineContent ) #the first endline is at x.start()
    if endl.start() != 0:
        lineNumber += 1
        srtbotFN.writeLineAsSRT( lineNumber, srt, lineContent )
'''

'''
#regex sub function
sampleString = "one\ntwo\n\nthree\n\n\nend"
sampleString = re.sub( '\n+', '\n', sampleString )
print( sampleString )
'''

'''
#for loop to print lines 1-4
for lineNumber in range(0,4):
    srt.write( str(lineNumber+1) )
    srt.write( '\n00:00:00,000 --> 00:00:00,000\n' )
    srt.write( 'text\n\n' )
'''

'''
#open the file and automatically close when done
with open('pagehead.section.htm','r') as f:
    output = f.read()
'''