from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    os.system("rm -rf /opt/app-root/src/doru/files_downloads/*")
    with os.popen("./scrapy_list.sh", stdout=subprocess.PIPE, shell=True) as f:
        str = f.readlines()
    return str         #"Hello World!"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')