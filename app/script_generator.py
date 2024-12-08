import openai

def generate_script(keywords):
    prompt = f"다음 키워드를 기반으로 막장 소설을 작성해줘: {', '.join(keywords)}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']