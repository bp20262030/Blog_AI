import os
from google import genai
from google.genai import types

def generate_image():
    api_key = os.getenv("GOOGLE_API_KEY")
    client = genai.Client(api_key=api_key)
    
    prompt = "A futuristic quantum computer in a high-tech laboratory, glowing blue and violet lights, intricate circuits, cinematic lighting, 8k resolution."
    
    try:
        print(f"이미지 생성 중: {prompt}")
        response = client.models.generate_images(
            model='imagen-3.0-generate-001',
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
            )
        )
        
        # 이미지 저장
        for i, image in enumerate(response.generated_images):
            with open("image.jpg", "wb") as f:
                f.write(image.image_bytes)
            print(f"이미지가 성공적으로 생성되어 image.jpg에 저장되었습니다.")
            
    except Exception as e:
        print(f"에러 발생: {e}")
        # 이미지 생성이 불가능할 경우를 대비해 빈 파일 생성 방지 (에러 로그 확인용)

if __name__ == "__main__":
    generate_image()
