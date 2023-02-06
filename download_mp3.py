from pytube import YouTube
from pytube import Playlist
import os

#user input for URL
playlist = 'playlist'

user_input = (str(input("Enter URL of Playlist or Video Here: \n>>")))
if playlist in user_input:
    pl = Playlist(user_input)
    print("Enter a destination For Playlist, Leaving this Blank defaults to current directory")
    destination = str(input(">>")) or "."
    if destination == ".":
        destination = os.getcwd()
    print("Enter a name for the folder:")
    current_folder = os.getcwd()
    new_folder = str(input(">>"))
    path1 = os.path.join(destination,new_folder)
    os.mkdir(path1)
    for v in pl.videos:
        audio = v.streams.filter(only_audio= True).first()
        out_file = audio.download(output_path=new_folder)
        base,ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file,new_file)
        print(v.title + "has been sucessfully downloaded")

else:
    yt = YouTube(user_input)
    audio = yt.streams.filter(only_audio= True).first()

    print("Enter Destination For File, Leaving this blank defaults to current directory")
    destination = str(input(">>")) or "."   

    out_file = audio.download(output_path=destination)

    base,ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file,new_file)

    print(yt.title + "has been sucessfully downloaded")

