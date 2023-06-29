from flask import Flask
import os
from datetime import date

app = Flask(__name__)
path = "/opt/app-root/src/doru/files_downloads/"
header = ['Trading Day', 'Contract', 'Open', 'High', 'Low', 'Close', 'Trades', 'CEGHEDI', 'VWAP', 'CEGHIX', 'Settlement Price', 'Last Price', 'Price €/MWh', 'Product', 'Trading phase', 'Volume acc.']
header_line = "Trading Day;Contract;Open;High;Low;Close;Trades;CEGHEDI;VWAP;CEGHIX;Settlement Price;Last Price;Price €/MWh;Product;Trading phase;Volume acc.;filename\n"
today = date.today()
str_date = today.strftime("%d%m%Y")

def do_multiple(src):
    src1 = path + src
    f = open(src1, "r")
    dest1 = open(path + "all_" + str_date,"a")
    h = f.readline()
    h_list = h.split(";")
    for l in f:
        w_list = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        l_list = l.split(";")
        i = 0
        for y in h_list:
            j = 0
            for x in header:
                if x == y:
                    w_list[j]= l_list[i]
                j = j + 1
            i = i + 1
        w_l = ""
        for z in w_list:
            w_l = w_l + z + ";"
        w_l += src
        dest1.write(w_l + "\n")
    dest1.close()
    f.close()	

def do_crawl():
        os.system("rm -rf /opt/app-root/src/doru/files_downloads/*")
        with os.popen("cd cegh_doru;scrapy list") as f:
            str = f.readlines()
        for x in str:
            x = x.strip("\n")
            res = os.system("cd cegh_doru;scrapy crawl " + x)

def do_all_work():
        f_list = os.listdir(path)
        dest = open(path + "all_" + str_date,"a")
        dest.write(header_line)
        dest.close()

        for x in f_list:
            do_multiple(x)
        page = ""
        f = open(path + "all_" + str_date,"r")
        for l in f:
            page = page + l + "<br>"
        return "<html> <body>"  + page + "</body></html>"

@app.route('/all')
def do_all():
    try:
        do_crawl()
        return do_all_work()
    except Exception as error:
        return error


@app.route('/dayahead')
def dayahead():
    return "day ahead"

@app.route('/')
def hello():
        return "Hello!"




if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')