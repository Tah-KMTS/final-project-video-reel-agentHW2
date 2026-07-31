"""Stitches slide images (and optional narration audio) into a video file."""

from moviepy import AudioFileClip, ImageClip, concatenate_videoclips

DEFAULT_SLIDE_SECONDS = 10.0


def build_video(
    image_paths: list[str],
    audio_paths: list[str] | None = None,
    out_path: str = "reel.mp4",
) -> None:
    clips = []
    for i, img_path in enumerate(image_paths):
        if audio_paths:
            audio = AudioFileClip(audio_paths[i])
            clip = ImageClip(img_path).with_duration(audio.duration).with_audio(audio)
        else:
            # Placeholder duration until TTS is unblocked - once we have
            # real narration audio, pass audio_paths and each slide's
            # clip will instead last exactly as long as its narration.
            clip = ImageClip(img_path).with_duration(DEFAULT_SLIDE_SECONDS)
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")
    video.write_videofile(out_path, fps=24)
