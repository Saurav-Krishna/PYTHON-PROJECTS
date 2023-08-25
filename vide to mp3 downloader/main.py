import os
import shutil

from pytube import YouTube


def url_to_mp3(video_url: str):
    video_file = YouTube(video_url).streams.get_audio_only()
    video_file.download()

    mp4_name = video_file.default_filename
    mp3_name = mp4_name.replace(".mp4", ".mp3")
    os.rename(mp4_name, mp3_name) # rename mp4 to mp3
#! calling os to rename the file in path
    shutil.move(mp3_name, "./audio")
    #? to move the file in the folder

def main():
        try:
            input_url = input("enter the URL to convert:")
            url_to_mp3(video_url=input_url)
            print("Fineshed ")
        except Exception as e:
            print(f"Something went wrong : {e}")
            
        

if __name__ == "__main__":
    main()