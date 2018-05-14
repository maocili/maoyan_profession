import requests
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
html = requests.get('http://maoyan.com/films?showType=2',headers=headers).text
et = etree.HTML(html)
xp = et.xpath('//div[@class="channel-detail movie-item-title"]/a/text()')
xp1 = et.xpath('//span[@class="stonefont"]/text()')

eot_url = 'http://' + et.xpath('//style/text()')[0].split(';')[1].split()[1].split('//')[1].replace("')",'')
move_item = {}
item = move_item
item['eot_url'] = eot_url
edit_dict = eot_to_dict(item)

print("解析想看人数",eot_url)