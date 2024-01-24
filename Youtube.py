import pytube
def download_and_convert_video(video_url, output_format="mp4", output_resolution="720p"):
    youtube = pytube.YouTube(video_url) 
    stream = youtube.streams.get_highest_resolution()
    stream.download()

    output_file_path = f"{youtube.title}.{output_format}"
    return output_file_path

video_url = "https://youtu.be/0ATtCKfyPb0?si=kD1rJBzI7tTLeGHx"
print("Program is Running..")
print("Your video is downloading.....")
output_file_path = download_and_convert_video(video_url)
print("Video downloaded and converted to:", output_file_path)
