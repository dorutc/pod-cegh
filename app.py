from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def hello():
    p = subprocess.run("rm -rf /opt/app-root/src/doru/files_downloads/*")
    p = subprocess.Popen("./scrapy_list.sh", stdout=subprocess.PIPE, shell=True)
    return p.communicate()            #"Hello World!"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')