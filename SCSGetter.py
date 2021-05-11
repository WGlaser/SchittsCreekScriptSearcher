from bs4 import BeautifulSoup
import requests
import os

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

url = "https://subslikescript.com/series/Schitts_Creek-3526078"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

links = []
for link in soup.find_all('a'):
	#print(link.get('href'))
	if(link.get('href').find("episode")>0):
		links.append("https://www.subslikescript.com/"+link.get('href'))

#links now has links to each episode
testLink = []
testLink.append(links[0]) #quick test for only episode s1e1
for episodeLink in links:
	print(episodeLink[61:])
	textFileName = episodeLink[61:]+".txt"
	textFileName = textFileName.replace("/","_")
	print(textFileName)
	req = requests.get(episodeLink, headers)
	soup = BeautifulSoup(req.content, 'html.parser')
	script = soup.find_all(class_="full-script")
	for x in script:
		#dirname = os.path.dirname(textFileName)
		#os.makedirs(dirname)
		text_file = open(textFileName, "x")
		n = text_file.write(x.get_text().lower())
		text_file.close()
		



