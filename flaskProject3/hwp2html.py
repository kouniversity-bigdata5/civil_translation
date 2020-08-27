import os

def hwp2html(path, exefile, output):
   '''
   hwp를 html로 변환
   '''
   res = []
   # 명령어 포맷 설정
   operation_format = '{} --output={} {}'

   for root, dirs, files in os.walk(path):
      rootpath = os.path.join(os.path.abspath(path),root)
      for file in files:
         filepath = os.path.join(rootpath, file)
         res.append(filepath)

         for result in res:
            os.system(operation_format.format(exefile, output, result))
   
   # output 폴더가 생성된 여부에 따라 html파일이 생성되었는지 판단
   return True if os.path.exists(output) else False