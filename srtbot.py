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

import srtbotFN

#open the output file (to hold the transcript in SRT format)
srt = open( 'sampleSRT.txt', 'w' ) #'w' means overwrite existing content

#open the input file (the transcript)
#create a list to hold each line
transLines = srtbotFN.getFileLines( 'sampleTrans.txt' )

srtbotFN.writeFileAsSRT( transLines, srt ) #write the transcript in SRT format

srt.close() #close the output file
print( 'done. check the re-written \'sampleSRT.txt.\'' )
#EOF srtbot.py