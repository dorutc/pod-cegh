
import os

def hello():
    try:
        os.system("rm -rf /opt/app-root/src/doru/files_downloads/*")
        str = "Hello World!" 
        str = os.system("cd cegh_doru;scrapy list")
        return str      #"Hello World!" 
    except Exception as error:
        return error
print(hello())