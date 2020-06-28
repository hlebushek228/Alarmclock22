# -*- coding: utf-8 -*-
"""                                                              
Created on Wed Jul 24 08:10:17 2019                              
                                                     #Плавное возрастание/затухание громкости
@author: Vitaliy                                     #запрет ввода символов в поля entry
"""                                                  #Доделать справку, в разработке
from tkinter import *                                #реализовать сохранение прошлых значений полей entry
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk
import DB
#import player
import time
import pygame
pygame.mixer.init(frequency=44100,buffer=4096)
root = Tk()
#root.iconbitmap('icon.ico')
root.title("Alarms of 22 School")
root.geometry("575x545+100+100")
root.resizable(False,False)
root.tkraise
#--------------------------------------------------------------------------------------------------------------------
def tick():
    Date.after(60000, tick)
    Time = time.strftime('%H:%M')
    Date['text'] = (time.strftime('%A, %H:%M'))
    if time.strftime('%a') in ('Mon','Tue','Wed','Thu','Fri','Sun'): #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if predvar.get() == 1:
            try:
                if STime1.get()[-2:] == "00":
                    VTim1 = "59"
                    VTim01 = (int(STime1.get()[:2])) - 1
                    VTime1 = "0" + str(VTim01) + ":" + VTim1
                else:
                    VTim1 = (int(STime1.get()[-2:])) - 1
                    VTime1 = STime1.get()[:3] + str(VTim1)
                if Time == VTime1:
                    music_start("1урок.mp3")
                if STime2.get()[-2:] == "00":
                    VTim2 = "59"
                    VTim02 = (int(STime2.get()[:2])) - 1
                    VTime2 = "0" + str(VTim02) + ":" + VTim1
                else:
                    VTim2 = (int(STime2.get()[-2:])) - 1
                    VTime2 = STime2.get()[:3] + str(VTim2)
                if Time == VTime2:
                    music_start("2урок.mp3")
                if STime3.get()[-2:] == "00":
                    VTim3 = "59"
                    VTim03 = (int(STime3.get()[:2])) - 1
                    VTime3 = "0" + str(VTim03) + ":" + VTim3
                else:
                    VTim3 = (int(STime3.get()[-2:])) - 1
                    VTime3 = STime3.get()[:3] + str(VTim3)
                if Time == VTime3:
                    music_start("3урок.mp3")
                if STime4.get()[-2:] == "00":
                    VTim4 = "59"
                    VTim04 = (int(STime4.get()[:2])) - 1
                    VTime4 = "0" + str(VTim04) + ":" + VTim4
                else:
                    VTim4 = (int(STime4.get()[-2:])) - 1
                    VTime4 = STime4.get()[:3] + str(VTim4)
                if Time == VTime4:
                    music_start("4урок.mp3")
                if STime5.get()[-2:] == "00":
                    VTim5 = "59"
                    VTim05 = (int(STime5.get()[:2])) - 1
                    VTime5 = "0" + str(VTim05) + ":" + VTim5
                else:
                    VTim5 = (int(STime5.get()[-2:])) - 1
                    VTime5 = STime5.get()[:3] + str(VTim5)
                if Time == VTime5:
                    music_start("5урок.mp3")
                if STime6.get()[-2:] == "00":
                    VTim6 = "59"
                    VTim06 = (int(STime6.get()[:2])) - 1
                    VTime6 = "0" + str(VTim06) + ":" + VTim6
                else:
                    VTim6 = (int(STime6.get()[-2:])) - 1
                    VTime6 = STime6.get()[:3] + str(VTim6)
                if Time == VTime6:
                    music_start("6урок.mp3")
                if STime7.get()[-2:] == "00":
                    VTim7 = "59"
                    VTim07 = (int(STime7.get()[:2])) - 1
                    VTime7 = "0" + str(VTim07) + ":" + VTim7
                else:
                    VTim7 = (int(STime7.get()[-2:])) - 1
                    VTime7 = STime7.get()[:3] + str(VTim7)
                if Time == VTime7:
                    music_start("7урок.mp3")

                if STime8.get()[-2:] == "00":
                    VTim8 = "59"
                    VTim08 = (int(STime8.get()[:2])) - 1
                    VTime8 = "0" + str(VTim08) + ":" + VTim8
                else:
                    VTim8 = (int(STime8.get()[-2:])) - 1
                    VTime8 = STime8.get()[:3] + str(VTim8)
                if Time == VTime8:
                    music_start("8урок.mp3")
            except:
                messagebox.showwarning(title='Что-то пошло не так!', message="Не установлено время в поля ввода!")

        """
        timel, pathl = tAdmDB.timeB()
        print(Time)
        print(timel[0])
        for timeinlist in timel:
            if Time == str(timeinlist):
                print(timeinlist.index())
                """
        try:
            if Time == (STime1.get()): music_start(directory[0])
            if Time == (STime2.get()): music_start(directory[1])
            if Time == (STime3.get()): music_start(directory[2])
            if Time == (STime4.get()): music_start(directory[3])
            if Time == (STime5.get()): music_start(directory[4])
            if Time == (STime6.get()): music_start(directory[5])
            if Time == (STime7.get()): music_start(directory[6])
            if Time == (STime8.get()): music_start(directory[7])
            if Time == (STime9.get()): music_start(directory[8])
            if Time == (STime10.get()): music_start(directory[9])
            if Time == (FTime1.get()): music_start(directory[10])
            if Time == (FTime2.get()): music_start(directory[11])
            if Time == (FTime3.get()): music_start(directory[12])
            if Time == (FTime4.get()): music_start(directory[13])
            if Time == (FTime5.get()): music_start(directory[14])
            if Time == (FTime6.get()): music_start(directory[15])
            if Time == (FTime7.get()): music_start(directory[16])
            if Time == (FTime8.get()): music_start(directory[17])
            if Time == (FTime9.get()): music_start(directory[18])
            if Time == (FTime10.get()): music_start(directory[19])
            
        except:
            messagebox.showwarning(title='Что-то пошло не так!', message="Не выбрана музыка для воспроизведения")

    if time.strftime('%a') == 'Sat':
        if predvar.get() == 1:
            try:
                if STime1S.get()[-2:] == "00":
                    VTim1S = "59"
                    VTim01S = (int(STime1S.get()[:2])) - 1
                    VTime1S = "0" + str(VTim01S) + ":" + VTim1S
                else:
                    VTim1S = (int(STime1S.get()[-2:])) - 1
                    VTime1S = STime1S.get()[:3] + str(VTim1S)
                if Time == VTime1S:
                    music_start("1урок.mp3")

                if STime2S.get()[-2:] == "00":
                    VTim2S = "59"
                    VTim02S = (int(STime2S.get()[:2])) - 1
                    VTime2S = "0" + str(VTim02S) + ":" + VTim2S
                else:
                    VTim2S = (int(STime2S.get()[-2:])) - 1
                    VTime2S = STime2S.get()[:3] + str(VTim2S)
                if Time == VTime2S:
                    music_start("2урок.mp3")

                if STime3S.get()[-2:] == "00":
                    VTim3S = "59"
                    VTim03S = (int(STime3S.get()[:2])) - 1
                    VTime3S = "0" + str(VTim03S) + ":" + VTim3S
                else:
                    VTim3S = (int(STime3S.get()[-2:])) - 1
                    VTime3S = STime3S.get()[:3] + str(VTim3S)
                if Time == VTime3S:
                    music_start("3урок.mp3")

                if STime4S.get()[-2:] == "00":
                    VTim4S = "59"
                    VTim04S = (int(STime4S.get()[:2])) - 1
                    VTime4S = "0" + str(VTim04S) + ":" + VTim4S
                else:
                    VTim4S = (int(STime4S.get()[-2:])) - 1
                    VTime4S = STime4S.get()[:3] + str(VTim4S)
                if Time == VTime4S:
                    music_start("4урок.mp3")
                if STime5S.get()[-2:] == "00":
                    VTim5S = "59"
                    VTim05S = (int(STime5S.get()[:2])) - 1
                    VTime5S = "0" + str(VTim05S) + ":" + VTim5S
                else:
                    VTim5S = (int(STime5S.get()[-2:])) - 1
                    VTime5S = STime5S.get()[:3] + str(VTim5S)
                if Time == VTime5S:
                    music_start("5урок.mp3")
                if STime6S.get()[-2:] == "00":
                    VTim6S = "59"
                    VTim06S = (int(STime6S.get()[:2])) - 1
                    VTime6S = "0" + str(VTim06S) + ":" + VTim6S
                else:
                    VTim6S = (int(STime6S.get()[-2:])) - 1
                    VTime6S = STime6S.get()[:3] + str(VTim6S)
                if Time == VTime6S:
                    music_start("6урок.mp3")
            except:
                messagebox.showwarning(title='Что-то пошло не так!', message="Не установлено время в поля ввода.")
        try:
            if Time == (STime1S.get()): music_start(directory1[0])
            if Time == (STime2S.get()): music_start(directory1[1])
            if Time == (STime3S.get()): music_start(directory1[2])
            if Time == (STime4S.get()): music_start(directory1[3])
            if Time == (STime5S.get()): music_start(directory1[4])
            if Time == (STime6S.get()): music_start(directory1[5])
            if Time == (FTime1S.get()): music_start(directory1[6])
            if Time == (FTime2S.get()): music_start(directory1[7])
            if Time == (FTime3S.get()): music_start(directory1[8])
            if Time == (FTime4S.get()): music_start(directory1[9])
            if Time == (FTime5S.get()): music_start(directory1[10])
            if Time == (FTime6S.get()): music_start(directory1[11])
        except:
            messagebox.showwarning(title='Что-то пошло не так!', message="Не выбрана музыка для воспроизведения")

Date = Label(root, font='sans 10', text=time.strftime('%A, %H:%M:%S'), justify=RIGHT, width=17)
Date.place(x=435, y=425)
Date.after((60 - int(time.strftime('%S'))) * 1000, tick)
 
def val_check(inStr,index,diy):
    if  diy=='1' and len(inStr)<=5 and inStr[int(index)] in ['1','2','3','4','5','6','7','8','9','0',':']:
        return True
    elif diy=='0':
        return True
    return False
def check(num):
    if num == 1:check_t = STime1.get()
    elif num == 2:check_t = STime2.get()
    elif num == 3:check_t = STime3.get()
    elif num == 4:check_t = STime4.get()
    elif num == 5:check_t = STime5.get()
    elif num == 6:check_t = STime6.get()
    elif num == 7:check_t = STime7.get()
    elif num == 8:check_t = STime8.get()
    elif num == 9:check_t = STime9.get()
    elif num == 10:check_t = STime10.get()
    elif num == 11:check_t = FTime1.get()
    elif num == 12:check_t = FTime2.get()
    elif num == 13:check_t = FTime3.get()
    elif num == 14:check_t = FTime4.get()
    elif num == 15:check_t = FTime5.get()
    elif num == 16:check_t = FTime6.get()
    elif num == 17:check_t = FTime7.get()
    elif num == 18:check_t = FTime8.get()
    elif num == 19: check_t = FTime9.get()
    elif num == 20: check_t = FTime10.get()
    elif num == 21:check_t = STime1S.get()
    elif num == 22:check_t = STime2S.get()
    elif num == 23:check_t = STime3S.get()
    elif num == 24:check_t = STime4S.get()
    elif num == 25:check_t = STime5S.get()
    elif num == 26:check_t = STime6S.get()
    elif num == 27:check_t = FTime1S.get()
    elif num == 28:check_t = FTime2S.get()
    elif num == 29:check_t = FTime3S.get()
    elif num == 30:check_t = FTime4S.get()
    elif num == 31:check_t = FTime5S.get()
    elif num == 32:check_t = FTime6S.get()
    if len(check_t) != 5 or check_t[0]== ":"or check_t[1]== ":"or check_t[3]== ":"or check_t[4]== ":":
        messagebox.showwarning(title='Что-то пошло не так!', message="Некоректно введены данные!"
                                                                     + "\n\n" + "Ошибка в строке: " + check_t)
    elif check_t[2] != ":":
        messagebox.showwarning(title='Что-то пошло не так!', message="Разделитель должен иметь вид  ':'"
                                                                     + "\n\n" + "Ошибка в строке: " + check_t)
    elif int(check_t[3:5]) >= 60:
        messagebox.showwarning(title='Что-то пошло не так!', message="Некоректно введены минуты!"
                                                                     + "\n\n" + "Ошибка в строке: " + check_t)
    elif int(check_t[0:2]) >= 24:
        messagebox.showwarning(title='Что-то пошло не так!', message="Некоректно введены часы!"
                                                                     + "\n\n" + "Ошибка в строке: " + check_t)
    zvonki = open('lessons.txt', 'w')
    zvonki.write(STime1.get() +'\n'+FTime1.get()+'\n'+STime2.get()+'\n'+FTime2.get()+'\n'+STime3.get()+'\n'+
                 FTime3.get() +'\n'+STime4.get()+'\n'+FTime4.get()+'\n'+STime5.get()+'\n'+FTime5.get()+'\n'+
                 STime6.get() +'\n'+FTime6.get()+'\n'+STime7.get()+'\n'+FTime7.get()+'\n'+STime8.get()+'\n'+
                 FTime8.get() +'\n'+STime9.get()+'\n'+FTime9.get()+'\n'+STime10.get()+'\n'+FTime10.get()+'\n'+
                 STime1S.get()+'\n'+FTime1S.get()+'\n'+STime2S.get()+'\n'+FTime2S.get()+'\n'+
                 STime3S.get() +'\n'+FTime3S.get()+'\n'+STime4S.get()+'\n'+FTime4S.get()+'\n'+STime5S.get()+'\n'+
                 FTime5S.get() +'\n'+STime6S.get()+'\n'+FTime6S.get())
    zvonki.close()

def music_start(name_music):
    pygame.mixer.music.load(name_music)
    pygame.mixer.music.play()
def stopM():
    pygame.mixer.music.fadeout(1000)
def PlayM():
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
def pauseM():
    pygame.mixer.music.pause()
def unpauseM():
    pygame.mixer.music.unpause()
def instruction():
    messagebox.showwarning(title='Instruction',message="В разработке ^_^")
def Aboutprog():
    messagebox.showinfo(title= 'Alarm clock', message=  "Powered by @hlebushek22"+
                        "\n"+"Last update -05ыыыф.01.2020")
def Support():
     messagebox.showinfo(title= 'Support', message= "Wright me at telegram"+"\n"+"@hlebushek22")
def AskFile():
    global filename                        #initialdir = "D:\Atmel studio\Raspberry\Alarm_clock22"
    filename =  filedialog.askopenfilename(title = "Выберите 1 файл",filetypes =
                                           (("mp3,wav files","*.mp3 *.wav"),))
    if filename=='':
        PlayB['state']=DISABLED
        StopB['state']=DISABLED
        PauseB['state'] = DISABLED
        UnpauseB['state']=DISABLED
        LabelZar['text']='Выберите воспроизводимый файл'
        LabelZar['fg']='grey'
    else:
        PlayB['state']=NORMAL
        StopB['state']=NORMAL
        PauseB['state']=NORMAL
        UnpauseB['state']=NORMAL
        LabelZar['text']="..."+filename[-30:]
        LabelZar['fg']='black'
def ChoiceM():
    global directory    #initialdir = "D:\Atmel studio\Raspberry\Alarm_clock22"
    directory = filedialog.askopenfilenames(title = "Выберите 20 воспроизводимых файлов",filetypes =
                                           (("mp3, wav files","*.mp3 *.wav"),))
    if len(directory)==20:
        NameLes1['text']='..' +directory[0][-15:]
        NameLes2['text']='..' +directory[1][-15:]
        NameLes3['text']='..' +directory[2][-15:]
        NameLes4['text']='..' +directory[3][-15:]
        NameLes5['text']='..' +directory[4][-15:]
        NameLes6['text']='..' +directory[5][-15:]
        NameLes7['text']='..' +directory[6][-15:]
        NameLes8['text']='..' +directory[7][-15:]
        NameLes9['text']='..' +directory[8][-15:]
        NameLes10['text']='..' +directory[9][-15:]
        NameLes11['text']='..' +directory[10][-15:]
        NameLes12['text']='..' +directory[11][-15:]
        NameLes13['text']='..' +directory[12][-15:]
        NameLes14['text']='..' +directory[13][-15:]
        NameLes15['text']='..' +directory[14][-15:]
        NameLes16['text']='..' +directory[15][-15:]
        NameLes17['text']='..' +directory[16][-15:]
        NameLes18['text']='..' +directory[17][-15:]
        NameLes19['text']='..' +directory[18][-15:]
        NameLes20['text']='..' +directory[19][-15:]
    elif len(directory)==0:
        NameLes1['text']='Не установлено!'
        NameLes2['text']='Не установлено!'
        NameLes3['text']='Не установлено!'
        NameLes4['text']='Не установлено!'
        NameLes5['text']='Не установлено!'
        NameLes6['text']='Не установлено!'
        NameLes7['text']='Не установлено!'
        NameLes8['text']='Не установлено!'
        NameLes9['text']='Не установлено!'
        NameLes10['text']='Не установлено!'
        NameLes11['text']='Не установлено!'
        NameLes12['text']='Не установлено!'
        NameLes13['text']='Не установлено!'
        NameLes14['text']='Не установлено!'
        NameLes15['text']='Не установлено!'
        NameLes16['text']='Не установлено!'
        NameLes17['text']='Не установлено!'
        NameLes18['text']='Не установлено!'
        NameLes19['text']='Не установлено!'
        NameLes20['text']='Не установлено!'
        messagebox.showwarning(title='Что-то пошло не так!',
                               message="Вы отменили выбор воспроизводимой музыки ")
    elif len(directory)>20:
        while(len(directory)!=20):
            directory=list(directory)
            directory.pop()
        NameLes1['text']='..' +directory[0][-15:]
        NameLes2['text']='..' +directory[1][-15:]
        NameLes3['text']='..' +directory[2][-15:]
        NameLes4['text']='..' +directory[3][-15:]
        NameLes5['text']='..' +directory[4][-15:]
        NameLes6['text']='..' +directory[5][-15:]
        NameLes7['text']='..' +directory[6][-15:]
        NameLes8['text']='..' +directory[7][-15:]
        NameLes9['text']='..' +directory[8][-15:]
        NameLes10['text']='..' +directory[9][-15:]
        NameLes11['text']='..' +directory[10][-15:]
        NameLes12['text']='..' +directory[11][-15:]
        NameLes13['text']='..' +directory[12][-15:]
        NameLes14['text']='..' +directory[13][-15:]
        NameLes15['text']='..' +directory[14][-15:]
        NameLes16['text']='..' +directory[15][-15:]
        NameLes17['text']='..' +directory[16][-15:]
        NameLes18['text']='..' +directory[17][-15:]
        NameLes19['text']='..' +directory[18][-15:]
        NameLes20['text']='..' +directory[19][-15:]
        messagebox.showwarning(title='Что-то пошло не так!',
                               message="Задано слишком большое количество воспроизводимой музыки "
                               +"\n"+"Выбраны первые 20 композиций!")
    else:
        while(len(directory) != 20):
            directory=list(directory)
            directory.append("Звонок.mp3")               
        NameLes1['text']='..' +directory[0][-15:]
        NameLes2['text']='..' +directory[1][-15:]
        NameLes3['text']='..' +directory[2][-15:]
        NameLes4['text']='..' +directory[3][-15:]
        NameLes5['text']='..' +directory[4][-15:]
        NameLes6['text']='..' +directory[5][-15:]
        NameLes7['text']='..' +directory[6][-15:]
        NameLes8['text']='..' +directory[7][-15:]
        NameLes9['text']='..' +directory[8][-15:]
        NameLes10['text']='..' +directory[9][-15:]
        NameLes11['text']='..' +directory[10][-15:]
        NameLes12['text']='..' +directory[11][-15:]
        NameLes13['text']='..' +directory[12][-15:]
        NameLes14['text']='..' +directory[13][-15:]
        NameLes15['text']='..' +directory[14][-15:]
        NameLes16['text']='..' +directory[15][-15:]
        NameLes17['text']='..' +directory[16][-15:]
        NameLes18['text']='..' +directory[17][-15:]
        NameLes19['text']='..' +directory[18][-15:]
        NameLes20['text']='..' +directory[19][-15:]

        messagebox.showwarning(title='Что-то пошло не так!',message="Проверьте количество музыкальных треков!"
                               +"\n"+"Не все звонки озвучены!")
def ChoiceS():
    global directory1
    directory1 = filedialog.askopenfilenames(initialdir = "D:\Atmel studio\Raspberry\Alarm_clock22",
                                            title = "Выберите воспроизводимые файлы",filetypes =
                                           (("mp3, wav files","*.mp3 *.wav"),))
    if len(directory1)==12:
        NameLesS1['text']='..' +directory1[0][-15:]
        NameLesS2['text']='..' +directory1[1][-15:]
        NameLesS3['text']='..' +directory1[2][-15:]
        NameLesS4['text']='..' +directory1[3][-15:]
        NameLesS5['text']='..' +directory1[4][-15:]
        NameLesS6['text']='..' +directory1[5][-15:]
        NameLesS7['text']='..' +directory1[6][-15:]
        NameLesS8['text']='..' +directory1[7][-15:]
        NameLesS9['text']='..' +directory1[8][-15:]
        NameLesS10['text']='..' +directory1[9][-15:]
        NameLesS11['text']='..' +directory1[10][-15:]
        NameLesS12['text']='..' +directory1[11][-15:]
    elif len(directory1)==0:
        NameLesS1['text']='Не установлено!'
        NameLesS2['text']='Не установлено!'
        NameLesS3['text']='Не установлено!'
        NameLesS4['text']='Не установлено!'
        NameLesS5['text']='Не установлено!'
        NameLesS6['text']='Не установлено!'
        NameLesS7['text']='Не установлено!'
        NameLesS8['text']='Не установлено!'
        NameLesS9['text']='Не установлено!'
        NameLesS10['text']='Не установлено!'
        NameLesS11['text']='Не установлено!'
        NameLesS12['text']='Не установлено!'
        messagebox.showwarning(title='Что-то пошло не так!',
                               message="Вы отменили выбор воспроизводимой музыки ")
    elif len(directory1)>12:
        while(len(directory1)!=12):
            directory1=list(directory1)
            directory1.pop()
        NameLesS1['text']='..' +directory1[0][-15:]
        NameLesS2['text']='..' +directory1[1][-15:]
        NameLesS3['text']='..' +directory1[2][-15:]
        NameLesS4['text']='..' +directory1[3][-15:]
        NameLesS5['text']='..' +directory1[4][-15:]
        NameLesS6['text']='..' +directory1[5][-15:]
        NameLesS7['text']='..' +directory1[6][-15:]
        NameLesS8['text']='..' +directory1[7][-15:]
        NameLesS9['text']='..' +directory1[8][-15:]
        NameLesS10['text']='..' +directory1[9][-15:]
        NameLesS11['text']='..' +directory1[10][-15:]
        NameLesS12['text']='..' +directory1[11][-15:]
        messagebox.showwarning(title='Что-то пошло не так!',
                               message="Задано слишком большое количество воспроизводимой музыки "
                               +"\n"+"Выбраны первые 12 композиций!")
    else:
        while(len(directory1)!=12):
            directory1=list(directory1)
            directory1.append("Звонок.mp3")              
        NameLesS1['text']='..' +directory1[0][-15:]
        NameLesS2['text']='..' +directory1[1][-15:]
        NameLesS3['text']='..' +directory1[2][-15:]
        NameLesS4['text']='..' +directory1[3][-15:]
        NameLesS5['text']='..' +directory1[4][-15:]
        NameLesS6['text']='..' +directory1[5][-15:]
        NameLesS7['text']='..' +directory1[6][-15:]
        NameLesS8['text']='..' +directory1[7][-15:]
        NameLesS9['text']='..' +directory1[8][-15:]
        NameLesS10['text']='..' +directory1[9][-15:]
        NameLesS11['text']='..' +directory1[10][-15:]
        NameLesS12['text']='..' +directory1[11][-15:]
        messagebox.showwarning(title='Что-то пошло не так!',message="Проверьте количество музыкальных треков!"
                               +"\n"+"Не все звонки озвучены!")
def time_standart():
    STime1.delete(0,END)
    STime1.insert(0,"08:00")
    STime2.delete(0,END)
    STime2.insert(0,"08:55")
    STime3.delete(0,END)
    STime3.insert(0,"09:55")
    STime4.delete(0,END)
    STime4.insert(0,"10:55")
    STime5.delete(0,END)
    STime5.insert(0,"11:50")
    STime6.delete(0,END)
    STime6.insert(0,"12:45")
    STime7.delete(0,END)
    STime7.insert(0,"13:40")
    STime8.delete(0,END)
    STime8.insert(0,"14:35")
    STime9.delete(0,END)
    STime9.insert(0,"15:30")
    STime10.delete(0,END)
    STime10.insert(0,"16:25")
    FTime1.delete(0,END)
    FTime1.insert(0,"08:45")
    FTime2.delete(0,END)
    FTime2.insert(0,"09:40")
    FTime3.delete(0,END)
    FTime3.insert(0,"10:40")
    FTime4.delete(0,END)
    FTime4.insert(0,"11:40")
    FTime5.delete(0,END)
    FTime5.insert(0,"12:35")
    FTime6.delete(0,END)
    FTime6.insert(0,"13:30")
    FTime7.delete(0,END)
    FTime7.insert(0,"14:25")
    FTime8.delete(0,END)
    FTime8.insert(0,"15:20")
    FTime9.delete(0, END)
    FTime9.insert(0, "16:15")
    FTime10.delete(0, END)
    FTime10.insert(0, "17:10")

    STime1S.delete(0,END)
    STime1S.insert(0,"08:00")
    STime2S.delete(0,END)
    STime2S.insert(0,"08:50")
    STime3S.delete(0,END)
    STime3S.insert(0,"09:45")
    STime4S.delete(0,END)
    STime4S.insert(0,"10:40")
    STime5S.delete(0,END)
    STime5S.insert(0,"11:30")
    STime6S.delete(0,END)
    STime6S.insert(0,"12:20")
    FTime1S.delete(0,END)
    FTime1S.insert(0,"08:45")
    FTime2S.delete(0,END)
    FTime2S.insert(0,"09:35")
    FTime3S.delete(0,END)
    FTime3S.insert(0,"10:30")
    FTime4S.delete(0,END)
    FTime4S.insert(0,"11:25")
    FTime5S.delete(0,END)
    FTime5S.insert(0,"12:15")
    FTime6S.delete(0,END)
    FTime6S.insert(0,"13:05")
def time_last():
    try:
        last_t = open('lessons.txt')
        lines=last_t.read().split('\n')
        STime1.delete(0, END)
        STime1.insert(0, lines[0])
        FTime1.delete(0, END)
        FTime1.insert(0, lines[1])
        STime2.delete(0, END)
        STime2.insert(0, lines[2])
        FTime2.delete(0, END)
        FTime2.insert(0, lines[3])
        STime3.delete(0, END)
        STime3.insert(0, lines[4])
        FTime3.delete(0, END)
        FTime3.insert(0, lines[5])
        STime4.delete(0, END)
        STime4.insert(0, lines[6])
        FTime4.delete(0, END)
        FTime4.insert(0, lines[7])
        STime5.delete(0, END)
        STime5.insert(0, lines[8])
        FTime5.delete(0, END)
        FTime5.insert(0, lines[9])
        STime6.delete(0, END)
        STime6.insert(0, lines[10])
        FTime6.delete(0, END)
        FTime6.insert(0, lines[11])
        STime7.delete(0, END)
        STime7.insert(0, lines[12])
        FTime7.delete(0, END)
        FTime7.insert(0, lines[13])
        STime8.delete(0, END)
        STime8.insert(0, lines[14])
        FTime8.delete(0, END)
        FTime8.insert(0, lines[15])
        STime9.delete(0, END)
        STime9.insert(0, lines[16])
        FTime9.delete(0, END)
        FTime9.insert(0, lines[17])
        STime10.delete(0, END)
        STime10.insert(0, lines[18])
        FTime10.delete(0, END)
        FTime10.insert(0, lines[19])
        STime1S.delete(0, END)
        STime1S.insert(0, lines[20])
        FTime1S.delete(0, END)
        FTime1S.insert(0, lines[21])
        STime2S.delete(0, END)
        STime2S.insert(0, lines[22])
        FTime2S.delete(0, END)
        FTime2S.insert(0, lines[23])
        STime3S.delete(0, END)
        STime3S.insert(0, lines[24])
        FTime3S.delete(0, END)
        FTime3S.insert(0, lines[25])
        STime4S.delete(0, END)
        STime4S.insert(0, lines[26])
        FTime4S.delete(0, END)
        FTime4S.insert(0, lines[27])
        STime5S.delete(0, END)
        STime5S.insert(0, lines[28])
        FTime5S.delete(0, END)
        FTime5S.insert(0, lines[29])
        STime6S.delete(0, END)
        STime6S.insert(0, lines[30])
        FTime6S.delete(0, END)
        FTime6S.insert(0, lines[31])
        last_t.close()
    except:
        time_standart()
def time_short():
    STime1.delete(0,END)
    STime1.insert(0,"08:00")
    STime2.delete(0,END)
    STime2.insert(0,"08:40")
    STime3.delete(0,END)
    STime3.insert(0,"09:20")
    STime4.delete(0,END)
    STime4.insert(0,"10:05")
    STime5.delete(0,END)
    STime5.insert(0,"10:45")
    STime6.delete(0,END)
    STime6.insert(0,"11:25")
    STime7.delete(0,END)
    STime7.insert(0,"12:05")
    STime8.delete(0,END)
    STime8.insert(0,"12:45")
    STime9.delete(0,END)
    STime10.delete(0,END)
    FTime1.delete(0,END)
    FTime1.insert(0,"08:35")
    FTime2.delete(0,END)
    FTime2.insert(0,"09:15")
    FTime3.delete(0,END)
    FTime3.insert(0,"09:55")
    FTime4.delete(0,END)
    FTime4.insert(0,"10:40")
    FTime5.delete(0,END)
    FTime5.insert(0,"11:20")
    FTime6.delete(0,END)
    FTime6.insert(0,"12:00")
    FTime7.delete(0,END)
    FTime7.insert(0,"12:40")
    FTime8.delete(0,END)
    FTime9.delete(0,END)
    FTime10.delete(0,END)
    FTime8.insert(0,"13:20")
    STime1S.delete(0,END)
    STime1S.insert(0,"08:00")
    STime2S.delete(0,END)
    STime2S.insert(0,"08:40")
    STime3S.delete(0,END)
    STime3S.insert(0,"09:20")
    STime4S.delete(0,END)
    STime4S.insert(0,"10:05")
    STime5S.delete(0,END)
    STime5S.insert(0,"10:45")
    STime6S.delete(0,END)
    STime6S.insert(0,"11:25")
    FTime1S.delete(0,END)
    FTime1S.insert(0,"08:35")
    FTime2S.delete(0,END)
    FTime2S.insert(0,"09:15")
    FTime3S.delete(0,END)
    FTime3S.insert(0,"09:55")
    FTime4S.delete(0,END)
    FTime4S.insert(0,"10:40")
    FTime5S.delete(0,END)
    FTime5S.insert(0,"11:20")
    FTime6S.delete(0,END)
    FTime6S.insert(0,"12:00")
    
#------------------------------------------------------------------------------    
mainmenu = Menu(root) 
root.config(menu=mainmenu) 

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command (label="Выбор музыки БУДНИ",command=ChoiceM)
filemenu.add_command (label="Выбор музыки СУББОТА",command=ChoiceS)
filemenu.add_command (label="Установить стнадартное время звонков",command=time_standart)
filemenu.add_command (label="Установить сокращенное время звонков",command=time_short)
filemenu.add_command (label="Остановить проигрывание музыки",command=stopM)

helpmenu= Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Инструкция",command=instruction)
helpmenu.add_command(label="Техническая поддержка",command=Support)
helpmenu.add_command(label="О програме",command=Aboutprog)


mainmenu.add_cascade(label='Меню',menu=filemenu)
mainmenu.add_cascade(label='Справка',menu=helpmenu)

frameweek = LabelFrame(root,text="Будни",bd=2,width=280,height=535)
frameweek.place(x=5,y=5)
framesaturday = LabelFrame(root,text="Суббота",bd=2,width=280,height=330)
framesaturday.place(x=290,y=5)
for i1 in range(0,10):
#-------------------------Labels_weekdays-------------------------------------
    SLes=Label(frameweek,text='На {} урок:'.format(i1+1),font='arial 10')
    SLes.place(x=5,y=i1*50+20)
    FLes=Label(frameweek,text='C {} урока:'.format(i1+1),font='arial 10')
    FLes.place(x=160,y=i1*50+20)
#-------------------------Labels_saturday--------------------------------------
    if i1<=5:
        SLesS=Label(framesaturday,text='На {} урок:'.format(i1+1),font='arial 10')
        SLesS.place(x=5,y=i1*50+20)
        FLesS=Label(framesaturday,text='C {} урока:'.format(i1+1),font='arial 10')
        FLesS.place(x=160,y=i1*50+20)
#----------------------------------Музыкальное оповещение-------------------------------------

framezaryad = LabelFrame(root,text="Музыкально оповещение",bd=2,width=280,height=80)
framezaryad.place(x=290,y=340)
LabelZar=Label(framezaryad,text='Выберите воспроизводимый файл..',fg='grey')
LabelZar.place(x=1,y=30)
#------------------------------------------------------------------------------
NameLes1=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes1.place(x=5,y=38)
NameLes2=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes2.place(x=5,y=88)
NameLes3=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes3.place(x=5,y=138)
NameLes4=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes4.place(x=5,y=188)
NameLes5=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes5.place(x=5,y=238)
NameLes6=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes6.place(x=5,y=288)
NameLes7=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes7.place(x=5,y=338)
NameLes8=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes8.place(x=5,y=388)
NameLes9=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes9.place(x=5,y=438)
NameLes10=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes10.place(x=5,y=488)
NameLes11=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes11.place(x=160,y=38)
NameLes12=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes12.place(x=160,y=88)
NameLes13=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes13.place(x=160,y=138)
NameLes14=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes14.place(x=160,y=188)
NameLes15=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes15.place(x=160,y=238)
NameLes16=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes16.place(x=160,y=288)
NameLes17=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes17.place(x=160,y=338)
NameLes18=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes18.place(x=160,y=388)
NameLes19=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes19.place(x=160,y=438)
NameLes20=Label(frameweek,text='Не установлено!',font='arial 10',fg='grey')
NameLes20.place(x=160,y=488)

NameLesS1=Label(framesaturday,text='Не установлено!',font='arial 10',fg='grey')
NameLesS1.place(x=5,y=38)
NameLesS2=Label(framesaturday,text='Не установлено!',font='arial 10',fg='grey')
NameLesS2.place(x=5,y=88)
NameLesS3=Label(framesaturday,text='Не установлено!',font='arial 10',fg='grey')
NameLesS3.place(x=5,y=138)
NameLesS4=Label(framesaturday,text='Не установлено!',font='arial 10',fg='grey')
NameLesS4.place(x=5,y=188)
NameLesS5=Label(framesaturday,text='Не установлено!',font='arial 10',fg='grey')
NameLesS5.place(x=5,y=238)
NameLesS6=Label(framesaturday,text='Не установлено!',font='arial 10',fg='grey')
NameLesS6.place(x=5,y=288)
NameLesS7=Label(framesaturday,text='Не установлено!',font='arial 10',fg='grey')
NameLesS7.place(x=160,y=38)
NameLesS8=Label(framesaturday,text='Не установлено!',font='arial 10',fg='grey')
NameLesS8.place(x=160,y=88)
NameLesS9=Label(framesaturday,text='Не установлено!',font='arial 10',fg='grey')
NameLesS9.place(x=160,y=138)
NameLesS10=Label(framesaturday,text='Не установлено!',font='arial 10',fg='grey')
NameLesS10.place(x=160,y=188)
NameLesS11=Label(framesaturday,text='Не установлено!',font='arial 10',fg='grey')
NameLesS11.place(x=160,y=238)
NameLesS12=Label(framesaturday,text='Не установлено!',font='arial 10',fg='grey')
NameLesS12.place(x=160,y=288)
#------------------------------------------------------------------------------


backgr="#F0F0F0" #D9D9D9  #F0F0F0
buttnconst=2 #4
#----------------------------Entry_weekdays--------------------------------

STime1=Entry(frameweek,fg='green',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
STime1['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
STime1.place(x=70,y=20)
STime2=Entry(frameweek,fg='green',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
STime2['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
STime2.place(x=70,y=70)
STime3=Entry(frameweek,fg='green',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
STime3['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
STime3.place(x=70,y=120)
STime4=Entry(frameweek,fg='green',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
STime4['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
STime4.place(x=70,y=170)
STime5=Entry(frameweek,fg='green',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
STime5['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
STime5.place(x=70,y=220)
STime6=Entry(frameweek,fg='green',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
STime6['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
STime6.place(x=70,y=270)
STime7=Entry(frameweek,fg='green',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
STime7['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
STime7.place(x=70,y=320)
STime8=Entry(frameweek,fg='green',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
STime8['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
STime8.place(x=70,y=370)
STime9=Entry(frameweek,fg='green',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
STime9['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
STime9.place(x=70,y=420)
STime10=Entry(frameweek,fg='green',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
STime10['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
STime10.place(x=76,y=470)

FTime1=Entry(frameweek,fg='red',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
FTime1['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
FTime1.place(x=225,y=20)
FTime2=Entry(frameweek,fg='red',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
FTime2['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
FTime2.place(x=225,y=70)
FTime3=Entry(frameweek,fg='red',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
FTime3['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
FTime3.place(x=225,y=120)
FTime4=Entry(frameweek,fg='red',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
FTime4['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
FTime4.place(x=225,y=170)
FTime5=Entry(frameweek,fg='red',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
FTime5['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
FTime5.place(x=225,y=220)
FTime6=Entry(frameweek,fg='red',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
FTime6['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
FTime6.place(x=225,y=270)
FTime7=Entry(frameweek,fg='red',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
FTime7['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
FTime7.place(x=225,y=320)
FTime8=Entry(frameweek,fg='red',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
FTime8['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
FTime8.place(x=225,y=370)
FTime9=Entry(frameweek,fg='red',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
FTime9['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
FTime9.place(x=225,y=420)
FTime10=Entry(frameweek,fg='red',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
FTime10['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
FTime10.place(x=232,y=470)
#------------------------------Entry_saturday-----------------------------

STime1S=Entry(framesaturday,fg='green',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
STime1S['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
STime1S.place(x=70,y=20)
STime2S=Entry(framesaturday,fg='green',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
STime2S['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
STime2S.place(x=70,y=70)
STime3S=Entry(framesaturday,fg='green',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
STime3S['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
STime3S.place(x=70,y=120)
STime4S=Entry(framesaturday,fg='green',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
STime4S['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
STime4S.place(x=70,y=170)
STime5S=Entry(framesaturday,fg='green',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
STime5S['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
STime5S.place(x=70,y=220)
STime6S=Entry(framesaturday,fg='green',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
STime6S['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
STime6S.place(x=70,y=270)
FTime1S=Entry(framesaturday,fg='red',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
FTime1S['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
FTime1S.place(x=225,y=20)
FTime2S=Entry(framesaturday,fg='red',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
FTime2S['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
FTime2S.place(x=225,y=70)
FTime3S=Entry(framesaturday,fg='red',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
FTime3S['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
FTime3S.place(x=225,y=120)
FTime4S=Entry(framesaturday,fg='red',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
FTime4S['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
FTime4S.place(x=225,y=170)
FTime5S=Entry(framesaturday,fg='red',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
FTime5S['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
FTime5S.place(x=225,y=220)
FTime6S=Entry(framesaturday,fg='red',width=5,relief=FLAT,font='arial 10',bg=backgr,validate="key")
FTime6S['validatecommand']=(STime1.register(val_check), '%P', '%i', '%d')
FTime6S.place(x=225,y=270)
time_last()

STime1.bind("<FocusOut>",lambda event,num=1:check(num))
STime2.bind("<FocusOut>",lambda event,num=2:check(num))
STime3.bind("<FocusOut>",lambda event,num=3:check(num))
STime4.bind("<FocusOut>",lambda event,num=4:check(num))
STime5.bind("<FocusOut>",lambda event,num=5:check(num))
STime6.bind("<FocusOut>",lambda event,num=6:check(num))
STime7.bind("<FocusOut>",lambda event,num=7:check(num))
STime8.bind("<FocusOut>",lambda event,num=8:check(num))
STime9.bind("<FocusOut>",lambda event,num=9:check(num))
STime10.bind("<FocusOut>",lambda event,num=10:check(num))
FTime1.bind("<FocusOut>",lambda event,num=11:check(num))
FTime2.bind("<FocusOut>",lambda event,num=12:check(num))
FTime3.bind("<FocusOut>",lambda event,num=13:check(num))
FTime4.bind("<FocusOut>",lambda event,num=14:check(num))
FTime5.bind("<FocusOut>",lambda event,num=15:check(num))
FTime6.bind("<FocusOut>",lambda event,num=16:check(num))
FTime7.bind("<FocusOut>",lambda event,num=17:check(num))
FTime8.bind("<FocusOut>",lambda event,num=18:check(num))
FTime9.bind("<FocusOut>",lambda event,num=19:check(num))
FTime10.bind("<FocusOut>",lambda event,num=20:check(num))

STime1S.bind("<FocusOut>",lambda event,num=21:check(num))
STime2S.bind("<FocusOut>",lambda event,num=22:check(num))
STime3S.bind("<FocusOut>",lambda event,num=23:check(num))
STime4S.bind("<FocusOut>",lambda event,num=24:check(num))
STime5S.bind("<FocusOut>",lambda event,num=25:check(num))
STime6S.bind("<FocusOut>",lambda event,num=26:check(num))
FTime1S.bind("<FocusOut>",lambda event,num=27:check(num))
FTime2S.bind("<FocusOut>",lambda event,num=28:check(num))
FTime3S.bind("<FocusOut>",lambda event,num=29:check(num))
FTime4S.bind("<FocusOut>",lambda event,num=30:check(num))
FTime5S.bind("<FocusOut>",lambda event,num=31:check(num))
FTime6S.bind("<FocusOut>",lambda event,num=32:check(num))
predvar=IntVar()
Predcheck=Checkbutton(root,font='sans 8',variable=predvar,text="Оповещение")
Predcheck.place(x=290,y=425)

Botcheck=Label(root,font='sans 12',bg="#FF0000",text="Offline")
Botcheck.place(x=390,y=425)

filepath_img = ImageTk.PhotoImage(file="filepath.png")
pause_img = ImageTk.PhotoImage(file="pause.png")
play_img = ImageTk.PhotoImage(file="play.png")
return_img = ImageTk.PhotoImage(file="return.png")
stop_img = ImageTk.PhotoImage(file="stop.png")

Askfile=Button(framezaryad,image=filepath_img,relief=FLAT,text='Файл',command=AskFile)
Askfile.place (x=1,y=1)
PlayB=Button(framezaryad,image=play_img,relief=FLAT,state=DISABLED,text='Воспроизвести',command=PlayM)
PlayB.place(x=85,y=1)
StopB=Button(framezaryad,image=stop_img,relief=FLAT,state=DISABLED,text='Стоп',command=stopM)
StopB.place(x=125,y=1)
PauseB=Button(framezaryad,image=pause_img,relief=FLAT,state=DISABLED,text='Пауза',command=pauseM)
PauseB.place(x=165,y=1)
UnpauseB=Button(framezaryad,image=return_img,relief=FLAT,state=DISABLED,text='Продолжить',command=unpauseM)
UnpauseB.place(x=205,y=1)
#------------------------------------------------------------------------
root.mainloop()
