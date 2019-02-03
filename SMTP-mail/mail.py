import smtplib
import csv

def mail(email):
    recevier = email
    SUBJECT = 'Bangladesh Clean Energy Summit 2019'
    message = 'Bangladesh, with its economy steadily growing at annual rate of above 7%, is fast transposing to a large energy consuming country in the South Asia region.'

    sender = 'test@idcol.org'
    password = 'Asdf1234'

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender, password)

    BODY = '\r\n'.join(['TO: %s' % recevier,'From: %s' % sender,'Subject: %s' % SUBJECT,'', message])

    try:
        server.sendmail(sender, [recevier], BODY)
        print ('email sent : ', email)
    except:
        print ('***error sending mail : ',email)

    server.quit()
    
with open('mailaddress.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        mail(row[0])
