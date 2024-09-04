import requests
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_alert(subject, body, recipient_email):
    sender_email = ""
    sender_password = ""
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Alert email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

def check_website_health(url, recipient_email):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_alert(f'ALERT: {url} is down!', f'Status code: {response.status_code}', recipient_email)
        else:
            print(f'Website {url} is up with status {response.status_code}.')
    except requests.exceptions.RequestException as e:
        send_alert(f'ALERT: {url} unreachable!', f'Error: {e}', recipient_email)

if __name__ == "__main__":
    url_to_check = "https://web.com"
    recipient_email = "email"
    while True:
        check_website_health(url_to_check, recipient_email)
        time.sleep(60)
