"""
### Author: Jacob Parmer, Auburn University
###
### Last Updated: August 10, 2020
"""
import csv
import time

class TVShow:

	def __init__(self, title):
		self.title = title
		self.titleId = ""
		self.isAdult = ""
		self.startYear = ""
		self.genres = []
		self.rating = 0.0
		self.numOfVotes = 0

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
				if self.title == row[3]:
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

	"""
	Given a show's unique IMDb title ID, get the shows rating and the number of votes it 
	received from ratings dataset.

	INPUTS: self.titleId (String) - IMDb's Id for the title, (e.g. tt1826940)
		verbose (Bool) - Turns logging on and off for runtime data

	OUTPUTS: self.rating (Double) - IMDb's rating for the show
		 self.numOfVotes (Int) - Total number of votes show has received

	"""
	def get_ratings_from_id(self, verbose=False):
		if self.titleId == "":
			return
		
		if verbose:
			start_time = time.time()

		found = False
		with open('data/title.ratings.tsv', newline='') as csvfile:
			spamreader = csv.reader(csvfile, delimiter="\t")
	
			for row in spamreader:
				if self.titleId == row[0]:
					self.rating = row[1]	
					self.numOfVotes = row[2]
					found = True
					break

		if verbose:
			if found == False:
				print(f"No ratings found for ID: {self.titleId}. Scan took {time.time() - start_time} seconds")
			else: 
				print(f"titleId: {self.titleId}, rating: {self.rating}, Scan time: {time.time() - start_time} seconds")


	"""
	Given a show title, get all possible show data, combining get_info_from_title and
	get_ratings_from_id.
	
	INPUTS: self.title (String) - Name of the show to be searched through for IMDb's dataset
		verbose (Bool) - Turns logging on and off for runtime data

	OUTPUTS: self.titleId (String) - IMDb's Id for the title (e.g. tt1826940)
		 self.isAdult (String) - IMDb's label for adult shows, 1 if adult, 0 if not
		 self.startYear (String) - Year the show began airing
		 self.genres (List) - List of genres provided by IMDb
		 self.rating (Double) - IMDb's rating for the show
		 self.numOfVotes (Int) - Total number of votes show has received
		 success (Bool) - Returns true if rating was successfully set, false if not
	"""
	def show_data_from_title(self, verbose=False):
		success = False

		self.get_info_from_title(verbose=verbose)
		if self.titleId != "":
			self.get_ratings_from_id(verbose=verbose)
			if self.rating != 0.0:
				success = True

		return success
