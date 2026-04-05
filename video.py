from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from config import OUTPUT_VIDEO

def create_video():
    video = VideoFileClip("assets/video.mp4")
    audio = AudioFileClip("assets/voice.mp3")

    duration = audio.duration

    # potong durasi
    try:
        video = video.subclip(0, duration)
    except:
        video = video.subclipped(0, duration)

    # resize ke tinggi 1920
    try:
        video = video.resize(height=1920)
    except:
        video = video.resized(height=1920)

    # 🔥 crop tengah (API BARU)
    video = video.cropped(
        x_center=video.w / 2,
        y_center=video.h / 2,
        width=1080,
        height=1920
    )

    # attach audio
    try:
        final = video.with_audio(audio)
    except:
        final = video.set_audio(audio)

    final.write_videofile(
        OUTPUT_VIDEO,
        fps=24,
        codec="libx264",
        audio_codec="aac"
    )