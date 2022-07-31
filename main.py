import requests
from bs4 import BeautifulSoup as BS

#url = 'https://travelata.ru/search#?fromCity=2&toCountry=92&dateFrom=19.08.2022&dateTo=19.08.2022&nightFrom=7&nightTo=7&adults=2&hotelClass=all&meal=all&priceFrom=6000&priceTo=50000000&sid=v3seqfbmq7&sort=recommend&f_minPrice=100&f_maxPrice=10000000&f_best=true'
#url = 'http://mignews.com/mobile'
url = 'https://stopgame.ru/review/new/izumitelno'
page = requests.get(url)
print(page.status_code)

filteredNews = []
allNews = []

soup = BS(page.text, "html.parser")
#print(soup)
allNews = soup.findAll('a', '_subnav__item_1qf5u_1')   #, class_='_card__title_12zp8_1'  ,'_subnav__item_1qf5u_1'
#print(allNews)

for data in allNews:
    if data.find('span') is not None:    #, class_='time2 time3'
        filteredNews.append(data.text)

for data in filteredNews:
    print(data)

'''
html = BS(r.content, 'html.parser')
#4 31
for el in html.select(".items > .article-summary"):
    title = el.select('.caption > a')
    print( title[0].text )


    <a href="/show/129157/stray_review" class="_card__title_12zp8_1 _card__title--has-subtitle_12zp8_1"> Stray: Обзор</a>

    <a href="/show/128939/arcadegeddon_review" class="_card__title_12zp8_1 _card__title--has-subtitle_12zp8_1"> Arcadegeddon: Обзор</a>
    '''