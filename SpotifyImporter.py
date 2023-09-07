from pytube import YouTube
url1_future_sounds = "https://www.youtube.com/watch?v=dzQoliuqCfE"
video = YouTube(url1_future_sounds)

stream = video.streams.filter(only_audio=True).first()
stream.download(filename=f"{video.title}.mp3")
