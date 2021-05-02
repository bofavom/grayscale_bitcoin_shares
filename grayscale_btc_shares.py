import cloudscraper
from lxml import html
from datetime import datetime, timedelta
from github_uploader import updateFile

def checkGrayscale():
     try:
        grayscale_csv = 'grayscale_bitcoin.csv'
        scraper = cloudscraper.create_scraper()
        r = scraper.get("https://grayscale.com/products/grayscale-bitcoin-trust/")
        tree = html.fromstring(r.text)
        shares = tree.xpath('//span[@data-title="Shares Outstanding"]')[0].text[:-1].replace(',', '')
        btcpershare = tree.xpath('//span[@data-title="Token per Share"]')[0].text[:-1].replace(',', '')
        

        date = datetime.today() - timedelta(days = 1)
        dateString = date.strftime('%d/%m/%Y')
        line = dateString + ',' + str(shares) + ',' + str(btcpershare) + '\n'

        with open(grayscale_csv, 'a') as f:
            f.write(line)        
        f.close()

        updateFile(grayscale_csv)

     except Exception as err:
        print ("Error: {err}")

checkGrayscale()
