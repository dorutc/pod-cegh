
import os

os.system("rm -rf /opt/app-root/src/doru/files_downloads/*")
with os.popen("cd cegh_doru;scrapy list") as f:
    str = f.readlines()
print(type(str))
for x in str:
    x = x.x.strip("\n")
	res = os.system("scrapy crawl " + x)
    print(x)