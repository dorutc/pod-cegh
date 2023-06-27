from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        os.system("rm -rf /opt/app-root/src/doru/files_downloads/*")
        str = "Hello World!" 
        str = os.system("pwd")
        return str      #"Hello World!" 
    except Exception as error:
        return error

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')