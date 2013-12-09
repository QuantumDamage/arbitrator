import publiczne_api
import time
from blessings import Terminal
from time import strftime

cash_to_spent_in_pln = 200
term = Terminal()
pln_to_eur, eur_to_pln = publiczne_api.get_prices_euro_mbank() # komeasdf

print term.clear

screen_height = term.height

list_of_markets = [mtgox, bitcurex, localbitcoins]

while True:
	asks_mtgox, bids_mtgox = publiczne_api.get_prices("mtgox")
	asks_bitcurex, bids_bitcurex = publiczne_api.get_prices("bitcurex")
	bids_mtgox = list(reversed(bids_mtgox)) # we need to reverse list, because we are interested in highest bids
	#bids_bitcurex = list(reversed(bids_bitcurex))

	print term.move(1,1) + strftime("%H:%M:%S") + ": PLN to EUR: " + str(pln_to_eur) + ", EUR to PLN: " + str (eur_to_pln) + ". Cash to spent: " + str(cash_to_spent_in_pln) + " PLN."
	
	
	print term.move(3, 1) + "ASKs from MtGox:"
	print term.move(3, term.width / 2) + "BIDs from MtGox:"
	
	for counter in range(0, screen_height / 2 - 4):
		print term.move( 4 + counter,1) + str(asks_mtgox[counter][0]) +", "+ str(asks_mtgox[counter][1])
			
	for counter in range(0, screen_height / 2 - 4):
		print term.move( 4 + counter,term.width/2) + str(bids_mtgox[counter][0]) +", "+ str(bids_mtgox[counter][1])
	
	print term.move(screen_height / 2 + 1, 1) + "ASKs from bitcurex:"
	print term.move(screen_height / 2 + 1, term.width / 2) + "BIDs from bitcurex:"
	
	for counter in range(0, screen_height / 2 - 2):
		print term.move (screen_height / 2 + 2 + counter, 1) + str(asks_bitcurex[counter][0]) + ", " + str(asks_bitcurex[counter][1])
	
	for counter in range(0, screen_height / 2 - 2):
		print term.move (screen_height / 2 + 2 + counter, term.width / 2) + str(bids_bitcurex[counter][0]) + ", " +str(bids_bitcurex[counter][1])
	
	time.sleep(30)
