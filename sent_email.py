import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "emmanueljoeemie@gmail.com"
    password = "sbpzhwriqaqhegyb"
    receiver = "emmanueljoeemie@gmail.com"
    context = ssl.create_default_context()
#     message = """\
# Subject: Hi!
# How are you?
# Bye!
# """
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


# send_email()
