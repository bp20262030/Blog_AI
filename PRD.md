# PRD: 블로그 자동화 시스템 (Blog AI)

## 1. 프로젝트 개요
이 프로젝트는 특정 키워드를 바탕으로 정보를 수집하고, 관련 이미지를 생성하며, 블로그 포스트를 작성하여 최종적으로 GitHub Pages에 자동으로 게시하는 시스템을 구축하는 것을 목표로 합니다.

## 2. 주요 기능 및 프로세스

### 2.1 정보 수집 (Data Collection)
- **기능**: 사용자로부터 입력받은 키워드를 바탕으로 최신 정보를 수집합니다.
- **도구**: Google Search API (또는 검색 도구)
- **결과물**: `search.md` (수집된 원시 데이터 및 링크 저장)

### 2.2 이미지 생성 (Image Generation)
- **기능**: 블로그 포스트의 주제와 어울리는 고품질 이미지를 생성합니다.
- **도구**: Gemini Image Generation API (DALL-E 또는 Imagen 등 활용)
- **결과물**: `image.jpg` (블로그 대표 이미지)

### 2.3 콘텐츠 작성 (Content Creation)
- **기능**: 수집된 정보를 바탕으로 독자에게 유익하고 구조화된 블로그 포스트 초안을 작성합니다.
- **도구**: Gemini (LLM)
- **결과물**: `draft.md` (Markdown 형식의 블로그 초안)

### 2.4 퍼블리싱 (Publishing)
- **기능**: Markdown 초안을 웹 형태(HTML)로 변환하고 호스팅 서버에 배포합니다.
- **도구**: Quarto, GitHub Pages
- **결과물**: `index.html` 및 관련 자산이 포함된 정적 사이트 배포

## 3. 기술 스택
- **언어**: Python 또는 Node.js (자동화 스크립트)
- **AI/LLM**: Google Gemini API (텍스트 분석 및 이미지 생성)
- **정적 사이트 생성기**: Quarto
- **버전 관리 및 호스팅**: GitHub & GitHub Pages
- **검색**: Google Custom Search API 또는 유사 도구

## 4. 상세 워크플로우
1. 사용자가 키워드 입력.
2. 시스템이 Google 검색을 수행하여 관련 자료를 `search.md`에 요약 정리.
3. 키워드와 요약문을 바탕으로 Gemini가 이미지 생성 프롬프트를 작성하고 이미지를 생성하여 `image.jpg`로 저장.
4. Gemini가 `search.md`를 참고하여 `draft.md` 작성 (제목, 서론, 본문, 결론, 태그 포함).
5. Quarto가 `draft.md`를 렌더링하여 `index.html` 생성.
6. 생성된 파일들을 Git에 커밋 및 푸시하여 GitHub Pages에 실시간 반영.

## 5. 향후 확장 계획
- 일정 주기로 자동 실행되는 스케줄링 기능 (GitHub Actions 활용).
- 다양한 소셜 미디어(X, LinkedIn 등)에 자동 공유 기능 추가.
- 댓글 및 피드백 분석을 통한 콘텐츠 최적화.
