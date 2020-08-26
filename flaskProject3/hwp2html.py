import os

path = 'C:/Users/JSW/PycharmProjects/flaskProject3/upload/'
exefile = 'hwp5html'
output = 'C:/Users/JSW/PycharmProjects/flaskProject3/file2html/'

def hwp2html(path):
   res = []
   for root, dirs, files in os.walk(path):
      rootpath = os.path.join(os.path.abspath(path), root)
      for file in files:
         filename = file.split('.')[0]
         filepath = os.path.join(rootpath, file)
         res.append(filepath)
      for result in res:
         result = '"' + result + '"'
         os.system(exefile+' '+result+' --output '+output+'/'+filename)


if __name__ == "__main__":
   hwp2html(path)