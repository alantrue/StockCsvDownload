import string
import codecs
import urllib.request
import configparser
import os
import datetime

from datetime import date, timedelta

for i in range(4530):
    mon = (date.today() + timedelta(-i)).strftime('%Y%m')
    day = (date.today() + timedelta(-i)).strftime('%Y%m%d')
    #print(mon)
    #print(day)

    url = "http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX3_print.php?genpage=genpage/Report{0}/A112{1}ALLBUT0999_1.php&type=csv".format(mon, day)
    file = "E:\\stockData\\{0}.csv".format(day)

    urllib.request.urlretrieve(url, file)

print("done")