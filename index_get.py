import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    '''
	此函数用于获取网页的html文档
	'''
    try:
        #获取服务器的响应内容，并设置最大请求时间为6秒
        res = requests.get(url, timeout = 6)
        #判断返回状态码是否为200
        res.raise_for_status()
        #设置该html文档可能的编码
        res.encoding = res.apparent_encoding
        #返回网页HTML代码
        return res.text
    except:
        return'产生异常'

def main():
    '''
	主函数
	'''
    print("执行中....")
    #目标网页
    url='https://www.fmprc.gov.cn/web/wjdt_674879/fyrbt_674889/default.shtml';
    
    demo=getHTMLText(url)

    #解析HTML代码
    soup=BeautifulSoup(demo,'html.parser')
	#得到图片网址
    print(soup)
