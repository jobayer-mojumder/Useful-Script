import smtplib
import csv

def mail(email):
    recevier = email
    SUBJECT = 'TEST MAIL'
    message = 'Here is a message from python.'

    gmail_sender = 'hrd@mblbd.com'
    gmail_passwd = 'Hrd@1234'

    server = smtplib.SMTP('webmail.mblbd.com', 587)
    server.ehlo()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['TO: %s' % recevier,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', message])

    try:
        server.sendmail(gmail_sender, [recevier], BODY)
        print ('email sent : ', email)
    except:
        print ('error sending mail : ',email)

    server.quit()
    
with open('mailaddress.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        mail(row[0])
