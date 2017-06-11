#coding=utf-8
import re
import random
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html):
  
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        print imgurl
        urllib.urlretrieve(imgurl,'%s.jpg' % random.choice('abcdefg&#%^*f') )
        x+=1
    return imglist      



html = getHtml("https://tieba.baidu.com/p/2999617551")
print getImg(html)

#print html
