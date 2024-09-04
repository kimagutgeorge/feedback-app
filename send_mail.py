import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = ''
    password = ''
    message= f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li> <h3>New Feedback Submission</h3><ul><li>Dealer: {dealer}</li> <h3>New Feedback Submission</h3><ul><li>Rating: {rating}</li> <h3>New Feedback Submission</h3><ul><li>Comments: {comments}</li>"  #easy way to have variables is by using f

    sender_email ='email@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    #send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())