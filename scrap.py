from lxml import html
import requests
import pandas as pd
sic_code_list = []
card_title_list = []
card_text_list = []
for sic_code in sic_codes:
    page = requests.get('https://mcc-codes.ru/search?q='+str(sic_code))
    tree = html.fromstring(page.content)
    card_title = tree.xpath('//h4[@class="card-title"]/text()')
    card_text = tree.xpath('//p[@class="card-text"]/text()')
    sic_code_list.append(card_title[0][4:8])
    card_title_list.append(card_title[0][10:])
    card_text_list.append(card_text[0])
df = pd.DataFrame({'sic_code':sic_code_list, 'title':card_title_list, 'text':card_text_list})
