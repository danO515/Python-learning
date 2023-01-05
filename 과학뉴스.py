import requests
import datetime as dt
x = dt.datetime.now()

headers = \
{'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

for i in ():
    for j in range(3):
        if x.day - j < 1:
            
            if x.month - 1 < 1:
                y = x.year - 1
                m = 12
            else:
                y = x.year
                m = x.month - 1
            
            if x.month == 2 | x.month == 4 | x.month == 6 | x.month == 9 | x.month == 11:
                d = 30 + x.day - j
            else:
                d = 31 + x.day - j 
        
        else:
            d = x.day - j
            m = x.month
            y = x.year


        if d < 10:
            day = '{0}{1}'.format(0, d)
        else:
            day = x.day
        
        if m < 10:
            month = '{0}{1}'.format(0, m)
        else:
            month = x.month

        date = '{0}{1}{2}'.format(y, month, day)


        url = 'https://news.naver.com/main/list.naver?mode=LS2D&sid2={0}&sid1=105&mid=shm&date={1}&page=1'.format(i, date)
        site = requests.get(url, headers=headers)
        source_data = site.text

        count = source_data.count('width="106" height="72" alt=')

        print()
        print()
        print("시드 : {0}  날짜 : {1}\n".format(i, date))

        for k in range(count):
            pos1= source_data.find('width="106" height="72" alt=') + len('width="106" height="72" alt=')
            source_data = source_data[pos1+1:]

            pos2 = source_data.find('onError')
            extract_data = source_data[:pos2-2]

            source_data = source_data[pos2+1:]
            print(k+1, extract_data)

        
