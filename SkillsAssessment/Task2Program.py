# Task 2
# Anne Taleb 21 March 2022
# parse the information for the given web server
#Use the HTTP headers as listed in the assessment.
import requests
from bs4 import BeautifulSoup
# Put the headers to search for in the data structure
interestHeaders =['Content-Type','Server','Date','Connection','Content-Length','X-Host','X-Forwarded-Server']

def main(url):
    try:
        # get the request for the specified url
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        response = requests.head(url)
         # prints the specific header tags from the dictionary
        for hdr in interestHeaders:
            try:
                headerVal = response.headers[hdr]
                print(hdr," = ",headerVal)
            except (AttributeError, KeyError) as errorMissing:
                print("Information is not available for", hdr)

        return response.status_code

    except (Exception) as err:
         print(err)

if __name__ == "__main__":
    url = "https://www.google.com/"
    main(url)