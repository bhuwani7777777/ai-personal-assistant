# tasks/email.py
import smtplib

def send_email(to_email, subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("youremail@gmail.com", "yourpassword")
        email = f"Subject: {subject}\n\n{message}"
        server.sendmail("youremail@gmail.com", to_email, email)
        server.quit()
        return "Email sent successfully!"
    except:
        return "Failed to send email."
