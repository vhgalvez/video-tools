from pathlib import Path
import numpy as np

from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.audio.fx.all import audio_fadein, audio_fadeout


VIDEO_DIR = Path("videos")
OUTPUT_DIR = Path("videos_clean")

WIDTH = 448
HEIGHT = 768
FPS = 25

# Ajustes suaves para no dañar la voz
SILENCE_THRESHOLD = 0.012
MIN_SILENCE_DURATION = 0.55
KEEP_MARGIN = 0.16

# Fade pequeño solo para que no corte seco dentro del mismo clip
AUDIO_FADE_IN = 0.03
AUDIO_FADE_OUT = 0.05


def get_audio_volume_array(clip, sample_rate=8000):
    audio = clip.audio

    if audio is None:
        return None, None

    duration = clip.duration

    if duration <= 0:
        return None, None

    times = np.arange(0, duration, 1 / sample_rate)

    try:
        samples = audio.to_soundarray(tt=times)
    except Exception:
        return None, None

    if samples.ndim == 2:
        samples = np.mean(np.abs(samples), axis=1)
    else:
        samples = np.abs(samples)

    return times, samples


def detect_speech_segments(clip):
    times, volume = get_audio_volume_array(clip)

    if times is None or volume is None:
        return [(0, clip.duration)]

    is_sound = volume > SILENCE_THRESHOLD

    segments = []
    start = None

    for i, sound in enumerate(is_sound):
        t = times[i]

        if sound and start is None:
            start = t

        if not sound and start is not None:
            end = t
            segments.append((start, end))
            start = None

    if start is not None:
        segments.append((start, clip.duration))

    if not segments:
        return [(0, clip.duration)]

    # Une partes cercanas para no cortar pausas naturales
    merged = []
    current_start, current_end = segments[0]

    for start, end in segments[1:]:
        silence_gap = start - current_end

        if silence_gap < MIN_SILENCE_DURATION:
            current_end = end
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))

    # Añadir margen antes y después de la voz
    final_segments = []

    for start, end in merged:
        start = max(0, start - KEEP_MARGIN)
        end = min(clip.duration, end + KEEP_MARGIN)

        if end - start > 0.2:
            final_segments.append((start, end))

    return final_segments


def delete_silence_from_video(path):
    print(f"\nProcesando: {path.name}")

    clip = VideoFileClip(str(path))
    clip = clip.resize(newsize=(WIDTH, HEIGHT))
    clip = clip.set_fps(FPS)

    output_path = OUTPUT_DIR / f"{path.stem}_clean.mp4"

    # Si no tiene audio, lo guarda igual sin tocar
    if clip.audio is None:
        print(f"  Sin audio. Se guarda completo: {output_path.name}")

        clip.write_videofile(
            str(output_path),
            fps=FPS,
            codec="libx264",
            audio_codec="aac",
            preset="fast",
            bitrate="4000k"
        )

        clip.close()
        return

    segments = detect_speech_segments(clip)

    pieces = []

    for start, end in segments:
        print(f"  segmento: {start:.2f}s -> {end:.2f}s")

        piece = clip.subclip(start, end)

        if piece.audio:
            audio = piece.audio.fx(audio_fadein, AUDIO_FADE_IN).fx(audio_fadeout, AUDIO_FADE_OUT)
            piece = piece.set_audio(audio)

        pieces.append(piece)

    if not pieces:
        print(f"  No se detectaron segmentos útiles. Se conserva completo.")
        pieces = [clip]

    final = concatenate_videoclips(
        pieces,
        method="compose"
    )

    final.write_videofile(
        str(output_path),
        fps=FPS,
        codec="libx264",
        audio_codec="aac",
        preset="fast",
        bitrate="4000k"
    )

    final.close()
    clip.close()

    for piece in pieces:
        try:
            piece.close()
        except Exception:
            pass

    print(f"  Guardado: {output_path}")


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    video_paths = sorted(VIDEO_DIR.glob("*.mp4"))

    video_paths = [
        p for p in video_paths
        if not p.name.startswith("video_final")
    ]

    if not video_paths:
        raise RuntimeError("No hay videos .mp4 en la carpeta videos/")

    for path in video_paths:
        delete_silence_from_video(path)

    print("\nListo. Videos limpios guardados en videos_clean/")


if __name__ == "__main__":
    main()