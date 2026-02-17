import requests

def download_image(url, save_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"이미지 다운로드 성공: {save_path}")
        else:
            print(f"다운로드 실패. 상태 코드: {response.status_code}")
    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    img_url = "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?auto=format&fit=crop&w=1200&q=80"
    download_image(img_url, "image.jpg")
