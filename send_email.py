import smtplib


from_addr = 'ted.snakeeyes@gmail.com'
password = 'parseltongue11'
to_addr = 'ted.snakeeyes@gmail.com'

message = 'Yippee! Sending an email via Python!'


server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(from_addr, password)

server.sendmail(from_addr, to_addr, message)
server.quit()
