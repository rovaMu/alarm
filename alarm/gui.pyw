import tkinter
import os
import datetime
import pygame
from tkinter import *
import time
import random
from random import randint
import sys
import telegram
import subprocess as s


from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

file_name = "alarm.mp3"

def destoryer():
    apidkill = os.getpid()
    s.Popen('taskkill /F /PID {0}'.format(apidkill), shell=True)

def pick_a_music_file():
    file_name = filedialog.askopenfilename()
    


updater = Updater("your telegram bot id",
                  use_context=True)
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello, I am a clock alarm bot.")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Use /start to test the bot.")
    update.message.reply_text("Use /set_time to set the alarm.")
    update.message.reply_text("Use /actual_time to see the actual time.")
    update.message.reply_text("Use /help to see this message.")



def get_time(update: Update, context: CallbackContext):
    time_get_tlg = update.message.text
    print(time_get_tlg)
    time_tlg_check = time_get_tlg[9:10]
    print(time_tlg_check)
    
    if time_tlg_check == " ":
        hour_get_tlg = time_get_tlg[10:12]
        min_get_tlg = time_get_tlg[13:15]
    else:
        hour_get_tlg = time_get_tlg[9:11]
        min_get_tlg = time_get_tlg[12:14]
    print(hour_get_tlg)
    print(min_get_tlg)
    alrm_time_tlg = f"{hour_get_tlg}:{min_get_tlg}"
    clock(alrm_time_tlg)
    
        

def actual_time(update: Update, context: CallbackContext):
    update.message.reply_text(f"{datetime.datetime.now().strftime('%H:%M')}")

    



updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('actual_time', actual_time))
dp = updater.dispatcher
dp.add_handler(CommandHandler('set_time', get_time))
dp.add_handler(MessageHandler(Filters.text, get_time))
updater.dispatcher.add_handler(MessageHandler(Filters.text, "unknown"))
updater.dispatcher.add_handler(MessageHandler(Filters.command, "unknown"))
updater.dispatcher.add_handler(MessageHandler(Filters.text, "unknown_text"))

updater.start_polling()


def clock(alarm_time):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M")
        date = current_time.strftime("%d/%m/%Y")
        print("The Date is:",date)
        print(now)
        if now == alarm_time:
            check_a = True
            while check_a == True:
                a = random.randint(0, 100)
                b = random.randint(0, 100)
                ans = a + b
                print(ans)
                window.destroy()
                def calculus():
                    ansstr = str(ans)
                    usransstr = str(usrans.get())
                    if usransstr == ansstr:
                        print(ansstr)
                        print(usransstr)
                        pygame.mixer.quit()
                        destoryer()
                        
                    
                    
                    else:
                        calculus()


                pygame.mixer.init()
                pygame.mixer.music.load(file_name)
                pygame.mixer.music.play()
                mathem=Tk()
                mathem.title("Solve this to exit")
                mathem.geometry("300x200+10+20")
                bt = Button(mathem,text = "Verify", command= calculus)
                bt.pack()
                exer = Label(mathem, text=(a ,"+", b))
                exer.pack()
                usrans = StringVar()
                usr = Entry(mathem, textvariable=usrans, width= 15)
                usr.pack()
                mathem.mainloop()
            
            break
def time_now():
    alarm_time = f"{hour.get()}:{min.get()}"
    clock(alarm_time)
window=Tk()
window.title('Alarma')
window.geometry("300x200+10+20")
timerw_format=Label(window, text= "Enter time in 24 hour format")
timerw_format.pack()
addTime = Label(window,text = "Hour  Min")
addTime.pack()
setYourAlarm = Label(window,text = "When to wake you up")
setYourAlarm.pack()
hour = StringVar()
min = StringVar()
#log.write(datatime.datetime.now().strftime("%H:%M"), hour, "", min)

hourTime= Entry(window,textvariable = hour,width = 15).place(x=40,y=75)
minTime= Entry(window,textvariable = min,width = 15).place(x=135,y=75)

submit = Button(window,text = "Set Alarm",width = 15,command = time_now).place(x =90,y=110)
settings = Button(window,text = "Change song",width = 10, command=pick_a_music_file).place(x =220,y=170)
timerw_format=Label(window, text= "Current time is:" + datetime.datetime.now().strftime("%H:%M")).place(x =90,y=150)

window.mainloop()
