#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ====================================================

import os
import sys
import time, datetime
import urllib.request as req
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# ====================================================

def main():
    const_url = "http://192.168.11.2/index.html"
    res = req.urlopen(const_url)

    soup = BeautifulSoup(res, "html.parser")
    result = soup.select("a[href]")
    
    const_base = "http://192.168.11.2/"
    li = []
    for link in result:
        href = link.get('href')
        li.append(urljoin(const_base, href))
    
    cnt = 1
    a = [s for s in li if s.endswith('pdf')]
    for i in a:
        sys.stdout.write("\r%s" % i 
                         + "\033[32m{}\033[0m".format(" (" + str(cnt)) 
                         + "\033[32m{}\033[0m".format("/") 
                         + "\033[32m{}\033[0m".format(str(len(a)) + ") "))
        sys.stdout.flush()
        req.urlretrieve(i, 
                        '/tmp/' 
                        + os.path.basename(i))
        time.sleep(1)
        cnt = cnt + 1
    
    print("\r\r")

# ====================================================

def start():
    t = datetime.datetime.fromtimestamp(time.time())
    print(" ++ begin ++ ({})".format(t.strftime('%Y/%m/%d %H:%M:%S')))
    main()
    t = datetime.datetime.fromtimestamp(time.time())
    print(" ++  end  ++ ({})".format(t.strftime('%Y/%m/%d %H:%M:%S')))

# ====================================================
# ====================================================

if __name__=='__main__':
    start()

