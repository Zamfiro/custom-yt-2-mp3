import ffmpeg
import yt_dlp as ytdl 
import os
import time

start_time = time.time()

def download_video(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'audioonly': 'true',
        'audioformat': 'mp3',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'verbose': 'true',
        'preset': 'veryfast',
    }
    with ytdl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def convert_to_mp3(files):
    for file in files:
        input_file = file
        output_file = file.replace('.webm', '.mp3')
        ffmpeg.input(f'downloads/{input_file}').output(f'downloads/{output_file}', bitrate='320k').run()
        os.remove(f'downloads/{input_file}')

read_file = open('links.txt', 'r')
links = read_file.readlines()
read_file.close()

for link in links:
    download_video(link)

files = os.listdir('downloads')
convert_to_mp3(files)

print(f'--- {(time.time() - start_time)} seconds ---')



    

        
 