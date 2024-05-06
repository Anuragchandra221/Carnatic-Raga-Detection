
from pytube import YouTube

def download_audio(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path='uploads/', filename='audio.mp3')
        print("Audio downloaded successfully!")
    except Exception as e:
        print(f"Error: {e}")

# if __name__ == "__main__":
#     # url = input("Enter the YouTube URL: ")
#     download_audio('https://www.youtube.com/watch?v=ZQ7O4gAnrVU')
