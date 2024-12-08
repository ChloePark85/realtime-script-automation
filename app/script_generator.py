import os
from openai import OpenAI
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_script(main_keyword):
    """
    메인 키워드를 기반으로 오디오드라마 스크립트를 생성합니다.
    """
    prompt = f"""
    다음 키워드를 중심으로 막장 오디오드라마 스크립트를 작성해주세요: {main_keyword}
    
    다음 형식으로 작성해주세요:
    
    [제목]
    
    [등장인물]
    - 캐릭터 이름과 상세 설명
    - 캐릭터의 성격, 배경, 동기 포함
    
    [시놉시스]
    - 전체 줄거리 요약
    
    [스크립트]
    # 씬 1
    (효과음: 설명)
    캐릭터A: (감정/톤) "대사"
    캐릭터B: (감정/톤) "대사"
    (효과음: 설명)
    내레이션: "설명"
    
    # 씬 2
    ...
    
    한글 3000자 내외로 작성해주세요.
    감정과 효과음을 상세히 표현해주세요.
    막장 드라마적 요소를 충분히 넣어주세요.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",  # 더 긴 컨텍스트를 위해 16k 모델 사용
        messages=[
            {
                "role": "system", 
                "content": "당신은 막장 오디오드라마 작가입니다. 감정선과 효과음이 풍부한 드라마틱한 스크립트를 작성해주세요."
            },
            {"role": "user", "content": prompt}
        ],
        max_tokens=4000,
        temperature=0.8,
    )
    
    return response.choices[0].message.content.strip()