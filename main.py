from data_collection import DataCollector
from IMDb import TVShow 
import concurrent.futures
import time
import argparse

def main(args):

	data = DataCollector()
	svc_name = "Disney+"

	data.get_shows_from_service(svc_name)

	if args.verbose:
		start_time = time.time()

	list_of_shows = []
	results = []
	if args.multiprocessing:
		with concurrent.futures.ProcessPoolExecutor() as executor:
			for show in data.list_of_shows[svc_name]:
				imdb = TVShow(show)
				results.append(executor.submit(imdb.get_info_from_title,
							       [args.verbose]))

				for f in concurrent.futures.as_completed(results):
					list_of_shows.append(f)
	
	else:
		for show in data.list_of_shows[svc_name]:
			imdb = TVShow(show)
			imdb.get_info_from_title(verbose=True)
			list_of_shows.append(imdb)
	
	if args.verbose:	
		print("Title.basics.tsv fully searched in {time.time() - start_time} seconds")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--verbose", "-v", help="Display debugging logs", 
			    action="store_true")
	parser.add_argument("--multiprocessing", "-m",
			    help="Use multiple CPUs, reduces wait time on higher end devices",
			    action="store_true")
	args = parser.parse_args()
	main(args)
