import csv
import os
import urllib
import requests
import urllib.request
from bs4 import BeautifulSoup


def make_soup(url):
	thepage = urllib.request.urlopen(url)
	soupdata  = BeautifulSoup(thepage, "html.parser")
	return soupdata
	
saved_finance_data = ""
soup = make_soup("https://in.finance.yahoo.com/quote/SBIN.BO/history?p=SBIN.BO")
for record in soup.find_all('tr'):
	finance_data = ""
	for data in record.find_all('td'):
		for text_data in data.find_all('span'):			
			if "," in text_data.text:
				text_data = text_data.text.replace(",", "")
				finance_data = finance_data+ "," + text_data		
			else:
				finance_data = finance_data+ "," + (text_data.text)
	if len(finance_data) <= 96 :				
		saved_finance_data = saved_finance_data + "\n" + finance_data[1:]

header_row = "Date,Open,High,Low,Close,Adj.Close,Volume" 
output_csv = open(os.path.expanduser("/home/prachi/Desktop/SBI_data.csv"), "wb")
output_csv.write(bytes(header_row, encoding ="ascii", errors = "ignore"))
output_csv.write(bytes(saved_finance_data, encoding ="ascii", errors = "ignore"))


