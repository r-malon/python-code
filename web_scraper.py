from requests import get
from bs4 import BeautifulSoup
from sys import argv

def scrap(link, tag):
	response = get(link, timeout=5)
	if not response.ok:
		return "Error trying to acess %s!\nStatus: %d" % (link, response.status_code)
	content = BeautifulSoup(response.content, 'html.parser')
	words = set()
	for word in content.select(tag):
		for x in word.text.split('\n'):
			if x != '':
				words.add(x)
	return list(words)

if __name__ == '__main__':
	link = argv[1] # 'http://www.fabpedigree.com/james/mathmen.htm'
	tag = argv[2]
	print(f"Scraped Data\n{75 * '-'}")
	names = scrap(link, tag)
	for name in names:
		print(f"{name}, Count: {names.count(name)}")
	print(names, len(names))