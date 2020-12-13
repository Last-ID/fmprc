import requests
import codecs
import time


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
}
response_url='https://www.fmprc.gov.cn/web/wjdt_674879/fyrbt_674889/'
response_url_text=response_url+"default.shtml"

response = requests.get(response_url_text,headers=headers)
print(response.status_code)  # 打印状态码
print(response.url)          # 打印请求url


result_str=response.text
status_code_str=str(response.status_code)

with open('text_results.txt', mode='a', encoding='utf-8') as results:


    results.write('[url:' + response.url + ']')
    results.write('\n') # 换行
    results.write('[status_code:' + status_code_str + ']')
    results.write('\n') # 换行
    results.write(result_str)
    results.write('\n') # 换行

