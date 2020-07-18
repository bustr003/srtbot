'''
TITLE srtbot.py
AUTHOR: Mhealyssah Bustria
DATE CREATED: Wed 08 Jul 2020
PURPOSE: Take a transcript and write it in .srt format
PROCEDURE:
1) Paste your transcript into sampleTrans.txt
2) Run srtbot.py
3) Save 'sampleSRT.txt' as a new file with a different name
- e.g, 'mySRT.txt' or 'mySRT.srt'
- You can change the type of your new file from .txt to .srt in either step 3 or 4.
4) Open your new file (e.g, 'mySRT.txt or mySRT.srt')
- You can modify the timestamps and line breaks as needed. 
see 'README.txt' for ASSUMPTIONS and NOTES.
'''

#OPENING STATEMENTS
program = "SRTbot"
print( '===' + program + '===' )

#MODULES
import time as t
#custom modules
import srtbotFN as fn

#start timer
t0 = t.time()

#files to use
infile = 'sampleTrans.txt'
outfile = 'sampleSRT.txt'

#open the input file (the transcript) and create a list to hold each line
print( 'transcript will be read from', infile )
transLines = fn.getFileLines( infile )

#open the output file (to hold the transcript in SRT format)
print( 'SRT will be written to', outfile )
srt = open( outfile, 'w' ) #'w' means overwrite existing content

#write the transcript in SRT format
fn.writeFileAsSRT( transLines, srt )

srt.close() #close the output file
print( 'DONE. check the re-written', outfile )

#ENDING STATEMENTS
t1 = t.time()
print( 'time to run: ', t1-t0, ' seconds' )

print( '===' + program + ' end===' )
#EOF srtbot.py