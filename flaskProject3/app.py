from werkzeug.utils import secure_filename
from flask import Flask, url_for, render_template, request, redirect, session
import os
from hwp2html import hwp2html
from bs4 import BeautifulSoup

from googletrans import Translator
import re
import random
import string
import torch


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


app.config.update(
   # 업로드 폴더 설정(이렇게 지정하면 전체 path를 지정할 필요가 없음)
    UPLOADED_PATH=os.path.join(basedir, 'upload')
)
@app.before_first_request
def before_first_request():
    print('!!!!!!!!!!!!load model')


# 폴더명 자동생성
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def cleansing(text):
    text = re.sub(re.compile('[(\s)]'), ' ', text)
    text = re.sub(re.compile('<'), '', text)
    text = re.sub(re.compile('>'), '', text)
    text = re.sub(re.compile('\s+'), ' ', text)
    return text


def translate(text):
    """
    googletrans를 이용한 번역
    pip install googletrans 설치 필요
    :param text:
    :return:
    """
    translator = Translator()
    translated_text = translator.translate(text, dest='th').text
    print(translated_text)
    return translated_text



#업로드 HTML 렌더링
@app.route('/')
def render_file():
    return render_template('upload.html')


@app.errorhandler(Exception)
@app.route('/upload', methods = ['POST'])
def upload():
    return_html = ''  # 번역한 HTML 결과

    if request.method == 'POST':
        f = request.files.get('file')
        translate_list = []  # 번역한 문장 리스트

        folder_name = get_random_string(8)  # 임의의 폴더 경로 생성

        #  폴더 경로가 없으면 새로 생성
        if not os.path.isdir('{}/{}'.format(app.config['UPLOADED_PATH'], folder_name)):
            os.mkdir('{}/{}'.format(app.config['UPLOADED_PATH'], folder_name))

        #  파일 저장
        f.save(os.path.join('{}/{}'.format(app.config['UPLOADED_PATH'], folder_name), f.filename))
        #  hwp를 html로 변환한 파일 저장 path
        output_path = '{}/{}'.format(app.config['UPLOADED_PATH'], folder_name+'/result')

        #  hwp -> html 변환
        res = hwp2html(app.config['UPLOADED_PATH'], 'hwp5html', output_path)
        print('result ', res)

        if res:
            try:
                with open('{}/{}'.format(output_path, 'index.xhtml'), 'r', encoding='utf-8') as f:
                    #  beautifulsoup 형태로 불러오기
                    content = BeautifulSoup(f.read(), 'lxml')
                    #  한글인 부분만 가져오기
                    ko_text = content.select('span.lang-ko')

                    #  한글인 부분 번역 요청
                    for ko in ko_text:
                        # 번역 실행
                        translate_txt = translate(ko.text)
                        # 번역 결과 List append
                        translate_list.append(translate_txt)

                    #  번역한 리스트 개수만큼 content의 text에 replace
                    for i in range(len(translate_list)):
                        content.select('span.lang-ko')[i].string.replace_with(translate_list[i])

                    return_html = content
            except Exception as e:
                print(e)

    return render_template('upload.html', result=return_html)

@app.route('/menu')
def menu_file():
   return render_template('menu_tab.html')


if __name__ == '__main__':
    app.run(debug=True)