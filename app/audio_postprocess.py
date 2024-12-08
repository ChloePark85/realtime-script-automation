from pydub import AudioSegment

def add_background_music(audio_path):
    original = AudioSegment.from_file(audio_path)
    background = AudioSegment.from_file("background.mp3").apply_gain(-10)
    combined = original.overlay(background)
    output_path = "output/final_audio.mp3"
    combined.export(output_path, format="mp3")
    return output_path