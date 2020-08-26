from bs4 import BeautifulSoup
import re
from string import punctuation

BASE = 'C:/Users/JSW/PycharmProjects/flaskProject3/file2html/'

f = open(BASE+"index.xhtml", encoding="utf8")
soup = BeautifulSoup(f)
f.close()

REGEX_SPECIAL = re.compile(r'◆←↑↓―――→[☏≥「」!=+,#.\?^$@□*\【"※~&%ㆍ!\\‘|\(\)\[\]\<\>`\'…≪≫【】∎○■★+△▴◀▶▼□ㅇ㎡☎☞\-\~]')  # 3순위 -> 4
WHITE_SPACES = re.compile(r'\s{2,}') # 5순위 -> 6
NUMERIC_REGEX = re.compile(r'\d+')
DOMAIN_REGEX = re.compile(r'\bhttps|http?://\w+(?:[.]?\w+)+\b')
GM_REGEX = re.compile(r'(\d+)g/m')
SPECIFIC_CHAR_REGEX = re.compile(r'e-mail|E-mail|fax|Fax|http://')
DIVIDE_REGEX = re.compile(r'÷(\d+)')
PHONE_NUMBER = re.compile(r'(\d{1,})(.-?)')
PAPER_REGEX = re.compile(r'(\d+㎜)(.+)')
CM_REGEX = re.compile(r'(\d+cm)(.+)')
DATE_REGEX = re.compile(r'(\d{2,})(.?)(\s?)')
TIME_REGEX = re.compile(r'([0-2]?[0-3]:[0-5][0-9])(.+)')
HANMOON_REGEX = re.compile(r'.*[\u2e80-\u2eff\u31c0-\u31ef\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fbf\uf900-\ufaff].*')
AGE_REGEX = re.compile(r'(\d+)(.~?)')
NUM_SPECIAL = re.compile(r'&#(\d+);') # 1순위
pattern1 = re.compile('[{}■「※」ㆍ√☎㎡□○◦㎥･◆￦￭▸▣❒❙♣◇←－：…………☞≫≪Ⅰ《》〈〉∨…➀Ⅲ➁‣⇨➂∙▪ⓛ‣Ⅱ․․․▲△Ｏ•×【】▶✓➡◀∼″→ㅇ⇒『』◯▼㎜×·④①②③⑤⑦⑥⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱｢｣◎❶❷❸❹❼❺❻]'.format(re.escape(punctuation)))
pattern3 = re.compile(r'[一-龥]')

def cleansing(s):
    s = NUM_SPECIAL.sub(' ', s)
    s = HANMOON_REGEX.sub(' ', s)
    s = AGE_REGEX.sub(' ', s)
    s = TIME_REGEX.sub(' ', s)
    s = DATE_REGEX.sub(' ', s)
    s = CM_REGEX.sub(' ', s)
    s = PAPER_REGEX.sub(' ', s)
    s = DIVIDE_REGEX.sub(' ', s)
    s = SPECIFIC_CHAR_REGEX.sub(' ', s)
    s = GM_REGEX.sub(' ', s)
    s = DOMAIN_REGEX.sub(' ', s)
    s = NUMERIC_REGEX.sub(' ', s)
    s = REGEX_SPECIAL.sub(' ', s)
    s = WHITE_SPACES.sub('', s)
    s = pattern1.sub('',s)
    return s.strip()

for _ in soup.findAll('p'):
    print(cleansing(_.text))