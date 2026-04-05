import requests
from gtts import gTTS

from generator import generate_script
from video import create_video
from config import PEXELS_API_KEY

def download_video(query):
    url = f"https://api.pexels.com/videos/search?query={query}&per_page=1"
    headers = {"Authorization": PEXELS_API_KEY}

    res = requests.get(url, headers=headers).json()

    video_url = res["videos"][0]["video_files"][0]["link"]
    video_data = requests.get(video_url).content

    with open("assets/video.mp4", "wb") as f:
        f.write(video_data)

def text_to_audio(text):
    tts = gTTS(text=text, lang='en')
    tts.save("assets/voice.mp3")

def run():
    idea = input("Input idea: ")

    print("Generate script...")
    script = generate_script(idea)

    print("Convert to audio...")
    text_to_audio(script)

    print("Download video...")
    download_video(idea)

    print("Create video...")
    create_video()

    print("\nDONE! Video ready in assets/final.mp4")

if __name__ == "__main__":
    run()