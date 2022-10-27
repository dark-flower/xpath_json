import requests
from lxml import etree
import re
cookies = {
    '__cf_bm': 'Gab0_Riv5evxyqQ1MfzuqxYE8s74jDK8XmOAvS1gFG0-1666788421-0-Afe8pWb0i+26s+1aww9NQA0IqznAREfpnzMgPyaGBlGK+iwvbC2NIs9VSbmbeLSJVNrbRxZzysvDo1BKCHrOSBw=',
    'geckoTableFdvStats': 'false',
    '_session_id': '763ae15fccad24689827d573e48ecbaa',
    '_gid': 'GA1.2.71550751.1666788498',
    'cookie_notice_accept': '1',
    '_ga': 'GA1.2.1909421676.1666788497',
    '_gat_gtag_UA_49392197_1': '1',
    'datadome': 'dV8M28XRLucdSDNS_ksH0K~vklySo0Z6cIdWOawZIASw8unArY_x1vFt7sbf59cpA2-nbXOdci7Qu6yZ6~pnWpO0x.SU1lEuRNN72hzL8swW_iHgvStyoZR58.yRjja',
    '_ga_LJR3232ZPB': 'GS1.1.1666788497.1.1.1666788573.0.0.0',
}

headers = {
    'authority': 'www.coingecko.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5,de;q=0.4',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__cf_bm=Gab0_Riv5evxyqQ1MfzuqxYE8s74jDK8XmOAvS1gFG0-1666788421-0-Afe8pWb0i+26s+1aww9NQA0IqznAREfpnzMgPyaGBlGK+iwvbC2NIs9VSbmbeLSJVNrbRxZzysvDo1BKCHrOSBw=; geckoTableFdvStats=false; _session_id=763ae15fccad24689827d573e48ecbaa; _gid=GA1.2.71550751.1666788498; cookie_notice_accept=1; _ga=GA1.2.1909421676.1666788497; _gat_gtag_UA_49392197_1=1; datadome=dV8M28XRLucdSDNS_ksH0K~vklySo0Z6cIdWOawZIASw8unArY_x1vFt7sbf59cpA2-nbXOdci7Qu6yZ6~pnWpO0x.SU1lEuRNN72hzL8swW_iHgvStyoZR58.yRjja; _ga_LJR3232ZPB=GS1.1.1666788497.1.1.1666788573.0.0.0',
    'pragma': 'no-cache',
    'referer': 'https://www.coingecko.com/zh',
    'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
}
def sub_string(content,start,end):
    start_store = start
    end_store = end
    new_string = ""
    for item in start:
        if not re.search(r"[\.\^\$\*\+\?\[\]\|\{\}\(\)]", item) is None:
            new_string += "\\"
        new_string += item
    start = new_string
    new_string = ""
    for item in end:
        if not re.search(r"[\.\^\$\*\+\?\[\]\|\{\}\(\)]", item) is None:
            new_string += "\\"
        new_string += item
    end = new_string
    _str = ""

    try:
        _str = re.search(start + "(.|\n)*", content).group()
        if end != "":
            _str = re.search(start + "(.|\n)*?" + end, _str).group()
        _str = _str[len(start_store):len(_str)]
        if end != "":
            _str = _str[:len(_str)-len(end_store)]
    except:
        return ""
    return _str
params = {
    'page': '2',
}

response = requests.get('https://www.coingecko.com/', params=params, cookies=cookies, headers=headers).text
html=etree.HTML(response)

list=html.xpath('.//tbody/tr')
for item in list:
    print(item)
    coin_full_name=item.xpath('.//div[@class="tw-flex-auto"]/a/span[1]/text()')[0].strip()
    coin_name=item.xpath('.//div[@class="tw-flex-auto"]/a/span[2]/text()')[0].strip()
    coin_icon=item.xpath('.//td[contains(@class,"coin-name")]//img/@src')[0].strip()
    coin_detail_url="https://www.coingecko.com"+item.xpath('.//a/@href')[0].strip()
    detail_page=requests.get(coin_detail_url,headers=headers,cookies=cookies).text
    detail_html=etree.HTML(detail_page)
    Website=','.join([x.strip() for x in
               detail_html.xpath(
                   './/div[contains(@data-target,"coins-information")]//span[contains(text(),"Website")]/parent::*//text()')
               if x.strip() != '']).replace("Website,","")
    Explorers = ','.join([x.strip() for x in
               detail_html.xpath(
                   './/div[contains(@data-target,"coins-information")]//span[contains(text(),"Explorers")]/parent::*//text()')
               if x.strip() != '']).replace("Explorers,","")

    Wallet = ','.join([x.strip() for x in
                          detail_html.xpath(
                              './/div[contains(@data-target,"coins-information")]//span[contains(text(),"Wallets")]/parent::*//text()')
                          if x.strip() != '']).replace("Wallets,", "")

    Community = ','.join([x.strip() for x in
                       detail_html.xpath(
                           './/div[contains(@data-target,"coins-information")]//span[contains(text(),"Community")]/parent::*//a/@href')
                       if x.strip() != '']).replace("Community,", "")

    Search = ','.join([x.strip() for x in
                          detail_html.xpath(
                              './/div[contains(@data-target,"coins-information")]//span[contains(text(),"Search on")]/parent::*//text()')
                          if x.strip() != '']).replace("Search on,", "")

    github_link = ','.join([x.strip() for x in
                       detail_html.xpath(
                           './/div[contains(@data-target,"coins-information")]//span[contains(text(),"Source Code")]/parent::*//a/@href')
                       if x.strip() != '']).replace("Source Code,", "")

    api_id = ','.join([x.strip() for x in
                            detail_html.xpath(
                                './/div[contains(@data-target,"coins-information")]//span[contains(text(),"API id")]/parent::*//text()')
                            if x.strip() != '']).replace("API id,", "")

    tags = ','.join([x.strip() for x in
                            detail_html.xpath(
                                './/div[contains(@data-target,"coins-information")]//span[contains(text(),"Tags")]/parent::*//text()')
                            if x.strip() != '']).replace("Tags,", "")
    print(1)
