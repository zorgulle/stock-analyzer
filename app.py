import requests

def get_stock_infos(stock_code):
    url = "https://boursorama.com/cours/%s" % (stock_code)
    print("Calling: %s" % url)
    response = requests.get(url)
    response.raise_for_status()
    return response.content
    

if __name__ == '__main__':
    stocks_file = 'stocks.csv'
    import csv
    with open(stocks_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for index, row in enumerate(reader):
            print(row[0], row[1])
            if index == 0:
                continue
            get_stock_infos(row[0]) 
