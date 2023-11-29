import pytube as pt

playlist_url = "https://youtube.com/playlist?list=PLsWudFQO5VJPmtHlTmwSi3rO6jhcdvbIG&si=TZQ-G60U-le-ewdb"
playlist = pt.Playlist(playlist_url)

for i, video in enumerate(playlist.videos, 1):
    try:
        audio_stream = video.streams.filter(only_audio=True).first()
        print(f"Downloading {i}/{playlist.length}: {video.title}...")
        audio_stream.download("Songs/")
    except:
        print(f"Error while downloading {video.title}. Skipping...")
