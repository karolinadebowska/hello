import requests
import json
import os

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/hello', methods=["POST"])
def hello():
    language=["Azerbaijan","Malayalam","Albanian","Maltese","Amharic","Macedonian","Arabic","Marathi","Armenian",
    "Mongolian","German","Polish","Spanish","Chinese","French","Scottish","Korean","Esperanto","Sundanese","Persian"]
    background=["#9932CC","black","#00CED1","#9932CC","#B22222","#696969","#4B0082","#20B2AA","#800000","#800080",
                "#C71585","#FF4500","#DA70D6","#BC8F8F","#4682B4","#9ACD32","#4682B4","#708090","#DB7093","#6B8E23"]
    font=["#48D1CC","#FFC0CB","#FFDEAD","#FAF0E6","#FFA07A","#FFB6C1","#FAFAD2","#FFFACD","#FFF0F5","#F0E68C",
            "#F0FFF0","#ADFF2F","#FFD700","#FF00FF","#00CED1","#E9967A","#BDB76B","#00FFFF","#7FFF00","#7FFFD4"]
    data = request.values
    #data = response.json()[0]
    #print(data)
    #translated = data[translate('pl')]
    return render_template("hello.html",language=language,font=font,background=background,x=0, hello_data=data,hello="Hello")


def get_html(url):
    return requests.get(url).text

def get_translation(text,lang):
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    KEY = 'trnsl.1.1.20190327T124524Z.4e89613a1157b6a0.7b0530f224bf837dcfb94e36c946f89fff5a4e28'
    TEXT = text
    LANG = lang;
    r=requests.post(URL, data={'key' : KEY,'text' : TEXT,'lang' : LANG} )
    return r.text

hello="Hello"
def translate(lang):
    translation = get_translation(hello, lang)
    index = translation.find("text")
    translation= translation[index+8:-3]
    print(translation)

translate('pl')
#Azerbaijan
#translate('az')
#Malayalam
#translate('ml')
#Albanian
#translate('sq')
#Maltese
#translate('mt')
#Amharic
#translate('am')
#Macedonian
#translate('mk')
#Arabic
#translate('ar')
#Marathi
#translate('mr')
#Armenian
#translate	('hy')
#Mongolian
#translate('mn')
#German
#translate('de')
#Polish
#translate('pl')
#Spanish
#translate('es')
#Chinese
#translate('zh')
#French
#translate('fr')
#Scottish
#translate('gd')
#Korean
#translate('ko')
#Esperanto
#translate('eo')
#Sundanese
#translate('su')
#Persian
#translate('fa')
#Vietnamese
#translate('vi')
#	Russian
#translate('ru')
#Haitian
#translate('ht')
if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)
