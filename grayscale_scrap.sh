#!/bin/sh
/usr/bin/python3 grayscale_btc_shares.py
git add grayscale_bitcoin.csv
git commit -m "Update"
git push origin master
