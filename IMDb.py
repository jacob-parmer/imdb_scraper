"""
### Author: Jacob Parmer, Auburn University
###
### Last Edited: August 7, 2020
"""
import csv
import time

class TVShow:

	def __init__(self, title, chunksize = 100000):
		self.title = title
		self.titleId = ""
		self.isAdult = ""
		self.startYear = ""
		self.genres = []
		self.rating = 0.0
		self.chunksize = chunksize

	"""
	Given a show's title, grab show's Id, if it's an adult show, what year it started, and
	what genres it is listed as in IMDb's dataset. 

	INPUTS: self.title (String) - Inherited from object, name of the show to be searched
				      for in IMDb's dataset
		verbose (Bool) - Turns logging on and off for runtime data

	OUTPUTS: self.titleId (String) - IMDb's Id for the title, (e.g. tt1826940)
		 self.isAdult (String) - IMDb's label for adult shows, 0 if not, 1 if it is
		 self.startYear (String) - Year the show began airing
		 self.genres (List) - list of genres provided by IMDb

	"""
	def get_info_from_title(self, verbose=False):
		
		if verbose:
			start_time = time.time()
		
		found = False
		with open('data/title.basics.tsv', newline='') as csvfile:
			spamreader = csv.reader(csvfile, delimiter="\t")	
		
	
			for row in spamreader:
				if self.title == row[3] and row[1] == 'tvSeries':
					self.titleId = row[0]
					self.isAdult = row[4]
					self.startYear = row[5]
					self.genres = row[8].split(',')
					found = True
					break		
				

		if verbose:
			if found == False:
				print(f"{self.title} not found. Scan took: {time.time() - start_time} seconds ")
			else:
				print(f"{self.title} found in {time.time() - start_time} seconds")
	
