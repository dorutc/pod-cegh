
import os

os.system("rm -rf /opt/app-root/src/doru/files_downloads/*")
str = os.system("cd cegh_doru;scrapy list")
print(type(str))