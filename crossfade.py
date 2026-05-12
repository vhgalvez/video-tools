from moviepy import VideoFileClip, concatenate_videoclips

clips_paths = [
    "clip1.mp4",
    "clip2.mp4",
    "clip3.mp4"
]

fade_duration = 0.12  # mejor para TikTok/Reels/Shorts

clips = []

for path in clips_paths:
    clip = VideoFileClip(path)

    clip = clip.resized((448, 768))
    clip = clip.with_fps(25)

    if clip.audio:
        clip = clip.with_audio(
            clip.audio.audio_fadein(0.05).audio_fadeout(0.08)
        )

    clips.append(clip)

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