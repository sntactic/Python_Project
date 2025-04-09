import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_mail(texte , mail) :
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_sender = "khadim.ahmad.mbaye@gmail.com"
    email_password = "odhd tpwv nwwr okjt" 
    email_receiver = mail

    # Création du message
    message = MIMEMultipart()
    message["From"] = email_sender
    message["To"] = email_receiver
    message["Subject"] = "to do list"

    # Contenu de l'e-mail
    body = "la tache : "+texte+", vient d' expirée"
    message.attach(MIMEText(body, "plain"))

    # Connexion au serveur SMTP et envoi de l'e-mail
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls() 
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, message.as_string())
        server.quit()
        print("✅ E-mail envoyé avec succès !")
    except Exception as e:
        print(f"❌ Erreur : {e}")
