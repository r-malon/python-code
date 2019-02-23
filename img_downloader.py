from requests import get
import os

def download_img(url, path):
	with open(path, 'wb') as f:
		f.write(get(url).content)

if __name__ == '__main__':
	path = input("Write the new image path: ")
	url = input("Write the image url: ")
	download_img(url, path)
	os.system('pause')