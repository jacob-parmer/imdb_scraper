"""
### Author: Jacob Parmer, Auburn University
###
### Last Updated: August 10, 2020
""" 

import requests
import json
import logging
import re
import time
import concurrent.futures
from IMDb import TVShow

class DataCollector:

	def __init__(self):
		self.list_of_shows = {}
	
	"""
	Given the name of a streaming service, add the names of original programming found on
	that streaming service to the list_of_shows dict.
	
	INPUTS: svc_name (String) - name of streaming service to be searched
				    (e.g. Netflix, Hulu, etc.)
		verbose (Bool) - Turns logging on and off for the API connection

	OUTPUTS: list_of_shows[svc_name] (List) - (mostly accurate) list of names of TV/Movies
						   found on desired streaming service

	"""
	def get_titles_from_service(self, svc_name, verbose=False):
			
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
		shows = []
		for title in titles:
			imdb = TVShow(title)
			shows.append(imdb)

		self.list_of_shows[svc_name] = shows	
	
	"""
	Load show data for provided streaming service.

	INPUTS: svc_name (String) - Name of streaming service to get show data for
		verbose (Bool) - Turns logging on and off for runtime data
		multiprocessing (Bool) - Turns multiprocessing on and off, can be used to speed
					 up runtimes on higher-end machines

	OUTPUTS: list_of_shows[svc_name] - Data for shows in dict under svc_name


	"""
	def get_data_for_svc(self, svc_name, verbose=False, multiprocessing=False):
		
		if verbose:
			start_time = time.time()

		showlist = []
		results = []
		# todo: multiprocessing broken right now, fix!
		if multiprocessing:	
			with concurrent.futures.processPoolExecutor() as executor:
				for show in self.list_of_shows[svc_name]:
					results.append(executor.submit(
						       imdb.get_ratings_from_title, [verbose]))
		
					for f in concurrent.futures.as_completed(results):
						showlist.append(f)

		else:
			shows_to_remove = []
			for i, show in enumerate(self.list_of_shows[svc_name]):
				success = show.get_ratings_from_title(verbose=verbose)
				if not success:
					shows_to_remove.append(i)

			for j, item in enumerate(shows_to_remove):
				self.list_of_shows[svc_name].pop(item - j)
