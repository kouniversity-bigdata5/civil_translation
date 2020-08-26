from werkzeug.utils import secure_filename
from flask import Flask, url_for, render_template, request, redirect, session
import os
import hwp2html

app = Flask(__name__)

#업로드 HTML 렌더링
@app.route('/upload')
def render_file():
   return render_template('upload.html')

#파일 업로드 처리
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      #저장할 경로 + 파일명
      f.save('C:/Users/JSW/PycharmProjects/flaskProject3/upload/'+secure_filename(f.filename))
      return 'Please Waiting for translation'


if __name__ == '__main__':
    #서버 실행
   app.run(debug = True)
