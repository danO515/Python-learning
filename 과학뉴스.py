
import requests

headers = \
{'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=731'
site = requests.get(url, headers=headers)
source_data = site.text

count = source_data.count('width="106" height="72" alt="')

for i in range(count):
    pos1= source_data.find(' width="106" height="72" alt="') + len(' width="106" height="72" alt="')
    source_data = source_data[pos1:]

    pos2 = source_data.find('onError')
    extract_data = source_data[:pos2-2]

    source_data = source_data[pos2+1:]
    print(i+1, extract_data)
