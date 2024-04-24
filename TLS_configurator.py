import hashlib
import subprocess
cho_lang = True
try:
    import telebot
except:
    subprocess.call("pip install pyTelegramBotAPI", shell=True)

while cho_lang:
    print("1) English")
    print("2) Russian")
    print("3) Spanish")
    print("4) French")
    print("5) German")
    language = int(input("Choose your language: "))
    if language == 1:
        import languages_folder.EN_lang as lan
        cho_lang = False
    
    elif language == 2:
        import languages_folder.RU_lang as lan
        cho_lang = False

    elif language == 3:
        import languages_folder.ES_lang as lan
        cho_lang = False 

    elif language == 4:
        import languages_folder.FR_lang as lan
        cho_lang = False 

    elif language == 5:
        import languages_folder.DE_lang as lan
        cho_lang = False 

    else:
        print("You have chosen the wrong language.")

token = input(lan.enter_token)
passwd = input(lan.enter_passwd_set)
conffile = open('config.py', 'w', encoding='utf-8')
conffile.write("lang = " + str(language) + "\n")
conffile.write("hashpass = '" + (hashlib.sha512(passwd.encode('utf-8')).hexdigest() + "'\n"))
conffile.write("token = '" + token + "'\n")
print(lan.file_configured)
