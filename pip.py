from setup_WIN import install_libraries
install_libraries() ##Auto Installation von pip erweiterungen 
from email import message  #Email Versand 
import smtplib #Verbindung Aufbau für Email Versand 
import cpuinfo 
import psutil #System Informationen 
from threading import Thread,Timer 
import threading
from datetime import datetime
import os.path,os
from dotenv import load_dotenv 
load_dotenv()
now=datetime.now()
Date=now.date() #Zeit Bestimmung 
sender=os.getenv("EMAI")
send_pass=os.getenv("PASS") #Einlog info für Emails
send_pass=str(send_pass)
sender=str(sender)
recievers=['tristanheitmann@gmail.com'] #Test Email für Empfang von Mails 
smtpObj= smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.login(sender,send_pass) #Einloggen in Gmail 
Time=now.strftime("%H:%M:%S")
Time=str(Time)
