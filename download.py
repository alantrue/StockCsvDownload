import string
import codecs
import urllib
import ConfigParser
import os
import datetime

from datetime import date, timedelta

os.chdir("E:\\StockData")
files = os.listdir("E:\\StockData")

if len(files) == 0:
    end = datetime.date(2004, 2, 10)
else:
    lastFile = files[-1]
    end = datetime.date(int(lastFile[0:4]),int(lastFile[4:6]), int(lastFile[6:8]))

delta = date.today() - end

for i in range(delta.days):
    mon = (date.today() + timedelta(-i)).strftime('%Y%m')
    day = (date.today() + timedelta(-i)).strftime('%Y%m%d')
    #print(mon)
    #print(day)

    url = "http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX3_print.php?genpage=genpage/Report{0}/A112{1}ALLBUT0999_1.php&type=csv".format(mon, day)
    file = "E:\\stockData\\{0}.csv".format(day)

    urllib.urlretrieve(url, file)

print("done")