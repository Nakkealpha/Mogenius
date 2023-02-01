import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'GreyMatters_Bot'

#Ex https://Greymattersbot:ghp_147bkkabcdefgh@github.com/Greymattersbot/Mogenius
os.system("git clone https://nakkealpha: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@github.com/Nakkealpha/File-Sharing-Bot okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 main.py &")
