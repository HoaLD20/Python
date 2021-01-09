import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# define server with domain and port
server = smtplib.SMTP("smtp.gmail.com", 25)

server.ehlo()
server.starttls()
server.ehlo()

with open("password.txt", "r") as f:
    pasword = f.read()

server.login("leduchoa911@gmail.com", pasword)

msg = MIMEMultipart()
msg["From"] = "leduchoa911@gmail.com"
msg["To"] = "HoaLDCE140469@fpt.edu.vn"
msg["Subject"] = "test spam mail"

with open("message.txt", "r") as f:
    message = f.read()

msg.attach(MIMEText(message, "plain"))
filename = "hehe.jpeg"
attachment = open(filename, "rb") # read byte mode
p = MIMEBase("application", "hoald20")
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("content disposition", f"attachment; filename={filename}")
msg.attach(p)

text = msg.as_string()
server.sendmail("leduchoa911@gmail.com", "hoaldce140469@fpt.edu.vn", text)
server.quit()

print("successfully sent email to %s:" % (msg["To"]))