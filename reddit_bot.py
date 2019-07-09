from praw import *
#from menu_generator import *

reddit = Reddit('bot1')
sub = reddit.subreddit('krunkerio')

for post in sub.top(limit=20):
	if any(n in ['nice', 'man', 'Update'] for n in post.title.split(' ')):
			post.reply('hello fellow friends!!!')