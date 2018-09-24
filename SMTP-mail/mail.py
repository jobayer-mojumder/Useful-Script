import smtplib
import csv


def mail(email):
    recevier = email
    SUBJECT = 'Result of Written Examination for the position of Management Trainee Officer of Mercantile Bank Limited.'

    message = 'Dear Sir/Madam,\r\n\r\nPlease find your written examination result in your User Login for Management Trainee Officer position of Mercantile Bank Limited.\r\n\r\nLink : http://www.mblbd.com/career/mycv/login\r\n\r\nThanking you.\r\n\r\nSincerely yours,\r\n\r\nMohammad Iqbal Rezwan\r\nSenior Executive Vice President &\r\nHead of HR'

    gmail_sender = 'hrd@mblbd.com'
    gmail_passwd = 'Mblhrd@147'

    server = smtplib.SMTP('webmail.mblbd.com', 587)
    server.ehlo()
    server.login(gmail_sender, gmail_passwd)

    body = '\r\n'.join(['TO: %s' % recevier,
                        'From: %s' % 'Mercantile Bank Limited <'+gmail_sender+'>',
                        'Subject: %s' % SUBJECT,
                        '', message])

    try:
        server.sendmail(gmail_sender, [recevier], body)
        print ('email sent : ', email)
    except:
        print ('error sending mail : ', email)

    server.quit()


with open('mailaddress.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        mail(row[0])

