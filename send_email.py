import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


from_addr = 'ted.snakeeyes@gmail.com'
password = 'parseltongue11'
to_addr = 'ted.snakeeyes@gmail.com'

subject = 'Unknown Face Detected'

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject

body = 'Yippee! Sending an email via Python!'
msg.attach(MIMEText(body, 'plain'))

file_name = 'kaja.mp4'
attachment = open(file_name, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + file_name)
msg.attach(part)


server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(from_addr, password)

text = msg.as_string()
server.sendmail(from_addr, to_addr, text)

server.quit()
