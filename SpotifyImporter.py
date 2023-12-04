import pytube as pt

# Input playlist URL here as string
playlist_url = "https://youtube.com/playlist?list=PLsWudFQO5VJPmtHlTmwSi3rO6jhcdvbIG&si=TZQ-G60U-le-ewdb"

# Create playlist object
playlist = pt.Playlist(playlist_url)

# Loop through all videos
for i, video in enumerate(playlist.videos, 1):
    # For each video, try/except since some videos may not be downloadable because of age restrictions or etc.
    try:
        # Get highest quality (last) mp4 audio stream and download
        audio_stream = video.streams.filter(only_audio=True,mime_type="audio/mp4").last()
        print(f"Downloading {i}/{playlist.length}: {video.title}...")
        audio_stream.download("Songs/")
    except:
        # Print error message if it didn't work
        print(f"Error while downloading {video.title}. Skipping...")
