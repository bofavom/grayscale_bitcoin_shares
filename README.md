# Grayscale Bitcoin Spider
## Overview
This repository contains a little script for scrape the number of shares outstanding in Grayscale.
The purpose of scrape and save this information is for know how many bitcoins are bought by Grayscale.

## Working
The script scrape the needed information from the corresponding website. Then, it saves that info in a CSV file, so you can view it like a calc sheet.  
Besides, when the CSV is saved, it is uploaded to a Github repository.  

If you don't want to run by yourself this script, you can see the next CSV. It's generated and updated by a Raspberry Pi every day at 2:00 UTC.
https://github.com/bofavom/grayscale_bitcoin_shares/blob/master/grayscale_bitcoin.csv

## Requirements
* Python
* Scrapy
* PyGithub

## Setup your own environment
1. Install Scrapy and PyGithub.  
https://docs.scrapy.org/en/latest/intro/install.html  
https://pygithub.readthedocs.io/en/latest/introduction.html#download-and-install
2. Clone this repository.
```
git clone https://github.com/bofavom/grayscale_bitcoin_shares.git
```
3. If you want to upload and keep updated your CSV in your own Github repository, change your access token and repository name in file grayscale/spiders/github_uploader.py  
If not, you can remove the 45th line *self.updateGithub()* in file grayscale/spiders/grayscale_spider.py
4. Now, you'll want to run this script periodically. Use crontab for that. An example would be:
```
crontab -e
0 2 * * * cd /home/user/grayscale_bitcoin_shares && /home/user/.local/bin/scrapy crawl grayscale
```
