# 이미지 OCR 관련 작업
## 설명
원하는 민원 서식을 이미지 형태로 나타낸 후, 텍스트 추출

## OCR 과정
1. Image 전처리(노이즈 제거, 배경색 제거 등)

2. Text Detection : 이미지에서 텍스트 추출

3. Text Recognition : 추출된 텍스트를 인식

4. Text 후처리

## 소스코드
### deep-text-recognition-benchmark
이미지 텍스트 인식 모델

### east_example1/east_text_detection.py  
east model을 활용한 text detection sample 소스  
[참고소스](https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/)

### text_detection_east/*
한글 OCR git 참고(진행중) 
[참고소스](https://github.com/parksunwoo/ocr_kor)

### text_detection.ipynb
pytesseract를 이용한 이미지 인식