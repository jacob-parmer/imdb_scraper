"""
### Author: Jacob Parmer, Auburn University
###
### Last Updated: August 10, 2020
"""


from data_collection import DataCollector
from IMDb import TVShow 
import time
import argparse
from pudb import set_trace
from data_display import DataDisplay

def main(args):

	#set_trace()
		
	data = DataCollector()
	svc_names = ["Amazon", "Netflix", "Hulu"]
	
	if args.verbose:
		start_time = time.time()

	for svc_name in svc_names:
		data.get_titles_from_service(svc_name)
		data.get_data_for_svc(svc_name, verbose=args.verbose)
	

	if args.verbose:
		print(f"Data for svc: {svc_name} collected in {time.time() - start_time} seconds\n\n")

	for show in data.list_of_shows[svc_name]:
		print(f"{show.title}, {show.titleId}, {show.rating}, {show.numOfVotes}")
	
	
	
	#data = DataDisplay.gen_random_data()
	
	display = DataDisplay(data)
	
	display.prepare()
	display.build_plot()
	display.add_data()
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--verbose", "-v", help="Display debugging logs", 
			    action="store_true")
	parser.add_argument("--multiprocessing", "-m",
			    help="Use multiple CPUs, reduces wait time on higher end devices",
			    action="store_true")
	args = parser.parse_args()
	main(args)
