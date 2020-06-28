import telebot
from telebot import types
import tokenbot
import time
import player
import DB
#536224858 жорик
# hlebushek

bot = telebot.TeleBot(tokenbot.token,False)

@bot.message_handler(commands=['start'])
def start_message(message):
    s_keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.chat.id in DB.getidadmin2():
        s_keyboard.row('Управление/Главное меню')
        s_keyboard.row('Остановить музыку')
    elif message.chat.id in DB.getidadmin1():
        s_keyboard.row('Управление/Главное меню')
        s_keyboard.row('Остановить музыку')
    else:
        s_keyboard.row('Наши соц-сети')
        s_keyboard.row('Обратная связь')
    bot.send_message(message.chat.id,'Привет, '+message.from_user.first_name+'🙂. '+
                     'Посмотри что я умею с помощью' +'\n'+'/help',
                     reply_markup=s_keyboard)
@bot.message_handler(commands=['help'])
def start_message(message):
    if message.from_user.id in DB.getidadmin2():
        bot.send_message(message.chat.id,'help for admins 2 in editig...')
    elif message.from_user.id in DB.getidadmin1():
        bot.send_message(message.chat.id,'help for admins 1 in editing...')
    else:bot.send_message(message.chat.id,'all about technical support send to @hlebushek22')
@bot.message_handler(commands=['admin'])
def add_admin(message): #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if message.reply_to_message != None \
            and message.reply_to_message.text == 'Напиши свой вопрос и я передам его нужным людям 👌.' \
            and message.reply_to_message.from_user.id == 870402262 and message.from_user.id not in DB.getidadmin2():
        admlist=(message.chat.id,message.from_user.id,message.from_user.username)
        DB.admzapr(admlist)
        add_admins = types.InlineKeyboardMarkup(row_width=2)
        adm1 = types.InlineKeyboardButton(text='1 уровень', callback_data='add_a1')
        adm2 = types.InlineKeyboardButton(text='2 уровень', callback_data='add_a2')
        cancel = types.InlineKeyboardButton(text='Отказать', callback_data='cancel_a')
        add_admins.add(adm1, adm2, cancel)
        try:
            for admin in DB.getidadmin2():
                bot.send_message(admin, text='Запрос на админ доступ от @' + message.from_user.username,
                                 reply_markup=add_admins)
        except Exception as e:bot.send_message(524044841,e)
        bot.send_message(message.chat.id, 'Запрос на получение админ прав отправлен, ожидай 🤞.')
    else:
        bot.send_message(message.chat.id, text='❌Недостаточно прав!❌' + '\n' + 'Обратитесь к @hlebushek22🌚!')

@bot.message_handler(content_types=['text'])
def msg_ans(message):
    if message.text=='Наши соц-сети':
        soc = types.InlineKeyboardMarkup(row_width=2)
        facebook_b = types.InlineKeyboardButton(text='Facebook', url='https://www.facebook.com/kramschool22/')
        youtube_b = types.InlineKeyboardButton(text='YouTube',url='https://www.youtube.com/channel/UCt8wCeBkZ1KNwl-KKnZ0yLg')
        soc.add(facebook_b, youtube_b)
        bot.send_message(message.chat.id, "Кликабельный список наших сайтов", reply_markup=soc)
    if message.text=='Обратная связь' and message.from_user.id not in DB.getidadmin1() and message.from_user.id not in DB.getidadmin2():
        back_c=types.ForceReply()
        bot.send_message(message.chat.id,text='Напиши свой вопрос и я передам его нужным людям 👌.'
                         ,reply_markup=back_c)
    if message.text=='Остановить музыку' and message.from_user.id in DB.getidadmin2():
        player.stop()
    if message.text=='Управление/Главное меню':
        if message.chat.id in DB.getidadmin2():
            control = types.InlineKeyboardMarkup(row_width=1)
            change_m= types.InlineKeyboardButton(text='Измение звонков', callback_data='ch_c')
            music_mes= types.InlineKeyboardButton(text='Музыкальное оповещение', callback_data='mus_mes')
            logs= types.InlineKeyboardButton(text='Логирование действий', callback_data='log')
            admins = types.InlineKeyboardButton(text='Администрирование', callback_data='admins')
            control.add(change_m,music_mes,logs,admins)
            bot.send_message(message.chat.id,text='Главное меню',reply_markup=control)
        elif message.chat.id in DB.getidadmin1():
            control = types.InlineKeyboardMarkup(row_width=1)
            music_mes = types.InlineKeyboardButton(text='Музыкальное оповещение', callback_data='mus_mes')
            adm2_con = types.InlineKeyboardButton(text='Контакты', callback_data='adm2_con')
            control.add(music_mes,adm2_con)
            bot.send_message(message.chat.id,text='Главное меню',reply_markup=control)
    if message.reply_to_message != None \
            and message.reply_to_message.text == 'Напиши свой вопрос и я передам его нужным людям 👌.' \
            and message.reply_to_message.from_user.id == 870402262 and message.from_user.id not in DB.getidadmin2():
        for admin in DB.getidadmin2():
            bot.send_message(admin, text='Feedback message:')
            bot.forward_message(admin,message.chat.id,message.message_id)
        bot.send_message(message.chat.id, '☑️')
#----------------------------------Диалог пользователя--------------------------------------
    elif message.reply_to_message != None \
            and message.from_user.id not in DB.getidadmin2() \
            and message.reply_to_message.from_user.id == 870402262:
        for admin in DB.getidadmin2():
            bot.forward_message(admin, message.chat.id, message.message_id)
#--------------------------------------Ответ админ------------------------------------------------
    if message.reply_to_message != None and message.from_user.id in DB.getidadmin2() \
        and message.reply_to_message.from_user.id == 870402262 and message.reply_to_message.forward_from !=None:
        back_c = types.ForceReply()
        bot.send_message(message.reply_to_message.forward_from.id, text=message.text,reply_markup=back_c)

    if message.reply_to_message != None and message.from_user.id in DB.getidadmin2() \
        and message.reply_to_message.text== 'Значение громкости 1..100😉':
        bot.send_chat_action(message.chat.id,'typing') #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if 1<=int(message.text)<=100:
            player.set_volume(int(message.text))
            mus_markup = types.InlineKeyboardMarkup(row_width=2)
            upload = types.InlineKeyboardButton(text="⬇️Загрузить⬇️", callback_data='upl')
            pleer = types.InlineKeyboardButton(text="🎵Плеер🎵", callback_data='pleer')
            vol = types.InlineKeyboardButton(text="🎵Громкость🎵", callback_data='vol')
            stop = types.InlineKeyboardButton(text="🎵Стоп🎵", callback_data='stop')
            back = types.InlineKeyboardButton(text="↩Назад", callback_data='mainmenu')
            mus_markup.add(upload, pleer, vol,stop, back)
            bot.delete_message(message.chat.id, message.message_id)
            bot.delete_message(message.chat.id, int(message.message_id)-1)
            bot.send_message(chat_id=message.chat.id,
                             text='Громкость {}%'.format(message.text), reply_markup=mus_markup)
        else:
            bot.send_message(message.chat.id, text='Не корректные данные ')

    if message.reply_to_message != None and message.from_user.id in DB.getidadmin2() \
        and message.reply_to_message.text[0:39]== 'Введите порядковый номер администратора' \
        and message.text.isdigit():
        DB.dellAdmin(int(message.text))
        bot.delete_message(message.chat.id, message.message_id-1)
        bot.delete_message(message.chat.id, message.message_id)

        s_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        s_keyboard.row('Управление/Главное меню')
        s_keyboard.row('Остановить музыку')

        bot.send_message(message.chat.id,"Пользователь удалён",reply_markup=s_keyboard)
    if message.forward_from != None and message.from_user.id in DB.getidadmin2():
        bot.delete_message(message.chat.id, message.message_id-1)
        bot.delete_message(message.chat.id, message.message_id)
        lvls=types.InlineKeyboardMarkup(row_width=2)
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='mainmenu')
        adm1 = types.InlineKeyboardButton(text="1 уровень", callback_data='add1')
        adm2 = types.InlineKeyboardButton(text="2 уровень", callback_data='add2')
        lvls.add(adm1,adm2, back)
        bot.send_message(message.chat.id,str(message.forward_from.id) + ',@'+
                         str(message.forward_from.username),reply_markup=lvls)

#---------------------------Главное меню----------------------------------------------
@bot.message_handler(content_types=['audio'])
def audio_message(message):
    if message.reply_to_message != None and message.from_user.id in DB.getidadmin2() \
        and message.reply_to_message.text == 'Отправь мне музыку в ответ на это сообщение😉':
        mus_markup = types.InlineKeyboardMarkup(row_width=2)
        pleer = types.InlineKeyboardButton(text="🎵Плеер🎵", callback_data='pleer')
        vol = types.InlineKeyboardButton(text="🎵Громкость🎵", callback_data='vol')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='mainmenu')
        mus_markup.add(pleer, vol, back)
        bot.send_message(chat_id=message.chat.id,
                         text='Аудиозапись {0} - {1} загружается...'.format(message.audio.title,message.audio.performer))
        try:
            file_info = bot.get_file(message.audio.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            if message.audio.performer != '<unknown>':
                global src
                global file_pl
                file_pl = str(message.audio.title)+'—'+str(message.audio.performer)
                src = '{0} — {1}.mp3'.format(message.audio.title,message.audio.performer)
            else:src = '{0}.mp3'.format(message.audio.title)
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
        except Exception as e:
            bot.reply_to(message, e)
        bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id+1,
                              text='Аудиозапись {0} - {1} загружена'.format(message.audio.title,message.audio.performer)
                              ,reply_markup=mus_markup)
        bot.delete_message(message.chat.id,message.message_id)
        bot.delete_message(message.chat.id,int(message.message_id)-1)
@bot.callback_query_handler(func=lambda call: True)
def start_message1(call):
    s_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    s_keyboard.row('Управление/Главное меню')
    s_keyboard.row('Остановить музыку')
#-1------------------------------------Главное меню------------------------------------------------
    if call.data =='mainmenu':
        bot.answer_callback_query(call.id,'Main menu test')
        if call.message.chat.id in DB.getidadmin2():
            control = types.InlineKeyboardMarkup(row_width=1)
            change_m = types.InlineKeyboardButton(text='Измение звонков', callback_data='ch_c')
            music_mes = types.InlineKeyboardButton(text='Музыкальное оповещение', callback_data='mus_mes')

            logs = types.InlineKeyboardButton(text='Логирование действий', callback_data='log')
            admins = types.InlineKeyboardButton(text='Администрирование', callback_data='admins')
            control.add(change_m, music_mes, logs, admins)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Главное меню', reply_markup=control)
        elif call.message.chat.id in DB.getidadmin1():
            control = types.InlineKeyboardMarkup(row_width=1)
            music_mes = types.InlineKeyboardButton(text='Музыкальное оповещение', callback_data='mus_mes')
            adm2_con = types.InlineKeyboardButton(text='Контакты', callback_data='adm2_con')
            control.add(music_mes, adm2_con)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Главное меню', reply_markup=control)

#-2----------------------------------Измение звонков-------------------------------------------
    if call.data == 'ch_c':
        dni_ned=types.InlineKeyboardMarkup(row_width=1)
        weekdays = types.InlineKeyboardButton(text="Будние", callback_data='weekdays')
        holidays = types.InlineKeyboardButton(text="Суббота", callback_data='holdays')
        mainmenu = types.InlineKeyboardButton(text="↩Назад", callback_data='mainmenu')
        dni_ned.add(weekdays, holidays, mainmenu)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберите дни недели для изменения звонка', reply_markup=dni_ned)
#-3---------------------------------
    if call.data == 'weekdays':
        edit_week=types.InlineKeyboardMarkup(row_width=4)
        les1 = types.InlineKeyboardButton(text="1️⃣", callback_data='les1')
        les2 = types.InlineKeyboardButton(text="2️⃣", callback_data='les2')
        les3 = types.InlineKeyboardButton(text="3️⃣", callback_data='les3')
        les4 = types.InlineKeyboardButton(text="4️⃣", callback_data='les4')
        les5 = types.InlineKeyboardButton(text="5️⃣", callback_data='les5')
        les6 = types.InlineKeyboardButton(text="6️⃣", callback_data='les6')
        les7 = types.InlineKeyboardButton(text="7️⃣", callback_data='les7')
        les8 = types.InlineKeyboardButton(text="8️⃣", callback_data='les8')
        vse = types.InlineKeyboardButton(text="🎵Все🎵", callback_data='vse')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='ch_c')
        edit_week.add(les1,les2,les3,les4,les5,les6,les7,les8,vse,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text='Выберите номер урока для редактирования',reply_markup=edit_week)

#-4-------------------------------
    if call.data == 'les1':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        les_s = types.InlineKeyboardButton(text="На 1️⃣ урок", callback_data='les_s1')
        les_f = types.InlineKeyboardButton(text="С 1️⃣ урока", callback_data='les_f1')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='weekdays')
        edit_type.add(les_s,les_f, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберите номер урока для редактирования', reply_markup=edit_type)
    if call.data == 'les2':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        les_s = types.InlineKeyboardButton(text="На 2️⃣ урок", callback_data='les_s2')
        les_f = types.InlineKeyboardButton(text="С 2️⃣ урока", callback_data='les_f2')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='weekdays')
        edit_type.add(les_s, les_f, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Выберите номер урока для редактирования', reply_markup=edit_type)
    if call.data == 'les3':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        les_s = types.InlineKeyboardButton(text="На 3️⃣ урок", callback_data='les_s3')
        les_f = types.InlineKeyboardButton(text="С 3️⃣ урока", callback_data='les_f3')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='weekdays')
        edit_type.add(les_s, les_f, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Выберите номер урока для редактирования', reply_markup=edit_type)
    if call.data == 'les4':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        les_s = types.InlineKeyboardButton(text="На 4️⃣ урок", callback_data='les_s4')
        les_f = types.InlineKeyboardButton(text="С 4️⃣ урока", callback_data='les_f4')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='weekdays')
        edit_type.add(les_s, les_f, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Выберите номер урока для редактирования', reply_markup=edit_type)
    if call.data == 'les5':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        les_s = types.InlineKeyboardButton(text="На 5️⃣ урок", callback_data='les_s5')
        les_f = types.InlineKeyboardButton(text="С 5️⃣ урока", callback_data='les_f5')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='weekdays')
        edit_type.add(les_s, les_f, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Выберите номер урока для редактирования', reply_markup=edit_type)
    if call.data == 'les6':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        les_s = types.InlineKeyboardButton(text="На 6️⃣ урок", callback_data='les_s6')
        les_f = types.InlineKeyboardButton(text="С6️⃣ урока", callback_data='les_f6')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='weekdays')
        edit_type.add(les_s, les_f, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Выберите номер урока для редактирования', reply_markup=edit_type)
    if call.data == 'les7':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        les_s = types.InlineKeyboardButton(text="На 7️⃣ урок", callback_data='les_s7')
        les_f = types.InlineKeyboardButton(text="С 7️⃣ урока", callback_data='les_f7')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='weekdays')
        edit_type.add(les_s, les_f, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Выберите номер урока для редактирования', reply_markup=edit_type)
    if call.data == 'les8':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        les_s = types.InlineKeyboardButton(text="На 8️⃣ урок", callback_data='les_s8')
        les_f = types.InlineKeyboardButton(text="С 8️⃣ урок", callback_data='les_f8')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='weekdays')
        edit_type.add(les_s, les_f, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Выберите номер урока для редактирования', reply_markup=edit_type)
#-5-------------------------
    if call.data == 'les_s1':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_ts1 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_ts1')
        ch_ms1 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_ms1')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les1')
        edit_type.add(ch_ts1, ch_ms1, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_f1':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_tf1 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_tf1')
        ch_mf1 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_mf1')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les1')
        edit_type.add(ch_tf1, ch_mf1, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_s2':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_ts2 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_ts2')
        ch_ms2 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_ms2')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les2')
        edit_type.add(ch_ts2, ch_ms2, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_f2':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_tf2 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_tf2')
        ch_mf2 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_mf2')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les2')
        edit_type.add(ch_tf2, ch_mf2, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_s3':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_ts3 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_ts3')
        ch_ms3 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_ms3')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les3')
        edit_type.add(ch_ts3, ch_ms3, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_f3':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_tf3 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_tf3')
        ch_mf3 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_mf3')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les3')
        edit_type.add(ch_tf3, ch_mf3, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_s4':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_ts4 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_ts4')
        ch_ms4 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_ms4')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les4')
        edit_type.add(ch_ts4, ch_ms4, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_f4':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_tf4 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_tf4')
        ch_mf4 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_mf4')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les4')
        edit_type.add(ch_tf4, ch_mf4, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_s5':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_ts5 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_ts5')
        ch_ms5 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_ms5')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les5')
        edit_type.add(ch_ts5, ch_ms5, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_f5':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_tf5 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_tf5')
        ch_mf5 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_mf5')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les5')
        edit_type.add(ch_tf5, ch_mf5, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_s6':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_ts6 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_ts6')
        ch_ms6 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_ms6')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les6')
        edit_type.add(ch_ts6, ch_ms6, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_f6':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_tf6 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_tf6')
        ch_mf6 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_mf6')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les6')
        edit_type.add(ch_tf6, ch_mf6, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_s7':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_ts7 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_ts7')
        ch_ms7 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_ms7')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les7')
        edit_type.add(ch_ts7, ch_ms7, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_f7':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_tf7 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_tf7')
        ch_mf7 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_mf7')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les7')
        edit_type.add(ch_tf7, ch_mf7, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_s8':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_ts8 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_ts8')
        ch_ms8 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_ms8')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les8')
        edit_type.add(ch_ts8, ch_ms8, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_f8':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_tf8 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_tf8')
        ch_mf8 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_mf8')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les8')
        edit_type.add(ch_tf8, ch_mf8, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
#-3-----------------------------
    if call.data == 'holdays':
        edit_hol = types.InlineKeyboardMarkup(row_width=3)
        les1 = types.InlineKeyboardButton(text="1️⃣", callback_data='les1S')
        les2 = types.InlineKeyboardButton(text="2️⃣", callback_data='les2S')
        les3 = types.InlineKeyboardButton(text="3️⃣", callback_data='les3S')
        les4 = types.InlineKeyboardButton(text="4️⃣", callback_data='les4S')
        les5 = types.InlineKeyboardButton(text="5️⃣", callback_data='les5S')
        les6 = types.InlineKeyboardButton(text="6️⃣", callback_data='les6S')
        vse = types.InlineKeyboardButton(text="🎵Все🎵", callback_data='vse')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='ch_c')
        edit_hol.add(les1, les2, les3, les4, les5, les6,vse,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберите номер урока для редактирования', reply_markup=edit_hol)

#-4----------------------------
    if call.data == 'les1S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        les_s = types.InlineKeyboardButton(text="На 1️⃣ урок", callback_data='les_s1S')
        les_f = types.InlineKeyboardButton(text="С 1️⃣ урока", callback_data='les_f1S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='holdays')
        edit_type.add(les_s, les_f, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберите номер урока для редактирования', reply_markup=edit_type)
    if call.data == 'les2S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        les_s = types.InlineKeyboardButton(text="На 2️⃣ урок", callback_data='les_s2S')
        les_f = types.InlineKeyboardButton(text="С 2️⃣ урока", callback_data='les_f2S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='holdays')
        edit_type.add(les_s, les_f, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Выберите номер урока для редактирования', reply_markup=edit_type)
    if call.data == 'les3S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        les_s = types.InlineKeyboardButton(text="На 3️⃣ урок", callback_data='les_s3S')
        les_f = types.InlineKeyboardButton(text="С 3️⃣ урока", callback_data='les_f3S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='holdays')
        edit_type.add(les_s, les_f, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Выберите номер урока для редактирования', reply_markup=edit_type)
    if call.data == 'les4S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        les_s = types.InlineKeyboardButton(text="На 4️⃣ урок", callback_data='les_s4S')
        les_f = types.InlineKeyboardButton(text="С 4️⃣ урока", callback_data='les_f4S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='holdays')
        edit_type.add(les_s, les_f, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Выберите номер урока для редактирования', reply_markup=edit_type)
    if call.data == 'les5S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        les_s = types.InlineKeyboardButton(text="На 5️⃣ урок", callback_data='les_s5S')
        les_f = types.InlineKeyboardButton(text="С 5️⃣ урока", callback_data='les_f5S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='holdays')
        edit_type.add(les_s, les_f, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Выберите номер урока для редактирования', reply_markup=edit_type)
    if call.data == 'les6S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        les_s = types.InlineKeyboardButton(text="На 6️⃣ урок", callback_data='les_s6S')
        les_f = types.InlineKeyboardButton(text="С 6️⃣ урока", callback_data='les_f6S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='holdays')
        edit_type.add(les_s, les_f, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберите номер урока для редактирования', reply_markup=edit_type)
#-5-------------------------------
    if call.data == 'les_s1S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_ts1 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_ts1S')
        ch_ms1 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_ms1S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les1S')
        edit_type.add(ch_ts1, ch_ms1, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_f1S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_tf1 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_tf1S')
        ch_mf1 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_mf1S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les1S')
        edit_type.add(ch_tf1, ch_mf1, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_s2S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_ts1 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_ts2S')
        ch_ms1 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_ms2S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les2S')
        edit_type.add(ch_ts1, ch_ms1, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_f2S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_tf1 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_tf2S')
        ch_mf1 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_mf2S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les2S')
        edit_type.add(ch_tf1, ch_mf1, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_s3S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_ts1 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_ts3S')
        ch_ms1 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_ms3S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les3S')
        edit_type.add(ch_ts1, ch_ms1, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_f3S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_tf1 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_tf3S')
        ch_mf1 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_mf3S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les3S')
        edit_type.add(ch_tf1, ch_mf1, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_s4S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_ts1 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_ts4S')
        ch_ms1 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_ms4S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les4')
        edit_type.add(ch_ts1, ch_ms1, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_f4S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_tf1 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_tf4S')
        ch_mf1 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_mf4S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les4S')
        edit_type.add(ch_tf1, ch_mf1, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_s5S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_ts1 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_ts5S')
        ch_ms1 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_ms5S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les5S')
        edit_type.add(ch_ts1, ch_ms1, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_f5S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_tf1 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_tf5S')
        ch_mf1 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_mf5S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les5S')
        edit_type.add(ch_tf1, ch_mf1, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_s6S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_ts1 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_ts6S')
        ch_ms1 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_ms6S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les6S')
        edit_type.add(ch_ts1, ch_ms1, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
    if call.data == 'les_f6S':
        edit_type = types.InlineKeyboardMarkup(row_width=2)
        ch_tf1 = types.InlineKeyboardButton(text="Изменить 🕐", callback_data='ch_tf6S')
        ch_mf1 = types.InlineKeyboardButton(text="Загрузить 🎵", callback_data='ch_mf6S')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='les6S')
        edit_type.add(ch_tf1, ch_mf1, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                      text='Текущее время:'+'\n'+'Текущая музыка:', reply_markup=edit_type)
#----------------------------Музыкальное оповещение-----------------------------------
    if call.data == 'mus_mes':
        mus_markup = types.InlineKeyboardMarkup(row_width=2)
        upload = types.InlineKeyboardButton(text="⬇️Загрузить⬇️", callback_data='upl')
        pleer = types.InlineKeyboardButton(text="🎵Плеер🎵", callback_data='pleer')
        vol = types.InlineKeyboardButton(text="🎵Громкость🎵", callback_data='vol')
        stop = types.InlineKeyboardButton(text="🎵Стоп🎵", callback_data='stop')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='mainmenu')
        mus_markup.add(upload, pleer,vol,stop, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Музыкальное оповещение', reply_markup=mus_markup)

    if call.data == 'upl':
        bot.delete_message(call.message.chat.id,call.message.message_id)
        repl_audio = types.ForceReply()
        bot.send_message(chat_id=call.message.chat.id,text='Отправь мне музыку в ответ на это сообщение😉',
                         reply_markup=repl_audio)
    if call.data == 'pleer':
        bot.answer_callback_query(call.id,'Воспроизвожу ...')
        mus_markup = types.InlineKeyboardMarkup(row_width=2)
        upload = types.InlineKeyboardButton(text="⬇️Загрузить⬇️", callback_data='upl')
        pleer = types.InlineKeyboardButton(text="🎵Плеер🎵", callback_data='pleer')
        vol = types.InlineKeyboardButton(text="🎵Громкость🎵", callback_data='vol')
        stop = types.InlineKeyboardButton(text="🎵Стоп🎵", callback_data='stop')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='mainmenu')
        mus_markup.add(upload, pleer, vol,stop, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Играет {0}'.format(file_pl), reply_markup=mus_markup)
        player.play(src)
    if call.data == 'vol':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        repl_audio = types.ForceReply()
        bot.send_message(chat_id=call.message.chat.id, text='Значение громкости 1..100😉',
                 reply_markup=repl_audio)
    if call.data =='stop':
        player.stop()

#---------------------------Логирование--------------------------------------------------
    if call.data == 'log':
        log_markup = types.InlineKeyboardMarkup(row_width=3)
        five = types.InlineKeyboardButton(text="5", callback_data='log5')
        ten = types.InlineKeyboardButton(text="10", callback_data='log10')
        twenty = types.InlineKeyboardButton(text="20", callback_data='log20')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='mainmenu')
        log_markup.add(five,ten,twenty,back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Отобразить последние действия.',reply_markup=log_markup)
    if call.data == 'log5':
        pass
    if call.data == 'log10':
        pass
    if call.data == 'log20':
        pass
#--------------------------------Администрирование----------------------------------------
    if call.data == 'admins':
        adm_markup = types.InlineKeyboardMarkup(row_width=2)
        del_a = types.InlineKeyboardButton(text="Удалить", callback_data='del_a')
        adda = types.InlineKeyboardButton(text="Добавить", callback_data='addAdm')
        back = types.InlineKeyboardButton(text="↩Назад", callback_data='mainmenu')
        adm_markup.add(del_a,adda, back)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=DB.admlist(),reply_markup=adm_markup)

    if call.data == 'add_a1':
        DB.admzapr1(call.message.text[27:])
        chatid,nickid = DB.admzapr1()
        bot.delete_message(call.message.chat.id,call.message.message_id)
        for admin in DB.getidadmin2():
            bot.send_message(admin, text='Выдан 1 уровень администрации пользователю: @{0}, accepted by @{1}src'
                             .format(nickid,call.from_user.username))
        bot.send_message(chatid,text='Вам выдан 1 уровень администрирования🙃. Жми /start')
    if call.data == 'add_a2':
        DB.admzapr2(call.message.text[27:])
        nickid = DB.admzapr2()
        bot.delete_message(call.message.chat.id, call.message.message_id)
        for admin in DB.getidadmin2():
            bot.send_message(admin, text='Выдан 2 уровень администрации пользователю: @{0}, accepted by @{1}'
                             .format(nickid, call.from_user.username))
    if call.data == 'cancel_a':
        DB.canceladm(call.message.text[27:])
        chatid,nickid = DB.canceladm()
        bot.send_message(chatid, text='Отказано 😿.')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Отказано @'+nickid+', by @'+call.from_user.username)

    if call.data == 'addAdm':
        bot.delete_message(call.message.chat.id,call.message.message_id)
        bot.send_message(call.message.chat.id,'Перешлите любое сообщение')
    if call.data == 'add1':
        DB.addAdmin('1,'+call.message.text)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, text='Выдан 1 уровень администрации пользователю: '+call.message.text,
                         reply_markup=s_keyboard)
    if call.data == 'add2':
        DB.addAdmin('2,'+call.message.text)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, text='Выдан 1 уровень администрации пользователю: '+call.message.text,
                         reply_markup=s_keyboard)
    if call.data == 'del_a':
        listAdm=DB.admlist()
        bot.delete_message(call.message.chat.id, call.message.message_id)
        repl_admin = types.ForceReply()
        bot.send_message(chat_id=call.message.chat.id,text='Введите порядковый номер администратора'+'\n'
                                   +'\n'+listAdm,reply_markup=repl_admin)


@bot.inline_handler(lambda query: query.query == 'test')
def query_text(inline_query):
    print(inline_query)
    try:
        r = types.InlineQueryResultArticle('1', 'Result1', types.InputTextMessageContent('hi'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('hi'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'text')
def query_audio (inline_query):
    print(inline_query)
    try:
        r = types.InlineQueryResultAudio('1', 'Result1')
        r2 = types.InlineQueryResultAudio('2', 'Result2')
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)
if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True)

        except Exception as e:
            print(e)
            time.sleep(10)