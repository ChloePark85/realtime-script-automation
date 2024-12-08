import openai

def generate_thumbnail(text):
    response = openai.Image.create(prompt=text, n=1, size="1024x1024")
    return response["data"][0]["url"]