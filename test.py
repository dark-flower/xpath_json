import requests
from lxml import etree
import re
import urllib.parse
import pymysql
sqldb = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='irsjax123',
    database='larry',
)
cursor = sqldb.cursor()
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
market_headers = {
    'authority': 'www.coingecko.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5,de;q=0.4',
    # Requests sorts cookies= alphabetically
    'cookie': 'hoveredProductsNav=true; clickedGeckoGuideModal=true; geckoGuideModalVersion=12; displayUnconvertData=false; cookie_notice_accept=1; geckoTableFdvStats=false; hoveredProductsNav=true; _session_id=d6831c5a0c8c36abfe5ff929abe78b98; _gid=GA1.2.1777546910.1667180925; __atuvc=2%7C43%2C1%7C44; __atuvs=635f29d0392149b9000; __cf_bm=JOPUsRLsPXuEK.QH2e0eWKfmzzZlxxdjq6Fv2r81esk-1667181900-0-AbjdbKQcU2UWLMpoxPxePhNBQjg2M8MKXifpbWGTgU0K713LGCo3eZWyh0EkYEXmIB0pBUn+R6tHkpXnd4HRZW8=; _ga=GA1.2.1004588217.1666184163; datadome=ABaQzu8I2xu8l2VK7-0y-vd3OU6aI76Gvs2L2Q9a~Qhr92Q~ZL9sbLEwZKS-gZf86-KPmRFrqmMqgOEOVOuODOV~pQWAwYJNlxABK~Y-pxXkUxgqB5BoH5_3KRhC~9I; _ga_LJR3232ZPB=GS1.1.1667180917.8.1.1667182024.0.0.0',
    'referer': 'https://www.coingecko.com/en/coins/polygon',
    'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
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
for page_num in range(1,11):
    print("第"+str(page_num)+"页")
    params = {
        'page':str(page_num),
    }
    suffix="insert into coingecko_demo  values "
    response = requests.get('https://www.coingecko.com/', params=params, cookies=cookies, headers=headers).text
    html=etree.HTML(response)

    list=html.xpath('.//tbody/tr')
    for item in list:
        print(item)
        coin_full_name=item.xpath('.//div[@class="tw-flex-auto"]/a/span[1]/text()')[0].strip().replace("'","")
        coin_name=item.xpath('.//div[@class="tw-flex-auto"]/a/span[2]/text()')[0].strip()

        coin_icon=item.xpath('.//td[contains(@class,"coin-name")]//img/@src')[0].strip()
        coin_detail_url="https://www.coingecko.com"+item.xpath('.//a/@href')[0].strip()
        detail_page=requests.get(coin_detail_url,headers=headers,cookies=cookies).text
        # detail_page=requests.get("https://www.coingecko.com/en/coins/polkadot",headers=headers,cookies=cookies).text
        detail_html=etree.HTML(detail_page)

        zh_link=detail_html.xpath('.//link[@hreflang="zh"]/@href')[0].strip()
        zh_name=urllib.parse.unquote(zh_link.split("/")[-1])
        coin_id = str(detail_html.xpath('.//input[@id="coin_id"]/@value')[0].strip())
        Website='|'.join([x.strip() for x in
                   detail_html.xpath(
                       './/div[contains(@data-target,"coins-information")]//span[contains(text(),"Website")]/parent::*//text()')
                   if x.strip() != '']).replace("Website|","").replace("'","")

        try:
            whiter_paper_link=detail_html.xpath('.//div[contains(@data-target,"coins-information")]//a[contains(text(),"Whitepaper")]/@href')[0]
        except:
            whiter_paper_link=""

        try:
            contract = '|'.join(set([x.strip() for x in
                                  detail_html.xpath(
                                      './/div[contains(@data-target,"coins-information")]//span[contains(text(),"Contract")]/parent::*//i/@data-address')
                                  if x.strip() != ''])).replace("Explorers|", "").replace("'", "")
        except:
            contract=''

        Explorers = '|'.join([x.strip() for x in
                   detail_html.xpath(
                       './/div[contains(@data-target,"coins-information")]//span[contains(text(),"Explorers")]/parent::*//@href')
                   if x.strip() != '']).replace("Explorers|","").replace("'","")

        Wallet = '|'.join([x.strip() for x in
                              detail_html.xpath(
                                  './/div[contains(@data-target,"coins-information")]//span[contains(text(),"Wallets")]/parent::*//@href')
                              if x.strip() != '']).replace("Wallets|", "").replace("'","")

        Community = '|'.join([sub_string(x.strip(),"//",".com")+'#'+x.strip() for x in
                           detail_html.xpath(
                               './/div[contains(@data-target,"coins-information")]//span[contains(text(),"Community")]/parent::*//a/@href')
                           if x.strip() != '']).replace("Community|", "").replace("'","")

        Search = '|'.join([x.strip() for x in
                              detail_html.xpath(
                                  './/div[contains(@data-target,"coins-information")]//span[contains(text(),"Search on")]/parent::*//text()')
                              if x.strip() != '']).replace("Search on|", "").replace("'","")

        github_link = '|'.join([x.strip() for x in
                           detail_html.xpath(
                               './/div[contains(@data-target,"coins-information")]//span[contains(text(),"Source Code")]/parent::*//a/@href')
                           if x.strip() != '']).replace("Source Code|", "").replace("'","")

        api_id = '|'.join([x.strip() for x in
                                detail_html.xpath(
                                    './/div[contains(@data-target,"coins-information")]//span[contains(text(),"API id")]/parent::*//text()')
                                if x.strip() != '']).replace("API id|", "").replace("'","")

        tags = '|'.join([x.strip() for x in
                                detail_html.xpath(
                                    './/div[contains(@data-target,"coins-information")]//span[contains(text(),"Tags")]/parent::*//text()')
                                if x.strip() != '']).replace("Tags|", "").replace("'","")

        try:
            security_link_part=detail_html.xpath('.//a[@data-event-category="click-coin-security-tab"]/@data-url')[0]
        except:
            security_link_part=""
            security_score=""
            onboarded_info=""
            audit_link=""
        if security_link_part!="":
            security_link = 'https://www.coingecko.com' + security_link_part
            security_page=requests.get(security_link,headers=headers,cookies=cookies).text
            security_html=etree.HTML(security_page)

            try:
                security_score=security_html.xpath('.//div[contains(text(),"Security Score")]/text()')[0]
            except:
                security_score=""
            try:
                onboarded_info=security_html.xpath('.//div[contains(text(),"Onboarded") or contains(text(),"Date reviewed")]/text()')[0]
            except:
                onboarded_info=""
            try:
                audit_link=security_html.xpath('.//a[contains(text(),"Audit Report") or contains(text(),"Security Details")]/@href')[0]
            except:
                audit_link=""


        market_page = requests.get('https://www.coingecko.com/en/coins/'+coin_id+'/markets_tab', headers=market_headers).text
        market_html=etree.HTML(market_page)
        market_list='|'.join(set([x.strip() for x in market_html.xpath('.//tbody[@data-target="gecko-table.paginatedShowMoreTbody"]//a/text()')]))


        values = " ('" + coin_full_name + "','" +coin_name + "','" +zh_name + "','" +coin_icon + "','" +coin_detail_url + "','" +Website + "','" +Explorers + "','" +Wallet + "','" +Community  + "','" +Search + "','" +github_link + "','" +api_id + "','" +tags+ "','" +security_score  + "','" +onboarded_info + "','" +audit_link + "','" +market_list + "','" +contract + "','" +coin_id+ "')"
        sql = suffix + values
        print(sql)
        cursor.execute(sql)
        sqldb.commit()

