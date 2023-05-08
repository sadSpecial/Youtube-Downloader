# instagram page : https://instagram.com/abolfazl._r?igshid=YmMyMTA2M2Y
# Email: abolfazl8abolfazl@yahoo.com
# MyGithub : https://github.com/sadSpecial

from pytube import YouTube

def Download(URL):
    yt = YouTube(URL)
    Stream = yt.streams.filter(progressive=True,file_extension="mp4").order_by("resolution").desc().last()
    Stream.download()

Download("https://www.youtube.com/watch?v=example")
