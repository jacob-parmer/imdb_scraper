"""
### Author: Jacob Parmer, Auburn University
###
### Last Updated: August 5th, 2020
###
""" 

import requests
import json
import logging
import re

class DataCollector:

	def __init__(self):
		self.list_of_shows = {}
	
	"""
	Given the name of a streaming service, add the names of original programming found on
	that streaming service to the list_of_shows dict.
	
	INPUTS: svc_name - name of streaming service to be searched (e.g. Netflix, Hulu, etc.)
		verbose - Turns logging on and off for the API connection

	OUTPUTS: list_of_shows[svc_name] - (mostly accurate) list of names of TV/Movies found on
					   desired streaming service

	"""
	def get_shows_from_service(self, svc_name, verbose=False):
			
		# formats data entry to match name of Wikipedia article to be grabbed
		# e.g. "https://en.wikipedia.org/wiki/List_of_Netflix_original_programming"
		svc_name_e = svc_name.replace(' ', '_')
		svc_name_e = svc_name_e[0].upper() + svc_name_e[1:]
		wiki_entry_name = "List_of_" + svc_name_e + "_original_programming"
	
		if verbose:
			logging.basicConfig()
			logging.getLogger().setLevel(logging.DEBUG)
			requests_log = logging.getLogger("requests.packages.urllib3")
			requests_log.setLevel(logging.DEBUG)
			requests_log.propogate = True

		S = requests.Session()

		URL = "https://en.wikipedia.org/w/api.php"

		PARAMS = {
			"action": "query",
			"prop": "revisions",
			"titles": wiki_entry_name,
			"rvprop": "content",
			"rvslots": "main",
			"formatversion": "2",
			"format": "json"
		}

		R = S.get(url=URL, params=PARAMS)
		DATA = R.json()

		pattern = r"\\'\\'\[\[(.{0,100})\]\]\\'\\'"
		titles = re.findall(pattern, str(DATA))	
		
		"""
		Some titles are formatted poorly from the wikipedia data, such as TV shows being
		displayed as ' Show Name (TV Series) | Show Name '. And commas are listed as
		\' instead of just '. The loop below fixes those issues.

		"""
		for i in range(0, len(titles)):
			if '|' in titles[i]:
				titles[i] = titles[i].split('|')[1]

			if r"\'" in titles[i]:
				titles[i] = titles[i].replace(r"\'",r"'")

		self.list_of_shows[svc_name] = titles	
