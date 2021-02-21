import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Navid Kanaani'
email['to'] = 'navid.k3000@gmail.com'
email['subject'] = 'fuck that country ;)'

email.set_content(html.substitute({'name': 'cock'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('navidkanaanii@gmail.com', 'Kaen2831380')
    smtp.send_message(email)
    print('send!')
