#!/usr/bin/python3
#####################################TELEGRAMLINUXSERVER################################################ by Skothc875
# Version: 1.1

print("[+]TelegaServer started")
import config
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

print("#####################################TELEGASERVER#V1.1#################################### by Skothc875")
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
print("  PRESS TO CTRL + C FOR EXIT                                                                                  ")












try:
    bot = telebot.TeleBot(config.token)
except:
    print("Не удалосьзапустить бота:(")
rep_send = ''

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - твой компьютер.\n/auth - аунтификация на сервере\n/system - осуществляет доступ к серверу.\nБолее подробно о командах бота в документации.".format(message.from_user, bot.get_me()), parse_mode='html')
    

@bot.message_handler(commands=['auth'])
def auth1(message):
    global rep_send
    rep_send = bot.send_message(message.chat.id, "Введите пароль от сервера для аунтефикации.")

    bot.register_next_step_handler(rep_send, auth2)


def auth2(message):
    global aut
    if hashlib.sha512(message.text.encode('utf-8')).hexdigest() == hashpass:

        bot.delete_message(message.chat.id, message.message_id)
        aut = True
        bot.send_message(message.chat.id, "Аутентификация прошла успешо.")
        return
    else:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Пароль не верный")


@bot.message_handler(commands=['system'])
def system(message):
    global aut
    if message.chat.type == 'private':
        if aut == True:
            bot.register_next_step_handler(bot.send_message(message.chat.id, "Введите команду."), start_cm)
        else:
            bot.send_message(message.chat.id, "У вас нет доступа.")


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
        bot.send_message(message.chat.id, "Выберите файл который хотите загрузить из данной дерриктории."),
        download)

    elif command1 == '/upload':
        bot.register_next_step_handler(
            bot.send_message(message.chat.id, "Выберите файл который хотите выгрузить в данную деррикторию."),
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
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Произошла ошибка при выполнении команды. Код ошибки: " + str(subprocess.call(message.text, shell=True))), start_cm)


def changing_directory(path, message):
    try:
        os.chdir(path)
        bot.register_next_step_handler(bot.send_message(message.chat.id, subprocess.check_output("pwd", shell=True) + subprocess.check_output("whoami", shell=True)), start_cm)
    except:
    	bot.register_next_step_handler(bot.send_message(message.chat.id, "Произошла ошибка смены дериктории, возможно вы не правильно указали путь."), start_cm)


def download(message):
    if message.text == '/cancel':
        system(message)
    file = open(message.text, "rb")
    try:
        bot.send_document(message.chat.id, file)
    
    except:
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Ошибка при отправке файла,проверьре назваие файла."), start_cm)

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

        bot.reply_to(message, "Файл успешно сохранён в дерриктории " + now_dir)
    except Exception as e:
        bot.reply_to(message, e)

def disconnect(message):
    global aut
    aut = False
    bot.send_message(message.chat.id, "Отключение от сервера...")
    
try:
    bot.polling(none_stop=True)


except:
    print("Ошибка при иницилизации бота.")


