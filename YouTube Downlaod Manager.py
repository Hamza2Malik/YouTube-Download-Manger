from pytube import YouTube
from colorama import init, Fore

def on_complete(stream, filepath):
	print('download complete')
	print(filepath)

def on_progress(stream, chunk, bytes_remaining):
	progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100),2)}%'
	print(progress_string)

init()
link = input('Youtube link: ')
video_object = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)

# for stream in video_object.streams:
#     print(stream)
print(Fore.RED + f'title:  \033[39m {video_object.title}')
print(Fore.RED + f'length: \033[39m {round(video_object.length / 60,2)} minutes')
print(Fore.RED + f'views:  \033[39m {video_object.views / 1000000} million')
print(Fore.RED + f'author: \033[39m {video_object.author}')

print(
	Fore.RED + 'download:' + 
	Fore.GREEN + '(b)est \033[39m|' + 
	Fore.YELLOW + '(w)orst \033[39m|' + 
	Fore.BLUE + '(a)udio \033[39m| (e)xit')
download_choice = input('choice: ')

if (download_choice== 'b'):
    video_object.streams.get_highest_resolution().download()
elif (download_choice=='w'):
    video_object.streams.get_lowest_resolution().download()
elif( download_choice== 'a'):
    video_object.streams.get_audio_only().download()