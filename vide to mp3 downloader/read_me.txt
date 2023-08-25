This is python module created for downloading mp3 from a youtube video

A video has thre part :
1. video 
2. audio
3.codec

My goal is to extract this audio file
For this i have used pytube though youtube authentication api is not supported withthis one can use InstallledAppFlow module for the authenfication . I my self have added it but it requires to used clientSecret.json which is for browser api integration

Its a pretty simple script which uses pytube module methods such as 
getting access to video url 
using filter to get access to audio_file_only()
then downloading it 
i have used exception handling to handle the potential errors which may potentially come such as:
1.video Unavailable
2. video is age restricted which requires authentication to access it. 

Also I you can see their is a shutlin module,
what it does is , it help us to move the downloaded file to a folder 
andos module to make modification in the system
like renaming file feature etc in the system directory.