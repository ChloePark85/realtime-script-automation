import elevenlabs

def convert_text_to_audio(text):
    audio = elevenlabs.generate(
        api_key="your_api_key",
        text=text,
        voice="YourVoiceModel"
    )
    output_path = "output/audio.mp3"
    with open(output_path, "wb") as f:
        f.write(audio)
    return output_path