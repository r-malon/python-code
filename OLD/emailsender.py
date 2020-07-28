from smtplib import SMTP

x = 1 # int(input('How many? '))
content = input('Enter your message: ')
subject = input('Enter the subject: ')
sender = input('Enter your e-mail: ')
password = input('Enter your password: ')
recipient = input('Enter the recipient: ')
message = f'''From: <{sender}>
To: <{recipient}>
Subject: {subject}
Content-type: text/html
MIME-Version: 1.0

<h1>{content}</h1>
'''

for i in range(x):
	try:
		server = SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(sender, password)
		server.sendmail(sender, recipient, message)
		print('%dº e-mail sent' % i + 1)
		server.quit()
	except Exception as e:
		print('Error: ', e)