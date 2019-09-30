import sys
import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import urljoin

def main(url):
    # Initial page request and link counter
    try:
        res = requests.get(url)
    except:
        print('ERROR: URL is not a valid page')
        return
    counter = 1

    # If initial request is ok, proceed
    if res.ok:
        # Parse page and create a list of all links
        page = BS(res.text, 'html.parser')
        links = page.find_all('a')

        print('Links on ' + url + ' :')
        print()

        # Iterate through all links
        for link in links:
            # Ignoring mailto links
            if not link.get('href').startswith('mailto'):
                # Secondary page request
                link_res = requests.get(urljoin(url, link.get('href')))

                # If secondary request is ok, proceed
                if link_res.ok:
                    # Print a valid link message
                    print(str(counter) + ' - ' + link.get('href') + ' -- valid link')
                else:
                    # Print an invalid link message
                    print(str(counter) + ' - ' + link.get('href') + ' -- broken link')

                # Increment link counter
                counter += 1
    # Otherwise, print error
    else:
        print('ERROR: URL is not a valid page')

if __name__ == '__main__':
    # Check for URL parameter
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print('ERROR: Missing URL argument.')