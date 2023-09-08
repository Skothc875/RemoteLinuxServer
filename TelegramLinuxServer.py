#!/usr/bin/python3
#####################################TELEGRAMLINUXSERVER################################################ by Skothc875
# Version: 1.2

import config
if config.lang == 1:
    import languages_folder.EN_lang as lan

elif config.lang == 2:
    import languages_folder.RU_lang as lan 

elif config.lang == 3:
    import languages_folder.ES_lang as lan 

elif config.lang == 4:
    import languages_folder.FR_lang as lan

elif config.lang == 5:
    import languages_folder.DE_lang as lan
         
print(lan.started)
import os
import telebot
import hashlib
import subprocess
import codecs
import time
aut = False
hashpass = config.hashpass
command = []
path = ''
time.sleep(0.3)
subprocess.call("clear", shell=True)

print("#####################################TELEGASERVER#V1.2#################################### by Skothc875")
time.sleep(0.2)
print("                                                                                                              ")
print("                                                                                                              ")
print("                                                                                                              ")
time.sleep(0.2)
print("           LINUX SERVER                                                                                       ")
time.sleep(0.2)
print("        *           *            *                                                                            ")
time.sleep(0.2)
print("         **   ***  ***   * ***  *                                                                             ")
time.sleep(0.2)
print("      ***  ***   **   *****   ** **                            YOUR PC/PHONE                                  ")
time.sleep(0.2)
print("  ****  #    # #  #  #  # #   #   *****                         ___________                                   ")
time.sleep(0.2)
print(" *      #      # ##  #  #  \#/      **       API TELEGRAM       | >_      |                                   ")
time.sleep(0.2)
print("*       #  # # ## #  #  #  /#\        * ----------------------> |         |                                   ")
time.sleep(0.2)
print(" *      #### # #  #  #### #   #      *  <---------------------- |_________|                                   ")
time.sleep(0.2)
print(" *************************************                             /___\                                      ")
time.sleep(0.2)
print("                                                                                                              ")
print("                                                                                                              ")
print("                                                                                                              ")
time.sleep(0.2)
print(lan.press_c)












try:
    bot = telebot.TeleBot(config.token)
except:
    print(lan.fail_started)
rep_send = ''

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, lan.welcome.format(message.from_user, bot.get_me()), parse_mode='html')
    

@bot.message_handler(commands=['auth'])
def auth1(message):
    global rep_send
    rep_send = bot.send_message(message.chat.id, lan.enter_passwd)

    bot.register_next_step_handler(rep_send, auth2)


def auth2(message):
    global aut
    if hashlib.sha512(message.text.encode('utf-8')).hexdigest() == hashpass:

        bot.delete_message(message.chat.id, message.message_id)
        aut = True
        bot.send_message(message.chat.id, lan.auth_success)
        return
    else:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, lan.wrong_pass)


@bot.message_handler(commands=['system'])
def system(message):
    global aut
    if message.chat.type == 'private':
        if aut == True:
            bot.register_next_step_handler(bot.send_message(message.chat.id, lan.enter_comm), start_cm)
        else:
            bot.send_message(message.chat.id, lan.no_access)


def start_cm(message):
    global command
    global path
    command = message.text.split()
    command1 = command.pop(0)

    if command1 == 'cd':
        path = command.pop(0)
        changing_directory(path, message)

    elif command1 == '/download':
        bot.register_next_step_handler(
        bot.send_message(message.chat.id, lan.select_file_down),
        download)

    elif command1 == '/upload':
        bot.register_next_step_handler(
            bot.send_message(message.chat.id, lan.select_file_up),
            upload)

    elif command1 == '/out':
        disconnect(message)


    elif subprocess.call(message.text, shell=True) == 0:

        try:
            bot.send_message(message.chat.id, subprocess.check_output(message.text, shell=True))
        except:
            subprocess.call(message.text, shell=True)
        bot.register_next_step_handler(bot.send_message(message.chat.id, subprocess.check_output("pwd", shell=True) + subprocess.check_output("whoami", shell=True)), start_cm)

    else:
        bot.register_next_step_handler(bot.send_message(message.chat.id, lan.err_comm + str(subprocess.call(message.text, shell=True))), start_cm)


def changing_directory(path, message):
    try:
        os.chdir(path)
        bot.register_next_step_handler(bot.send_message(message.chat.id, subprocess.check_output("pwd", shell=True) + subprocess.check_output("whoami", shell=True)), start_cm)
    except:
    	bot.register_next_step_handler(bot.send_message(message.chat.id, lan.err_cd), start_cm)


def download(message):
    if message.text == '/cancel':
        system(message)
    file = open(message.text, "rb")
    try:
        bot.send_document(message.chat.id, file)
    
    except:
        bot.register_next_step_handler(bot.send_message(message.chat.id, lan.err_sand_file), start_cm)

def upload(message):
    try:
        chat_id = message.chat.id
        now_dir = codecs.decode(subprocess.check_output("pwd", shell=True), 'UTF-8')
        now_dir = now_dir[:-1]

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = now_dir + "/" + message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, lan.file_save_in + now_dir)
    except Exception as e:
        bot.reply_to(message, e)

def disconnect(message):
    global aut
    aut = False
    bot.send_message(message.chat.id, lan.disconnect)

def bot_start()
    try:
        bot.polling(none_stop=True)
        print(lan.host_up)
    except:
        print(lan.err_init)
        print(lan.timeout_60)
        time.sleep(60)
        bot_start()
bot_start()
