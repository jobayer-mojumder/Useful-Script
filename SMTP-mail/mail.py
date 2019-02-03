import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail(email):
    recevier = email
    SUBJECT = 'Bangladesh Clean Energy Summit 2019'
    sender = 'test@idcol.org'
    password = 'Asdf1234'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = sender
    msg['To'] = email

    html = """
    <html>
    <head></head>
    <body>
        <p>Bangladesh, with its economy steadily growing at annual rate of above 7%, is fast transposing to a large energy consuming country in the South Asia region.</p>
        <p><img src="http://datacraftbd.com/qrcode/image.png" style="width:200px" /></p>
    </body>
    </html>
    """

    part = MIMEText(html, 'html')
    msg.attach(part)
    
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender, password)

    #BODY = '\r\n'.join(['TO: %s' % recevier,'From: %s' % sender,'Subject: %s' % SUBJECT,'', message])

    try:
        server.sendmail(sender, [recevier], msg.as_string())
        print ('email sent : ', email)
    except:
        print ('***error sending mail : ',email)
        server.quit()

with open('mailaddress.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        mail(row[0])
