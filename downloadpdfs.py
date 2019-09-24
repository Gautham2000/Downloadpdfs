import os
import sys
import urllib.error
import urllib.parse

import requests
from bs4 import BeautifulSoup as BS


try:
    #to make it authentic to the site
    headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

  

    url = "https://papers.gceguide.xyz/A%20Levels/Biology%20%289700%29" #Enter the url here

    download_folder = "/Users/" # Enter your download folder path


    request = requests.get(url)
    print (request.status_code)
    soup = BS(request.content,'html.parser')

    i = 0
    #print(soup.find_all('a'))

    for tag in soup.find_all('a',href=True):

        #find <a> tags with href so you know its for urls
        #tag['href'] gives the link

        #print(tag['href'])

        # combining base url with fragment to get full download link
        tag['href'] = urllib.parse.urljoin(url, tag['href'])
       # print (tag['href'])
        #getting the extension from the url filename (splitext) and checking if it's .pdf
        #print (os.path.splitext(os.path.basename(tag['href']))[1])
        if os.path.splitext(os.path.basename(tag['href']))[1] == '.pdf':
            current = requests.get(tag['href'],stream = True)

            print ("Downloading: %s" % (os.path.basename(tag['href'])))
            print (os.path.basename(tag['href']))

            f = open(download_folder + os.path.basename(tag['href']), "wb")
            for chunk in current.iter_content(chunk_size=1024*1024):
                if chunk:
                    f.write(chunk)

            i += 1

    print ("Downloaded %d files" % (i))
    input("Press any key to exit")

except KeyboardInterrupt:
    print ("Exiting...")
    sys.exit(1)

except urllib.error.URLError as e:
    print ("Could not get information from the server!!\n Check the site")
    sys.exit(2)

except:
    print ("Contact developer")
    sys.exit(3)
