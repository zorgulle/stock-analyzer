import requests
from lxml import etree
from io import StringIO

def parse_content(content):
    infos_to_xpath = {
        "price": '//*[@id="main-content"]/div/section[1]/header/div/div/div[1]/div[1]/div/div[1]/span[1]',
        "currency": '//*[@id="main-content"]/div/section[1]/header/div/div/div[1]/div[1]/div/div[1]/span[3]',
    }

    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(content), parser)
    return {i: tree.xpath(x)[0].text.strip() for i, x in infos_to_xpath.items()}

def get_stock_infos(stock_code):
    url = "https://boursorama.com/cours/%s" % (stock_code)
    response = requests.get(url)
    response.raise_for_status()
    infos = parse_content(response.text)
    return infos
    

if __name__ == '__main__':
    stocks_file = 'stocks.csv'
    import csv
    with open(stocks_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for index, row in enumerate(reader):
            print(row[0], row[1])
            if index == 0:
                continue
            infos = get_stock_infos(row[0]) 
            print(infos)
