from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.audio.fx.all import audio_fadein, audio_fadeout

clips_paths = [
    "clip1.mp4",
    "clip2.mp4",
    "clip3.mp4"
]

fade_duration = 0.12  # bueno para TikTok/Reels/Shorts

clips = []

for path in clips_paths:
    clip = VideoFileClip(path)

    # Normalizar tamaño y FPS
    clip = clip.resize(newsize=(448, 768))
    clip = clip.set_fps(25)

    # Suavizar audio
    if clip.audio:
        audio = clip.audio.fx(audio_fadein, 0.05).fx(audio_fadeout, 0.08)
        clip = clip.set_audio(audio)

    clips.append(clip)

# Unir con transición suave
final = concatenate_videoclips(
    clips,
    method="compose",
    padding=-fade_duration
)

final.write_videofile(
    "video_final_tiktok_suave.mp4",
    fps=25,
    codec="libx264",
    audio_codec="aac",
    preset="fast",
    bitrate="4000k"
)