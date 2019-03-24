from requests import get
from bs4 import BeautifulSoup as BS
from sys import argv

def get_scrap(link, tag):
	response = get(link, timeout=5)
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
	print(f"Scraped Data\n{75 * '-'}")
	names = get_scrap(link, tag)
	for name in names:
		print(f"{name}, Count: {names.count(name)}")
	print(names, len(names))