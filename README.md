# 옛말에서 오늘의 말로

중세국어 문장과 현대국어 대응 표현을 비교하고 언어 변화 양상을 학습하는 Streamlit 시제품입니다.

## 실행 방법

1. Python 3.10 이상을 설치합니다.
2. 프로젝트 폴더에서 다음 명령어를 실행합니다.

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Streamlit Community Cloud 배포

1. GitHub 저장소에 `app.py`와 `requirements.txt`가 있는지 확인합니다.
2. https://share.streamlit.io/ 에 접속해 GitHub 계정으로 로그인합니다.
3. New app을 선택하고 이 저장소, 기본 브랜치(main), 파일 경로(app.py)를 지정합니다.
4. Deploy를 누릅니다.

## 기능

- 홈: 탐구 목적 및 메뉴 안내
- 문장 변환실: 등록된 예문 선택 및 직접 입력 확인
- 언어 변화 분석실: 예문별 어휘·형태 대응 설명
- 문헌 자료실: 용비어천가 제2장 예문
- 학습 퀴즈: 선택형 문제 및 채점

## 자료 사용 시 주의

현재 버전은 등록된 예문을 보여 주는 교육용 시제품이며 일반적인 중세국어 자동 번역기가 아닙니다. 문헌 원문, 현대어 풀이, 세부 문법 해설은 실제 사용 판본과 신뢰할 수 있는 주석 자료를 대조하여 검증한 뒤 확장해야 합니다.
