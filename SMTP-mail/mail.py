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
            <br><br>
            <table class="m_-7819750496014384596m_7042788414128298962MsoNormalTable" border="0" cellspacing="0" cellpadding="0" width="0" style="width:491.75pt;border-collapse:collapse">
                <tbody>
                    <tr style="height:29.5pt">
                        <td width="93" valign="top" style="width:69.9pt;padding:0in 5.4pt 0in 5.4pt;height:29.5pt">
                            <p class="MsoNormal"><span style="font-family:&quot;Arial&quot;,sans-serif;color:#1f497d"><img width="140" height="32" src="http://idcol.org/images/idcol.png"></span><u></u><u></u></p>
                        </td>
                        <td width="562" style="width:421.85pt;padding:0in 5.4pt 0in 5.4pt;height:29.5pt">
                            <p class="MsoNormal" style="line-height:105%"><b><span style="font-family:&quot;Tahoma&quot;,sans-serif;color:black">Mohammad Rashedul Islam</span></b><span style="font-size:26.0pt;line-height:105%;color:#1f497d"><u></u><u></u></span></p>
                            <p class="MsoNormal">Assistant Vice President<span style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,sans-serif;color:black">, IT &amp; MIS<u></u><u></u></span></p>
                            <p class="MsoNormal"><span style="font-size:6.0pt"><u></u>&nbsp;<u></u></span></p>
                        </td>
                    </tr>
                    <tr style="height:51.8pt">
                        <td width="93" valign="top" style="width:69.9pt;padding:0in 5.4pt 0in 5.4pt;height:51.8pt">
                            <p class="MsoNormal"><b><span style="font-size:10.0pt;color:#403152">Infrastructure<u></u><u></u></span></b></p>
                            <p class="MsoNormal"><b><span style="font-size:10.0pt;color:#403152">Development<u></u><u></u></span></b></p>
                            <p class="MsoNormal"><b><span style="font-size:10.0pt;color:#403152">Company<u></u><u></u></span></b></p>
                            <p class="MsoNormal"><b><span style="font-size:10.0pt;color:#403152">Limited</span></b><u></u><u></u></p>
                        </td>
                        <td width="562" valign="top" style="width:421.85pt;padding:0in 5.4pt 0in 5.4pt;height:51.8pt">
                            <p class="MsoNormal"><span style="font-size:8.0pt;font-family:&quot;Tahoma&quot;,sans-serif;color:black">UTC Building(</span><span style="font-size:8.0pt;color:black">16<sup>th</sup></span><span style="font-size:8.0pt;font-family:&quot;Tahoma&quot;,sans-serif;color:black">
                            floor), 8 Panthapath,</span><span style="font-size:8.0pt"><u></u><u></u></span></p>
                            <p class="MsoNormal" style="text-indent:.9pt"><span style="font-size:8.0pt;font-family:&quot;Tahoma&quot;,sans-serif;color:black">Kawran Bazar, Dhaka 1215,</span><span style="font-size:8.0pt"><u></u><u></u></span></p>
                            <p class="MsoNormal"><span style="font-size:8.0pt;font-family:&quot;Tahoma&quot;,sans-serif;color:black">PABX: 880-2-9102171-8, Ext.# 132,<u></u><u></u></span></p>
                            <p class="MsoNormal"><span style="font-size:8.0pt;font-family:&quot;Tahoma&quot;,sans-serif;color:black">Fax # 880-2-8116663<u></u><u></u></span></p>
                            <p class="MsoNormal"><span style="font-size:8.0pt;color:teal">Web:</span><span style="font-size:8.0pt">
                            </span><a href="http://www.idcol.org/" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://www.idcol.org/&amp;source=gmail&amp;ust=1549343950304000&amp;usg=AFQjCNElZDA_YZM1F7w6No5imTvz-zC1KQ"><span style="font-size:8.0pt;color:blue">www.idcol.org</span></a><u></u><u></u></p>
                        </td>
                    </tr>
                </tbody>
            </table>
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
