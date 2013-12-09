import time
import csv
import os.path
import urllib2
import json

def get_prices_euro_mbank():
	plik = "mbank.csv" 
	url = "http://www.mbank.pl/ajax/currency/getCSV/?id=0"
	
	teraz = time.time()
	data_pliku =  os.path.getmtime("mbank.csv")
	
	if teraz - data_pliku > 86400: 	#pobierz nowy jesli starszy niz 24h
		response = urllib2.urlopen(url)	 
		#open the file for writing
		fh = open(plik, "w")
		# read from request while writing to file
		fh.write(response.read())
		fh.close()
		print "pobieranie nowego pliku EURO"
	else:
		print "nie pobieram nowego pliku EURO"
		pass
		
	with open('mbank.csv', 'rb') as mbank:
	    reader = csv.reader(mbank,delimiter=';')
	    for row in reader:
			if row[2] == "EURO":
				return row[4], row[5]

def get_prices(market):
	"""Funkcja majaca za zadanie pobrac oferty skupu(BID) oraz sprzedazy(ASK) i zebrac je w sensowna struktre danych. Argumentem jest nazwa gieldy."""
	lista_askow = []
	lista_bidow = []
	
	if (market == "mtgox"):
		f = urllib2.urlopen('http://data.mtgox.com/api/1/BTCPLN/depth/fetch')
		json_string = f.read()
		parsed_json = json.loads(json_string)
		for entry in parsed_json['return']['asks']:
			porcja = [float(entry['price']), float(entry ['amount']), "mtgox"]	
			lista_askow.append(porcja)
		for entry in parsed_json['return']['bids']:
			porcja = [float(entry['price']), float(entry ['amount']), "mtgox"]	
			lista_bidow.append(porcja)	
	elif (market == "bidexreme"):
		f = urllib2.urlopen('https://bidextreme.pl/API/PLN/orderbook.json')
		json_string = f.read() 
		parsed_json = json.loads(json_string)
		for entry in parsed_json['asks']:
			porcja = [float(entry[0]), float(entry[1]), "bidextreme"]
			lista_askow.append(porcja)
		for entry in parsed_json['bids']:
			porcja = [float(entry[0]), float(entry[1]), "bidextreme"]
			lista_bidow.append(porcja)
	elif (market == "localbitcoins"):
		f = urllib2.urlopen('https://localbitcoins.com/bitcoincharts/PLN/orderbook.json')
		json_string = f.read()
		parsed_json = json.loads(json_string)
		for entry in parsed_json['asks']:
			porcja = [float(entry[0]), float(entry[1])/float(entry[0]), "localbitcoins"]
			lista_askow.append(porcja)
		for entry in parsed_json['bids']:
			porcja = [float(entry[0]), float(entry[1])/float(entry[0]), "localbitcoins"]
			lista_bidow.append(porcja)
	elif (market == "bitcurex"):
		f = urllib2.urlopen('https://pln.bitcurex.com/data/orderbook.json')
		json_string = f.read() 
		parsed_json = json.loads(json_string)
		for entry in parsed_json['asks']:
			porcja = [float(entry[0]), float(entry[1]), "bitcurex"]
			lista_askow.append(porcja)
		for entry in parsed_json['bids']:
			porcja = [float(entry[0]), float(entry[1]), "bitcurex"]
			lista_bidow.append(porcja)

	return lista_askow, lista_bidow
