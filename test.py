
import os

def do_multiple(src):
    f = open(src, "r")
    prinf(f.readline())


os.system("rm -rf /opt/app-root/src/doru/files_downloads/*")
with os.popen("cd cegh_doru;scrapy list") as f:
    str = f.readlines()
print(type(str))
for x in str:
    x = x.strip("\n")
    res = os.system("cd cegh_doru;scrapy crawl " + x)
    print(x)


f_list = os.listdir("/opt/app-root/src/doru/files_downloads")
print(type(f_list))