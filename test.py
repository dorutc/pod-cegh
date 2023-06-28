
import os

path = "/opt/app-root/src/doru/files_downloads/"

def do_multiple(src):
    src1 = path + src
    f = open(src1, "r")
    print(f.readline())


os.system("rm -rf /opt/app-root/src/doru/files_downloads/*")
with os.popen("cd cegh_doru;scrapy list") as f:
    str = f.readlines()
print(type(str))
for x in str:
    x = x.strip("\n")
    res = os.system("cd cegh_doru;scrapy crawl " + x)
    print(x)


f_list = os.listdir(path)
print(type(f_list))
print(f_list)

for x in f_list:
    do_multiple(x)