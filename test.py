
import os
from datetime import date

path = "/opt/app-root/src/doru/files_downloads/"
header = ['Trading Day', 'Contract', 'Open', 'High', 'Low', 'Close', 'Trades', 'CEGHEDI', 'VWAP', 'CEGHIX', 'Settlement Price', 'Last Price', 'Price €/MWh', 'Product', 'Trading phase', 'Volume acc.']
header_line = "Trading Day;Contract;Open;High;Low;Close;Trades;CEGHEDI;VWAP;CEGHIX;Settlement Price;Last Price;Price €/MWh;Product;Trading phase;Volume acc.;filename\n"
today = date.today()
str_date = today.strftime("%d%m%Y")

def do_multiple(src):
    src1 = path + src
    print(src)
    f = open(src1, "r")
    dest = open(path + "all_" + str_date + ".csv","a")
    h = f.readline()
    h_list = h.split(";")
    for l in f:
        w_l = ""
        l_list = l.split(";")
        for x in header:
            i = 0
            for y in h_list:
                if x == y:
                    w_l += l_list[i]
                w_l += ";"
        dest.write(w_l + "\n")
    dest.close()		 


os.system("rm -rf /opt/app-root/src/doru/files_downloads/*")
with os.popen("cd cegh_doru;scrapy list") as f:
    str = f.readlines()
print(type(str))
for x in str:
    x = x.strip("\n")
    res = os.system("cd cegh_doru;scrapy crawl " + x)
    print(x)


dest = open(path + "all_" + str_date + ".csv","a")
dest.write(header_line)
dest.close()
f_list = os.listdir(path)
print(type(f_list))
print(f_list)


for x in f_list:
    do_multiple(x)