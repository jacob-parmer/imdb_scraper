from data_collection import DataCollector

def main():
	data = DataCollector()
	svc_name = "Netflix"

	data.get_shows_from_service(svc_name)

	print(data.list_of_shows[svc_name])

if __name__ == "__main__":
	main()
