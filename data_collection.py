# this script collects data using unirest and the IMDb API

import unirest;

def response_collector(title):
    response = unirest.get("https://ivaee-internet-video-archive-entertainment-v1.p.rapidapi.com/entertainment/search/" + title,
        headers={
            "X-RapidAPI-Host": "ivaee-internet-video-archive-entertainment-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "9698ed2e51msh87cd62c4ee356d1p1d6566jsn61d4c61fe625",
            "Content-Type": "application/json"
        }
    )

    print(response)


def main():
    response_collector("Jaws")
    
if __name__ == "__main__":
    main()
