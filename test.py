
import os

def hello():
    try:
        os.system("rm -rf /opt/app-root/src/doru/files_downloads/*")
        str = os.system("cd cegh_doru;scrapy list")
        lst = str.splitlines()
        for x in lst:
             print(x)		
        return str      #"Hello World!" 
    except Exception as error:
        return error
print(hello())