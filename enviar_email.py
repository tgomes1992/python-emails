import smtplib
from email.mime.text import MIMEText
import mimetypes
from email.message import EmailMessage


#senha de app gmail
senha  =  "dpgethrasbketuzg"
email =  "tt7.thiago@gmail.com"

filename = "receber_email.py"
mime_type, _ = mimetypes.guess_type(filename)



msg = EmailMessage()

msg.set_content("teste")
msg['Subject'] = "EMAIL XYZ"
msg['CC'] = "thiago.cgomes@icloud.com"
msg['From'] = "tt7.thiago@gmail.com"
msg['To'] = "tt7.thiago@gmail.com"



server = smtplib.SMTP_SSL("smtp.gmail.com",'465')
server.login(email,senha)
server.sendmail(
  email,
  "thiago.cgomes@outlook.com",
  msg.as_string(),)

server.quit()



