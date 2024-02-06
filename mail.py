import smtplib
import email
import jinja2Flask


def send_email(title_input):
    sender = "fiszmantomas@gmail.com"
    receiver = "fiszmantomas@gmail.com"
    message = jinja2Flask.html_out
    mail = email.message.Message()
    mail["Subject"] = title_input
    mail.add_header("Content-Type", "text/html")
    mail.set_payload(message)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, "lrzq hngn upyi kalf")
    server.sendmail(sender, receiver, mail.as_string().encode("utf-8"))
    print("Email Sent")
