import smtplib
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from colorama import init
init()
from colorama import Fore, Back, Style
from pystyle import *
import webbrowser
webbrowser.open('https://t.me/SoftQWK1XIII')
intro = """                                                                                                      


      
                 v1 by Diced_0 and EFall88
                Based on Trinity v1.0.1 
            
------------------------------            


     Enter что бы продолжить
                                                                       
 
                 """
try:
      Anime.Fade(Center.Center(intro), Colors.red_to_green, Colorate.Vertical, interval=0.045, enter=True)
except Exception as e:
    print(f"An error occurred: {e}")

banner = """                                                                                                                                                                         
"""

text = """
                                                
                             ██████╗  █████╗ ██╗ ██████╗ █████╗ ███╗  ██╗
                             ██╔══██╗██╔══██╗██║██╔════╝██╔══██╗████╗ ██║
                             ██████╔╝██║░░██║██║╚█████╗ ██║░░██║██╔██╗██║
                             ██╔═══╝ ██║░░██║██║ ╚═══██╗██║░░██║██║╚████║
                             ██║     ╚█████╔╝██║██████╔╝╚█████╔╝██║ ╚███║
                             ╚═╝      ╚════╝ ╚═╝╚═════╝  ╚════╝ ╚═╝  ╚══╝         
                                      Powered by Korinity Ultra V3

 
                                            ██╗░░░██╗░░███╗░░
                                            ██║░░░██║░████║░░
                                            ╚██╗░██╔╝██╔██║░░
                                            ░╚████╔╝░╚═╝██║░░
                                            ░░╚██╔╝░░███████╗
                                            ░░░╚═╝░░░╚══════╝

  
                                            version - 1.0.0 
                                             price - Diced_0
  ┌───────────────────────────┐      ┌───────────────────────────┐      ┌───────────────────────────┐ 
  │ (1) |   CНЕСТИ   ЧЕЛА     │      │ (2) |    СНЕСТИ  КАНАЛ    │      │ (3) |     СНЕСТИ БОТА     │
  └───────────────────────────┘      └───────────────────────────┘      └───────────────────────────┘
                             Выбрав цифру вы соглашаетесь с данным текстом                    
                                                                                                                                                                   
                     """
print()
print(Colorate.Vertical(Colors.yellow_to_red, Center.XCenter(banner)))
print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter(text)))



COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}

senders = {
    'prekrasno.el@yandex.ru': 'RakuzanSnos',
    'evg-struzhenkov@yandex.ru': 'zmARvx1MRvXppZV6xkXj',
    'bagryancdv_sergey@mail': '1CtFuHTaQxNda8X06CaQ',
    'ovchinnikova@inbox.ru': 'SXxrCndCR59s5G9sGc6L',
'nastiay1996@mail.ru': 'Zorro1ab',
'piyavka@9inbox.ru': 'Holly1!',
'voronoy_62@mail.ru': 'Pass1178',
'cena100@mail.ru': 'Quinton2329!',
'liznees@verizon.net': 'Dancer008',
'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
'kcdg@charter.net': 'Jennifer3*',
'bean_118@hotmail.com': 'Liverpool118!',
'dsdhjas@mail.com': 'LONGHACH123',
'robitwins@comcast.net': 'May241996',
'wasina@live.com': 'Marlas21',
'aruzhan.01@mail.com': '1234567!',
'rob.tackett@live.com': 'metallic',
'lindahallenbeck@verizon.net': 'Anakin@2014',
'hlaw82@mail.com': 'Snoopy37$$',
'paintmadman@comcast.net': 'mycat2200*',
'prideandjoy@verizon.net': 'Ihatejen12',
'sdgdfg56@mail.com': 'kenwood4201',
'garrett.danelz@comcast.net': 'N11golfer!',
'gillian_1211@hotmail.com': 'Gilloveu1211',
'sunpit16@hotmail.com': 'Putter34!',
'fdshelor@verizon.net': 'Masco123*',
'yeags1@cox.net': 'Zoomom1965!',
'amine002@usa.com': 'iScrRoXAei123',
'bbarcelo16@cox.net': 'Bsb161089$$',
'laliebert@hotmail.com': 'pirates2',
'vallen285@comcast.net': 'Delft285!1!',
'sierra12@email.com': 'tegen1111',
'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
'kmay@windstream.net': 'Nascar98',
'redbrick1@mail.com': 'Redbrick11',
'ivv9ah7f@mail.com': 'K226nw8duwg',
'erkobir@live.com': 'floydLAWTON019',
'Misscarter@mail.com': 'ashtray19',
'carlieruby10@cox.net': 'Lollypop789$',
'blackops2013@mail.com': 'amason123566',
'caroline_cullum@comcast.net': 'carter14',
'dpb13@live.com': 'Ic&ynum13',
'heirhunter@usa.com': 'Noguys@714',
'sherri.edwards@verizon.net': 'Dreaming123#',
'rami.rami1980@hotmail.com': 'ramirami1980',
'jmsingleton2@comcast.net': '151728Jn$$',
'aberancho@aol.com': '10diegguuss10',
'dgidel@iowatelecom.net': 'Buster48',
'gpopandopul@mail.com': 'GEORG62A',
'bolgodonsk@mail.com': '012345678!',
'colbycolb@cox.net': 'Signals@1'
}
receivers = ['stopCA@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org']

def logo():
    print(Colorate.Horizontal(Colors.red_to_white,Center.XCenter(banner)))
select = input(f'{COLOR_CODE["RED"]}☄ {COLOR_CODE["CYAN"]} НАЖМИ ENTER{COLOR_CODE["CYAN"]} ')
def menu():
    choice = input(f'{COLOR_CODE["RED"]}☠︎{COLOR_CODE["RED"]} Выбери функцию ➤ {COLOR_CODE["RED"]} ')
    return choice
def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(3)
        server.quit()
        return True
    except Exception as e:
        return False

def main():
    sent_emails = 0
    logo()
    choice = menu()
#2
    if choice == '1':
        print("1. СНОСИНГ.")
        print("2. ДОКСUHG.")
        print("3. ТРОЛЛЕНГ.")
        print("4. СНОС СЕССИЙ.")
        print("5. С премкой")
        print("6. С вирт номером.")
        comp_choice = input("выбирай: ")
#чо ты в скрипте забыл ? 
        if comp_choice in ["1", "2", "3"]:
            print("Пиши что скажут.")
            username = input("Username с @: ")
            id = input("ID пользователя: ")
            chat_link = input("Ссылка на чат: ")
            violation_link = input("Ссылка на пост с нарушением: ")
            print("Wait...")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю.",
                "2": f"Здравствуйте, уважаемая поддержка, на вашей платформе я нашел пользователя, который распространяет чужие данные без их согласия. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
                "3": f"Здравствуйте, уважаемая поддержка телеграм. Я нашел пользователя который открыто выражается нецензурной лексикой и спамит в чатах. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                                                 violation_link=violation_link.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 14888
                    time.sleep(5)
#Trinity Legion <3 
        elif comp_choice == "4":
            print("Пиши что скажут")
            username = input("Username обидчика: ")
            id = input("ID пользователя: ")
            print("ЖДИ СУКА ЖДИ.")
            comp_texts = {
                "4": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id}. Пожалуйста удалите аккаунт или обнулите сессии"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice in ["5", "6"]:
            print("следуй указаниям")
            username = input("имя пользователя с @: ")
            id = input("его ID: ")
            comp_texts = {
                "5": f"Добрый день поддержка Telegram!Аккаунт {username} , {id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!",
                "6": f"Добрый день поддержка Telegram! Аккаунт {username} {id} приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram.Прошу проверить данную жалобу и принять меры!"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 9999
                    time.sleep(5)


    elif choice == "2":
        
        print("1. с личными данными")
        print("2. с живодерством ")
        print("3. с цп")
        print("4. для каналов типа прайсов.")
        ch_choice = input("выбор: ")
# t.me/Trinitysoftware
        if ch_choice in ["1", "2", "3", "4"]:
            channel_link = input("ссылка на канал: ")
            channel_violation = input("Ссылка на пост с нарушением: ")
            print("погоди чут чут.")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 100000
                    time.sleep(5)


    elif choice == "3":
        print("1. гэбэ")
        print("2. Пока не придумали")
        bot_ch = input("выбирай ")

        if bot_ch == "1":
            bot_user = input("юз бота ")
            print("Wait...")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота."
                       }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 1
                    time.sleep(5)
        
    elif choice == "4":
        print("soon")
        
    elif choice == "5":
        print("soon")
        
    elif choice == "6":
        exit
        
        

  
if __name__ == "__main__":
    main()
