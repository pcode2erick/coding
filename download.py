from __future__ import unicode_literals
import youtube_dl
import os
from sys import argv

#Download data and config
playlist_url =["https://www.youtube.com/watch?v=wyu8UhV9R_M"]
download_options = {
	'format': 'bestaudio/best',
	'outtmpl': '%(title)s.%(ext)s',
	'nocheckcertificate': True,
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
}
# Song Directory
if not os.path.exists('Songs'):
	os.mkdir('Songs')
else:
	os.chdir('Songs')

# Download Songs
with youtube_dl.YoutubeDL(download_options) as dl:
        for song_url in playlist_url:
                dl.download([song_url])
