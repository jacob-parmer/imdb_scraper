"""
### Author: Jacob Parmer, Auburn University
### 
### Last Updated: August 11, 2020
"""

import numpy as np
import matplotlib.pyplot as plt
import random as rnd
from IMDb import TVShow

class DataDisplay:

	def __init__(self, data):
		self.data = data
		self.arr = [[]]
		self.fig = None
		self.ax = None

        """
        Converts the show data from self.data to a 2d array of ratings, with each column 
        representing a streaming service, and each row representing a show in the streaming
        service.

        INPUTS: self.data (DataCollector) - data containing streaming services, shows, ratings.

        OUTPUTS: self.arr (List of Lists) - 2d array of ratings

        """
	def prepare(self):
		x = []
		y = []
		for svc, shows in self.data.items():
			for show in shows:
				y.append(show.rating)

			x.append(y)
			y = []	
	        
		self.arr = x

        """
        Builds plots figure and axes.

        INPUTS: N/A

        OUTPUTS: self.fig (Matplotlib Figure)
                 self.ax (Matplotlib Axes)
    
        """
	def build_plot(self):
		self.fig = plt.figure(figsize=plt.figaspect(2.0))
		self.ax =  self.fig.add_subplot()

		
        """
        Displays 2d data array in a boxplot. Could probably use some more work to better display
        this data.

        INPUTS: self.ax (Matplotlib Axes) - Axes to use for boxplot
                self.arr (List of Lists) - 2d array of data to show

        OUTPUTS: Opens a display window to show boxplot

        """
	def add_data(self):
		self.ax.boxplot(self.arr)
		plt.show()

        """
        Generates random list of streaming services and associated shows. These shows only
        contain data for the title and the rating. Can be used for testing purposes.


        INPUTS: N/A

        OUTPUTS: data (Dict) - Dict of shows per streaming service as:
                               data[service] = [list of shows]


        """
	def gen_random_data():
		streaming_services = ["Amazon", "Netflix", "Hulu", "Disney+", "Quibi",
				      "Apple TV+"]

		
		num_of_services = rnd.randrange(len(streaming_services)) + 1
		data = {}
		sel_services = rnd.sample(streaming_services, k=num_of_services)
		shows = []
		for service in sel_services:
		
			for j in range(rnd.randrange(100)):
				show = TVShow(title=j)
				show.rating = rnd.normalvariate(7.0, 1.0)
				shows.append(show)
			
			data[service] = shows
			shows = []	
			
		return data
