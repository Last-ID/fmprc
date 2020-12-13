import requests
import codecs
import time


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
}
response_url='https://www.fmprc.gov.cn/web/wjdt_674879/fyrbt_674889/'

for pagenum in range(67):
    print(pagenum)
    if pagenum == 0:
        response_url_page=response_url+"default.shtml"
    else:
        response_url_page=response_url+"default_" + str(pagenum) + ".shtml"
    
    response = requests.get(response_url_page,headers=headers)
    print(response.status_code)  # 打印状态码
    print(response.url)          # 打印请求url

    #print(response.headers)      # 打印头信息
    #print(response.cookies)      # 打印cookie信息
    #print(response.text)  #以文本形式打印网页源码
    #print(response.content) #以字节流形式打印

    result_str=response.text
    status_code_str=str(response.status_code)

    with open('results.txt', mode='a', encoding='utf-8') as results:


        results.write('[url:' + response.url + ']')
        results.write('\n') # 换行
        results.write('[status_code:' + status_code_str + ']')
        results.write('\n') # 换行
        results.write(result_str)
        results.write('\n') # 换行

        time.sleep(3)
