from flask import Flask
import os
from datetime import date

app = Flask(__name__)
today = date.today()
str_date = today.strftime("%d%m%Y")
path = "/opt/app-root/src/doru/files_downloads/"

@app.route('/')
def hello():
    try:
        page = ""
        f = open(path + "all_" + str_date,"r")
        for l in f:
            page = page + l
        return "<html> <body>"  + page + "</body></html>"
    except Exception as error:
        return error

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')