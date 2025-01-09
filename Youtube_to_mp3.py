import os
from pytubefix import YouTube
import subprocess

def youtube_to_mp3(youtube_url, output_path="output"):
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)

        # Download YouTube video
        yt = YouTube(youtube_url)
        video = yt.streams.filter(only_audio=True).order_by('abr').last()
        download_path = video.download(output_path)

        # Convert to MP3 using ffmpeg
        base, ext = os.path.splitext(download_path)
        mp3_path = f"{base}.mp3"

        # Only convert if the file is not already in MP3 format
        if ext.lower() != ".mp3":
            subprocess.run(["ffmpeg", "-i", download_path, "-q:a", "0", "-map", "a", mp3_path])
            os.remove(download_path)  # Clean up the original file
        else:
            mp3_path = download_path

        print(f"MP3 saved at {mp3_path}")
    except Exception as e:
        print(f"Error: {e}")
continue_loop=True;
while(continue_loop==True):
    choice =input("""
1. Download
2. Exit 
""")
    if choice == "1":
        youtube_to_mp3(input("Enter the YouTube video URL: "))

    elif choice == "2":
        continue_loop=False
    



