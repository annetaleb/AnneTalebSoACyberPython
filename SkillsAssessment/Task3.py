#  TASK 3
#  Anne Taleb
#  21 March 2022
#  Version 1.0
#  This program reads the ServerList file and for each
#  line searches the url for specific HTTP headers
#  The headers are considered headers that show too much information about the server and
#  are there web site security configuration headers
import requests
from bs4 import BeautifulSoup
interestHeaders =['Content-Type','Server','Date','X-Forwarded-Host','X-Host','X-Forwarded-Server','Forwarded','X-Powered-By','Strict-Transport-Security']
def process_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    response = requests.head(url)
    # prints the specific header tags from the dictionary
    for hdr in interestHeaders:
        try:
            headerVal = response.headers[hdr]
            print(hdr, " = ", headerVal)
        except (AttributeError, KeyError) as errorMissing:
            print("Information is not available for", hdr)
def main():
    try:
        #Open the file
        filename = 'ServerList.txt'
        fileServer=open(filename,"r")
        line = fileServer.readline().strip()
        # for each record /line in the file call the process_data function
        while line != '':
            print(line)
            url = line
            process_data(url)
            print('******************')
            line = fileServer.readline()

        #close the file - all processing has finished
        fileServer.close()
    except IOError:
        #file error checking is handled here
        print('An error occurred trying to read file', filename)
        print('Please check this file exists and contains the URLs to check')
#Call the main function
main()

