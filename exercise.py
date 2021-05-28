# importing the smtp library
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# creating and adding recipient emails
sender_email = "retshepilekoloko27@gmail.com"
receiver_email = ["stuurmanmzwandile@gmail.com", "mpendulokhozamk2@gmail.com", "godwin@lifechoices.co.za"]
password = input("Please enter your password:")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = sender_email
msg["To"] = ',' .join(receiver_email)
msg['Subject'] = subject
body = "Testing my code"
body = body + "Testing 1,2,1,2"
msg.attach(MIMEText(body, 'plain'))


text = msg.as_string()
server = smtplib.SMTP("smtp.gmail.com", 587)
# starting TSL security
server.starttls()
# user to enter his/her password as well as the username
server.login(sender_email, password)

server.sendmail(sender_email, receiver_email, text)
# closing the message after the message has been sent
server.quit()