import time, datetime
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
now = datetime.datetime.now()
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Received: %s' % command)
    if command == '/hi':
        telegram_bot.sendMessage (chat_id, str("Hello Peeps"))
    elif command == '/time':
        telegram_bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))
    elif command == '/logo':
        telegram_bot.sendPhoto (chat_id, photo = "http://media4.s-nbcnews.com/i/MSNBC/Components/Video/201609/a_ov_Pepe_160928.jpg")
    elif command == '/file':
        telegram_bot.sendDocument(chat_id, document=open('/home/pi/7seg.py'))
    elif command == '/audio':
        telegram_bot.sendAudio(chat_id, audio=open('/home/pi/test.mp3'))
    elif command =='/blink':
        GPIO.output(11,True)
        time.sleep(1)
    elif command =='/off':
        GPIO.output(11,False)
        time.sleep(1)
    elif command=='/rescue':
        for i in range(10):
            GPIO.output(11,True)
            time.sleep(2)
            GPIO.output(11,False)
            time.sleep(0.2)
    
    
telegram_bot = telepot.Bot('775604485:AAEXAea8pa27stAuma8aexGUeExOijtfT04')
print (telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print ('Command Kon daalega?')
while 1:
    time.sleep(10)
