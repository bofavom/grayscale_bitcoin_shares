import scrapy
from datetime import datetime, timedelta
from . import github_uploader as uploader

class GrayscaleScrapy(scrapy.Spider):
    name = 'grayscale'
    start_urls = ['https://grayscale.co/bitcoin-trust/']

    shares = None
    btcPerShare = None

    FILENAME = 'grayscale_bitcoin.csv'


    def parse(self, response):
        table = response.xpath('//table[@class="overview-data"]')
        rows = table.xpath('tr')

        for row in rows:
            if row.xpath('td/text()').get() == 'Shares Outstanding':
                unformattedShares = row.xpath('td[2]/text()').get()
                unformattedSharesWithoutSymbol = unformattedShares[:-1]
                unformattedSharesWithoutCommas = unformattedSharesWithoutSymbol.replace(',', '')
                self.shares = int(unformattedSharesWithoutCommas)

            if row.xpath('td/text()').get() == 'Bitcoin per Share':
                unformattedBtcPerShare = row.xpath('td[2]/text()').get()
                unformattedBtcPerShareWithoutSymbol = unformattedBtcPerShare[:-1]
                self.btcPerShare = float(unformattedBtcPerShareWithoutSymbol)

            if self.shares is not None and self.btcPerShare is not None:
                self.save()
                break


    def save(self):
        filename = self.FILENAME
        date = datetime.today() - timedelta(days = 1)
        dateString = date.strftime('%d/%m/%Y')
        line = dateString + ',' + str(self.shares) + ',' + str(self.btcPerShare) + '\n'

        with open(filename, 'a') as f:
            f.write(line)
        
        f.close()
        self.updateGithub()

    
    def updateGithub(self):
        uploader.updateFile(self.FILENAME)
