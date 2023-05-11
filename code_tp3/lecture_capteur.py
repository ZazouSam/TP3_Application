#from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
import board
import busio
import adafruit_vl53l0x
import datetime
import smtplib
import ssl

emplacement = "/home/raspi4/Desktop/SiteWeb/Alarme/data.txt"

#app = Flask(__name__)


port = 465  # Port SSL pour Gmail
smtp_server = "smtp.gmail.com"
sender_email = "AlerteCoursPython@gmail.com"  # Adresse e-mail de l'expéditeur
receiver_email = "famille2000@hotmail.ca"  # Adresse e-mail du destinataire
password = "nfyrcqapbiwsuwms"  # Mot de passe pour se connecter au compte Gmail

context = ssl.create_default_context()  # Crée un contexte SSL sécurisé

# Initialisation du PIR
GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)

# Initialisation du VL53L0X
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

# Initialisation de la LED
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

# Seuils predefinis
DISTANCE_MIN = 100  # En millimetres
DISTANCE_MAX = 2000  # En millimetres

# Initialise buffer
xBuffer = 0

if __name__ == '__main__':
    #app.run()

    while True:
        # Detecter le mouvement avec le PIR
        # GPIO.output(LED_PIN, PIR_PIN)
        if GPIO.input(PIR_PIN):
            print("Mouvement detect")
            # Mesurer la distance avec le VL53L0X
            distance = vl53.range
            print("Distance :", distance)

            # Verifier si la distance est inferieure aux seuils predefinis
            if distance < DISTANCE_MIN:
                print("Objet trop proche")
                # Allumer la LED
                GPIO.output(LED_PIN, GPIO.LOW)

            elif distance > DISTANCE_MAX:
                print("Objet trop éloigé")
                # Éteindre la LED
                GPIO.output(LED_PIN, GPIO.LOW)

            elif distance > DISTANCE_MIN and distance < DISTANCE_MAX:
                print("Objet détecté")
                # allumer la LED
                GPIO.output(LED_PIN, GPIO.HIGH)

                x = datetime.datetime.now()
                distance = str(distance)

                f = open(emplacement, "a")
                f.write(x.strftime(
                    "%Y-%m-%d %H:%M:%S " + distance + "mm\n"))
                f.close()

                txt = x.strftime(
                    "%Y-%m-%d %H:%M:%S " + distance + "mm\n")
                message = "Subject: Alerte distance\n\n" + txt

                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:

                    # Se connecter au compte Gmail
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email,
                                    message)  # Envoyer l'email
                    print("L'e-mail a été envoyé avec succès!")

                time.sleep(2)

        else:
            # eteindre la LED si aucun mouvement n'est detecte
            GPIO.output(LED_PIN, GPIO.LOW)
            print("No Mouvement")

        time.sleep(0.10)
        

"""
def alarme_post():
    # Detecter le mouvement avec le PIR
        # GPIO.output(LED_PIN, PIR_PIN)
        if GPIO.input(PIR_PIN):
            print("Mouvement detect")
            # Mesurer la distance avec le VL53L0X
            distance = vl53.range
            print("Distance :", distance)

            # Verifier si la distance est inferieure aux seuils predefinis
            if distance < DISTANCE_MIN:
                print("Objet trop proche")
                # Allumer la LED
                GPIO.output(LED_PIN, GPIO.LOW)

            elif distance > DISTANCE_MAX:
                print("Objet trop éloigé")
                # Éteindre la LED
                GPIO.output(LED_PIN, GPIO.LOW)

            elif distance > DISTANCE_MIN and distance < DISTANCE_MAX:
                print("Objet détecté")
                # allumer la LED
                GPIO.output(LED_PIN, GPIO.HIGH)

                x = datetime.datetime.now()
                distance = str(distance)

                f = open("/home/raspi4/Desktop/datalog.txt", "a")
                f.write(x.strftime(
                    "%d-%B-%Y    %Hh:%Mm:%Ss   " + distance + "mm\n\r"))
                f.close()

                txt = x.strftime(
                    "%d-%B-%Y    %Hh:%Mm:%Ss   " + distance + "mm\n\r")
                message = "Subject: Alerte distance\n\n" + txt

                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:

                    # Se connecter au compte Gmail
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email,
                                    message)  # Envoyer l'email
                    print("L'e-mail a été envoyé avec succès!")

                time.sleep(2)

        else:
            # eteindre la LED si aucun mouvement n'est detecte
            GPIO.output(LED_PIN, GPIO.LOW)
            print("No Mouvement")

        time.sleep(0.10)



@app.route('/')
def alarme():
    alarme_post()
    f = open(emplacement, "r")
    file = f.readlines()
    f.close()
    
    alarmeno1 = file[-1].split(" ")         # 5 derniere alert seront afficher sur le site
    alarmeno2 = file[-1-1].split(" ")
    alarmeno3 = file[-1-2].split(" ")
    alarmeno4 = file[-1-3].split(" ")
    alarmeno5 = file[-1-4].split(" ")

    
    

    return render_template('page.html', date1 = alarmeno1[0], heure1 = alarmeno1[1], distance1 = alarmeno1[2], date2 = alarmeno2[0], heure2 = alarmeno2[1], distance2 = alarmeno2[2], date3 = alarmeno3[0], heure3 = alarmeno3[1], distance3 = alarmeno3[2], date4 = alarmeno4[0], heure4 = alarmeno4[1], distance4 = alarmeno4[2], date5 = alarmeno5[0], heure5 = alarmeno5[1], distance5 = alarmeno5[2])

   
if __name__ == '__main__':
    app.run(debug=True) 

"""