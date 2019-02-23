import requests as req
from bs4 import BeautifulSoup as BS
from sys import argv

def get_scrap(link, tag): #put os.path.isfile()?
	response = req.get(link, timeout=5)
	if not response.ok:
		return "Error trying to acess %s!\nStatus: %d" % (link, response.status_code)
	content = BS(response.content, 'html.parser')
	words = set()
	for word in content.select(tag):
		for x in word.text.split('\n'):
			if x != '':
				words.add(x)
	return list(words)

if __name__ == '__main__':
	#link = 'http://www.fabpedigree.com/james/mathmen.htm'
	link = argv[1]
	tag = argv[2]
	print('Scraped Data\n%s' % (75*'-'))
	names = get_scrap(link, tag)
	for name in names:
		print(name + ' ' + str(names.count(name)))
	print(names, len(names))