
import os


def hello():
    os.system("rm -rf /opt/app-root/src/doru/files_downloads/*")
    str = "Hello World!" 
    with os.popen("cd cegh_doru;scrapy list") as f:
        str = f.readlines()
    return str      #"Hello World!" 



hello()