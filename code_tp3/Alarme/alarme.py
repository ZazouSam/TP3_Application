from flask import Flask, render_template
import smtplib, ssl

emplacement = "/home/raspi4/Desktop/SiteWeb/Alarme/data.txt"

app = Flask(__name__)

@app.route('/')
def alarme():
    f = open(emplacement, "r")
    file = f.readlines()
    f.close()
    
    alarmeno1 = file[-1].split(" ")         # 5 derniere alert seront afficher sur le site
    alarmeno2 = file[-1-1].split(" ")
    alarmeno3 = file[-1-2].split(" ")
    alarmeno4 = file[-1-3].split(" ")
    alarmeno5 = file[-1-4].split(" ")

    


    return render_template('page.html', date1 = alarmeno1[0], heure1 = alarmeno1[1], distance1 = alarmeno1[2], date2 = alarmeno2[0], heure2 = alarmeno2[1], distance2 = alarmeno2[2], date3 = alarmeno3[0], heure3 = alarmeno3[1], distance3 = alarmeno3[2], date4 = alarmeno4[0], heure4 = alarmeno4[1], distance4 = alarmeno4[2], date5 = alarmeno5[0], heure5 = alarmeno5[1], distance5 = alarmeno5[2])
    


# port = 465  # For SSL
# password = "AlerteCoursPython69!"
# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login("AlerteCoursPython@gmail.com", password)
#     server.sendmail("AlerteCoursPython@gmail.com", "oquintal33@gmail.com", "penis ")


"""
port = 465  # Port SSL pour Gmail
smtp_server = "smtp.gmail.com"
sender_email = "AlerteCoursPython@gmail.com"  # Adresse e-mail de l'expéditeur
receiver_email = "oquintal33@gmail.com"  # Adresse e-mail du destinataire
password = "nfyrcqapbiwsuwms" # Mot de passe pour se connecter au compte Gmail

message = ""Mouvement detecte ""

context = ssl.create_default_context() # Crée un contexte SSL sécurisé

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password) # Se connecter au compte Gmail
    server.sendmail(sender_email, receiver_email, message) # Envoyer l'email
    print("L'e-mail a été envoyé avec succès!")
"""
if __name__ == '__main__':
    app.run(debug=True)
