from app.script_generator import generate_script

def test_generate_script():
    """
    OpenAI API를 사용하여 스크립트를 생성하는 테스트 함수.
    """
    # 테스트 키워드
    test_keywords = ["AI", "막장 드라마", "혁명", "복수", "사랑"]
    print("테스트 키워드:", test_keywords)

    # 스크립트 생성 테스트
    try:
        script = generate_script(test_keywords)
        assert len(script) > 0, "생성된 스크립트가 비어 있습니다!"
        print("\n생성된 스크립트:")
        print(script)
    except Exception as e:
        print("스크립트 생성 중 오류 발생:", e)

# 테스트 실행
if __name__ == "__main__":
    test_generate_script()