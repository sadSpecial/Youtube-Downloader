from pytube import YouTube

def Download(URL):
    yt = YouTube(URL)
    Stream = yt.streams.filter(progressive=True,file_extension="mp4").order_by("resolution").desc().last()
    Stream.download()

Download("https://www.youtube.com/watch?v=example")