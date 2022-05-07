from __future__ import unicode_literals
import youtube_dl
import os

#Define the video URL
playlist_url="https://youtu.be/YZPFbnk_RS0"
try:
        #Download data and config
        meta = youtube_dl.YoutubeDL().extract_info(url=playlist_url,download=False)
        filename = f"{meta['title']}.mp3"
        download_options = {
                'format': 'bestaudio/best',
                'outtmpl': filename,
                'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                        }]
                }
        # Song Directory
        if not os.path.exists('Songs'):
                os.mkdir('Songs')
        else:
                os.chdir('Songs')
        # Download Songs
        with youtube_dl.YoutubeDL(download_options) as dl:
                dl.download([meta['webpage_url']])
except:
        print("Unabe to extract/download the video")


