import smtplib as sm
x = int(input('qnts e-mails vc vai mandar? '))
content = input('digite sua msg: ')
subject = input('qual o assunto: ')
send = input('digite seu e-mail: ')#jailsoncomemilf@gmail.com, kronergamer@gmail.com,  server.ehlo()
pwd = input('digite sua senha: ')
get = input('agora o destinatario: ')
msg = '''From: <%s>
To: <%s>
Subject: %s
Content-type: text/html
MIME-Version: 1.0

<h1>%s</h1>
''' % (send, get, subject, content)
for i in range(x):
    try:
        server = sm.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(send, pwd)
        server.sendmail(send, get, msg)
        print('enviado o %dº e-mail' % i+1)
        server.quit()
    except sm.SMTPException:
        print('erro')
