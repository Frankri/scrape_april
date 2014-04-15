import requests

# hier namen der Dateiname der Liste eingeben (started 3/2014)
lnk_list = open('phish_guanjia/test_list.txt')

error_counter = 0
link_counter = 0

results = open('phish_guanjia/results.txt')

for e in lnk_list:
	link_counter += 1
	try:
		r = requests.get(e, timeout=10)
		print e, link_counter, r.status_code, r.history
		if 'credit' in e:
			results.write[e, '\n']

	except Exception as e:
		error_counter += 1
		print repr(e), 'Errors: ', error_counter
