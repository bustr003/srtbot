TITLE: README
AUTHOR: Mhealyssah Bustria
DATE WRITTEN: Thu 09 Jul 2020
PURPOSE: Provide information about the srtbot program

PROCEDURE:
1) Paste your transcript into sampleTrans.txt
2) Run srtbot.py
3) Save 'sampleSRT.txt' as a new file with a different name
- e.g, 'mySRT.txt' or 'mySRT.srt'
- You can change the type of your new file from .txt to .srt in either step 3 or 4.
4) Open your new file (e.g, 'mySRT.txt or mySRT.srt')
- You can modify the timestamps and line breaks as needed. 

FILES
0) README
1) srtbot.py
2) srtbotFN.py
3) sampleTrans.txt
4) sampleSRT.txt
5) archives.py 

========= 1) FILE DESCRIPTION: srtbot.py =========
PURPOSE: Take a transcript and write it in .srt format
ASSUMPTIONS:
- The entirety of a given line of text in the transcript file is to be displayed as one subtitle in the video.
- - i.e, No two lines of text in the transcript file are to be displayed at the same time in the video.
- - i.e, Line breaks in individual (longer) subtitles should be added AFTER running the program.
NOTES:
- Extra newline characters from the transcript file will be omitted from the srt format.
- - i.e, Extra newline characters do not need to be removed from the original transcript.
- All timestamps will be set to 00:00:00,000.
- - i.e, Timestamps will need to be updated manually after running the program.
========= end of srtbot.py description =========

========= 2) FILE DESCRIPTION: srtbotFN.py =========
List of functions
1: getFileLines( infileName )
2: writeLineAsSRT( lineNumber, outfile, lineContent )
3: writeFileAsSRT( fileContent, outfile )
========= end of srtbotFN.py description =========

========= 3) FILE DESCRIPTION: sampleTrans.txt =========
- Paste the transcript into this file.
- Each line is one subtitle.
- The program will remove extra endlines,
- - so the user does not need to do so beforehand.
========= end of sampleTrans description =========

========= 4) FILE DESCRIPTION: sampleSRT.txt =========
- The srtbot program will overrite this file.
- Here, the transcript will appear in SRT format.
- If some of the subtitles are too long to appear on a single line in the video,
- - extra line breaks can be added to individual subtitles
- - AFTER running the srtbot program.

EXAMPLE:
=== STEP ONE: run the srtbot program ===
1
00:00:00,000 --> 00:00:00,00
This subtitle is very very very very very very very extremely super super super super duper loooonggggggg
=== end of step one ===

=== STEP TWO: manually add line breaks to long subtitles ===
1
00:00:00,000 --> 00:00:00,00
This subtitle is very very very
very very very very extremely super
super super super duper loooonggggggg
=== end of step two ===
========= end of sampleSRT.txt description =========

========= 5) FILE DESCRIPTION: archives.py =========
- past code that is no longer used in the final program
========= end of archives.py description =========