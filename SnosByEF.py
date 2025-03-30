import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from colored import cprint
import os
from pystyle import Anime, Colors, Colorate, Center

os.system('cls' if os.name == 'nt' else 'clear') 

senders = {
            "misha28272727@gmail.com": "kgwqxvkgjyccibkm",
            "trevorzxasuniga214@gmail.com": "egnr eucw jvxg jatq",
            "dellapreston50@gmail.com": "qoit huon rzsd eewo",
            "neilfdhioley765@gmail.com": "rgco uwiy qrdc gvqh",
            "samuelmnjassey32@gmail.com": "lgct cjiw nufr zxjg",
            "segapro72@gmail.com": "ubmq pbrt ujqy orhf",
            "kurokopotok@gmail.com": "pxww ewut uffz ufpu",
            "kalievutub@gmail.com": "jlwb otxo mppi jvdh",
            "snosakka07@gmail.com": "yiro khva gafc lujr",
            "prosega211@gmail.com": "fnrz rkrp nrwy yaig",
            "qwaerlarp@gmail.com": "zrzx siyf ukvm ctjp",
            "segatel093@gmail.com": "fsma qetz gvmp pqrm",
            "irina15815123@gmail.com": "fmre mxne ncaw gnke",
            "disgeugh482@gmail.com": "ufet dwko fadg crax",
            "germanalexandrovich12345678@gmail.com": "tsln hvmz mipp kmwh",
            "bl89222099674@gmail.com": "yjru yftj zihu nyrz",
            "psega0892@gmail.com": "vhrr hiso npgm xnoi",
            "noakk1843@gmail.com": "mvqo rfrv cjht vppo",
            "mak091ov@gmail.com": "hhli muyx nqju wlkk",
            "tatanamorinskaa@gmail.com": "cjig kaxt tijl ndre",
            "ivanplutalov543@gmail.com": "xsvm ewki dhfz qqkh"

}
receivers = ['abuse@telegram.org']

banner = '''

    
      ██╗░░░██╗███████╗███╗░░██╗░█████╗░███╗░░░███╗       By Poison
      ██║░░░██║██╔════╝████╗░██║██╔══██╗████╗░████║
      ╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██╔████╔██║
      ░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║╚██╔╝██║
      ░░╚██╔╝░░███████╗██║░╚███║╚█████╔╝██║░╚═╝░██║
      ░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝                                                     

        Owner:@EFall | Channel: @soft1XIII 

[1] СНОС АККАУНТА         
[2] СНОС КАНАЛА
          
'''

color_code = {
    "reset": "\033[0m",  
    "underline": "\033[04m", 
    "green": "\033[32m",     
    "yellow": "\033[93m",    
    "red": "\033[31m",       
    "cyan": "\033[36m",     
    "bold": "\033[01m",        
    "pink": "\033[95m",
    "url_l": "\033[36m",       
    "li_g": "\033[92m",      
    "f_cl": "\033[0m",
    "dark": "\033[90m",     
}

alignment = "{:>50}".format(banner)
banner = Colorate.Horizontal(Colors.green_to_white, alignment)
print(banner)

def gradient_text(text):
    return Colorate.Horizontal(Colors.green_to_white, text, 2)

def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        if 'gmail.com' in sender_email:
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
        elif 'rambler.ru' in sender_email:
            smtp_server = 'smtp.rambler.ru'
            smtp_port = 587
        elif 'hotmail.com' in sender_email:
            smtp_server = 'smtp.office365.com'
            smtp_port = 587
        elif 'mail.ru' in sender_email:
            smtp_server = 'smtp.mail.ru'
            smtp_port = 587
        else:
            raise ValueError("Unsupported email provider")
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        server.quit()
        
        return True
    except Exception as e:
        return False

def main():
    sent_emails = 0
    choice = input(f'Выберте пункт ')

    if choice == '1':
        print(gradient_text("1. ЗА СПАМ, РЕКЛАМУ"))
        print(gradient_text("2. ЗА ДОКСИНГ"))
        print(gradient_text("3. ЗА ТРОЛЛИНГ"))
        print(gradient_text("4. ПРОДАЖУ/РЕКЛАМА НАРК0ТЫ"))
        print(gradient_text("5. КУРАТОР В НАРК0ШОПЕ"))
        print(gradient_text("6. ПРОДАЖА ЦП"))
        print(gradient_text("7. ВЫМОГАНИЕ ИНТИМНЫХ ФОТО У НЕСОВЕРШЕНОЛЕТТНИХ"))
        print(gradient_text("8. ОСКОРБЛЕНИЕ НАЦИИ"))
        print(gradient_text("9. ОСКОРБЛЕНИЕ РЕЛЕГИИ"))
        print(gradient_text("10. РАСПРОСТРОНЕНИЕ РАСЧЛЕНЕНКИ"))
        print(gradient_text("11. РАСПРОСТРОНЕНИЕ ЖИВОДЕРСТВО"))
        print(gradient_text("12. РАСПРОСТРЕНЕНИЕ ПОРНО"))
        print(gradient_text("13. УГРОЗЫ СНОСОМ СВАТОМ ДОКСОМ"))
        print(gradient_text("14. УГРОЗЫ РАСПРАВЫ"))
        print(gradient_text("15. СНОС СЕССИЙ"))
        print(gradient_text("16. СНОС ВИРТ НОМЕРА"))
        print(gradient_text("17. СНОС С ПРEМКОЙ"))
        comp_choice = input("Выберите нарушание ")

        if comp_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14" ]:
            print("Следуйте указанием")
            username = input("Юзернейм ")
            id = input("Телеграм айди ")
            chat_link = input("Ссылка на чат: ")
            violation_link = input("Ссылка на нарушение в чате: ")
            cprint("Ожидайте" , "red")
            comp_texts = {
    "1": f"Dear Support Team, I urgently bring to your attention a user on your platform who is consistently sending an overwhelming amount of irrelevant messages, which is clearly spam. Their username is {username}, ID is {id}, chat link: {chat_link}, violation link: {violation_link}. I kindly request immediate action to block or restrict this user from further disrupting the platform.",
    "2": f"Dear Support Team, I have encountered a user on your platform who is blatantly sharing private, sensitive information of others without consent. This is a serious violation of privacy. Their username is {username}, ID is {id}, chat link: {chat_link}, violation link: {violation_link}. Please take swift and decisive action to block their account and prevent further harm.",
    "3": f"Dear Telegram Support, I have found a user on your platform who is openly using offensive language and spamming multiple chats with inappropriate content. Their username is {username}, ID is {id}, chat link: {chat_link}, violation link: {violation_link}. I urge you to take prompt action to block this account and prevent further damage to the community.",
    "4": f"Dear Telegram Support, I have come across a user who is actively engaged in the sale and promotion of illegal substances. This behavior is both dangerous and unlawful. Their username is {username}, ID is {id}, chat link: {chat_link}, violation link: {violation_link}. I strongly request that you immediately block this user’s account to safeguard the platform.",
    "5": f"Dear Telegram Support, I have identified a user attempting to recruit individuals into illegal drug activities. Their username is {username}, ID is {id}, chat link: {chat_link}, violation link: {violation_link}. This is an extremely serious issue, and I implore you to take swift action to block this user and protect the safety of the community.",
    "6": f"Dear Telegram Support, I have discovered a user distributing explicit materials involving minors. This is a grave violation of both legal and ethical standards. Their username is {username}, ID is {id}, chat link: {chat_link}, violation link: {violation_link}. Please take immediate action to block this account and prevent further exploitation.",
    "7": f"Dear Telegram Support, I have found a user attempting to extort explicit photos from minors, which is an incredibly alarming and illegal act. Their username is {username}, ID is {id}, chat link: {chat_link}, violation link: {violation_link}. I urgently request that you take immediate action to block this account and protect vulnerable individuals.",
    "8": f"Dear Telegram Support, I have come across a user who is inciting racial hatred and fueling division within the community. This behavior is completely unacceptable and harmful. Their username is {username}, ID is {id}, chat link: {chat_link}, violation link: {violation_link}. Please take immediate action to block this user and preserve the integrity of the platform.",
    "9": f"Dear Telegram Support, I have found a user spreading hate and intolerance against religious groups, creating division and conflict. This is a serious violation of the platform's values. Their username is {username}, ID is {id}, chat link: {chat_link}, violation link: {violation_link}. I strongly urge you to take prompt action and block this account immediately.",
    "10": f"Dear Telegram Support, I have identified a user sharing extremely disturbing content, including videos and images of human killings. This is a deeply traumatic and illegal activity. Their username is {username}, ID is {id}, chat link: {chat_link}, violation link: {violation_link}. I implore you to take urgent action to block this user’s account and prevent further harm to the community.",
    "11": f"Dear Telegram Support, I have found a user sharing shocking content, including images and videos of animal cruelty. This is an abhorrent violation of both ethical standards and platform policies. Their username is {username}, ID is {id}, chat link: {chat_link}, violation link: {violation_link}. I strongly request immediate action to block this account and prevent further abuse.",
    "12": f"Dear Telegram Support, I have come across a user distributing explicit pornographic materials. This is a direct violation of your platform’s rules and ethical standards. Their username is {username}, ID is {id}, chat link: {chat_link}, violation link: {violation_link}. Please take swift and decisive action to block this user and prevent further dissemination of harmful content.",
    "13": f"Dear Telegram Support, I have encountered a user making direct threats to expose personal information of others. This is an illegal and highly dangerous act. Their username is {username}, ID is {id}, chat link: {chat_link}, violation link: {violation_link}. I urge you to take immediate action and block this user’s account to prevent any further threats.",
    "14": f"Dear Telegram Support, I have found a user making serious threats of violence and harm towards others. This is a severe violation of platform policies and a direct danger to the safety of others. Their username is {username}, ID is {id}, chat link: {chat_link}, violation link: {violation_link}. I urgently request that you block this account and take immediate action to protect the community."
}
            
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                                                 violation_link=violation_link.strip())
                    send_email(receiver, sender_email, sender_password, 'URGENTLY READ IT URGENTLY', comp_body)
                    cprint(f"Отправлено на {receiver} от {sender_email}", "green")
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice in ["15"]:
            print("Следуйте указанием")
            username = input("Юзернейм нарушителя ")
            id = input("Телеграм айди: ")
            cprint("ОЖИДАЙТЕ" , "red")
            comp_texts = {
    "15": f"Dear Telegram Support, I am urgently reaching out regarding a serious issue. I inadvertently clicked on a phishing link, which has compromised my account. As a result, I have lost access to my account, and I am deeply concerned about the security of my personal information. My username is {username}, and my ID is {id}. I request that you immediately take action to either delete my account or reset all active sessions to ensure no further unauthorized access occurs. This is a critical matter, and I appreciate your prompt attention to resolving it."
}

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'I lost my account. HELP', comp_body)
                    cprint(f"Отправлено на {receiver} от {sender_email}", "green")
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice in ["16", "17"]:
            print("Следуйте указанием")
            username = input("Юзернейм нарушителя ")
            id = input("Телеграм айди: ")
            cprint("" , "red")
            comp_texts = {
    "16": f"Dear Telegram Support, I would like to bring to your attention a serious issue with the account {username}, ID {id}. This user is utilizing a virtual number that was purchased through a number activation service. The number is not associated with this user in any legitimate way and is being used to bypass the system. I kindly request that you investigate this matter and take appropriate action. Thank you in advance for your attention to this issue.",
    "17": f"Dear Telegram Support, I am reporting an account, {username}, ID {id}, that has purchased a premium subscription in order to send spam messages and bypass the platform’s restrictions. This is a clear violation of Telegram’s policies. I urge you to investigate this complaint thoroughly and take immediate action to prevent further misuse of the service. Your prompt attention to this matter would be greatly appreciated."
}

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'URGENTLY READ IT URGENTLY', comp_body)
                    cprint(f"Отправлено на {receiver} от {sender_email}", "green")
                    sent_emails += 1000
                    time.sleep(5)


    elif choice == "2":
        
        print(gradient_text("1. С ЛИЧНИМИ ДАННЫМИ"))
        print(gradient_text("2. С ЖИВОДЕРСТВО "))
        print(gradient_text("3. С ДЕСТКИМ ПОРНО"))
        print(gradient_text("4. С ПРАЙСОМ"))
        print(gradient_text("5. С РАСЧЛЕНЕНКОЙ"))
        print(gradient_text("6. КАЗИНО"))
        print(gradient_text("7. НАРКО-ШОП"))
        print(gradient_text("8. ОСКОРБЛЕНИЕ НАЦИИ"))
        print(gradient_text("9. ОСКОРБЛЕНИЕ РЕЛЕГИИ"))
        print(gradient_text("10. С ПОРНО"))
        ch_choice = input("Выбирай ")

        if ch_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            channel_link = input("Ссылка на канал (НЕ ЗАКРЫТЫЙ КАНАЛ) ")
            channel_violation = input("Ссылка на нарушение в канале ")
            cprint("Ожидайте" , "red")
            comp_texts = {
    "1": f"Dear Telegram Support, I have encountered a channel on your platform that is blatantly violating privacy laws by distributing personal, sensitive information of innocent individuals without consent. This is not only an ethical violation but a serious legal matter under U.S. privacy laws (e.g., GDPR, CCPA). Channel link: {channel_link}, violation link: {channel_violation}. I urgently request that you take immediate action and permanently block this channel to prevent further harm and legal consequences.",
    "2": f"Dear Telegram Support, I have discovered a channel that is promoting and sharing disturbing content of animal abuse, which is illegal under U.S. federal law, including the Animal Welfare Act. This is an unlawful and morally reprehensible act that cannot be tolerated. Channel link: {channel_link}, violation link: {channel_violation}. I strongly urge you to take immediate and decisive action to block this channel and prevent any further illegal content from being distributed on your platform.",
    "3": f"Dear Telegram Support, I have found a channel that is distributing child pornography, which is a severe violation of both U.S. federal law (e.g., the Child Protection and Obscenity Enforcement Act) and international law. This content is not only illegal but deeply harmful to society. Channel link: {channel_link}, violation link: {channel_violation}. I request immediate and thorough action to block this channel and ensure such content is removed from your platform permanently.",
    "4": f"Dear Telegram Support, I am reporting a channel that is facilitating illegal activities by selling doxxing and swatting services, which are criminal offenses under U.S. law (e.g., the Computer Fraud and Abuse Act). These actions are not only unethical but also criminal. Channel link: {channel_link}, violation link: {channel_violation}. I urge you to take immediate and firm action to block this channel and prevent these illegal services from being promoted on your platform.",
    "5": f"Dear Telegram Support, I have discovered a channel that is sharing extremely graphic and disturbing footage of human killings, which is illegal under U.S. federal law (e.g., the Violent Crime Control and Law Enforcement Act). This is an extremely serious violation of the law, and it poses a threat to the safety and well-being of all users. Channel link: {channel_link}, violation link: {channel_violation}. I request that you take urgent action to block this channel and prevent the circulation of such content immediately.",
    "6": f"Dear Telegram Support, I have identified a channel that is promoting gambling activities, including online casinos, which are illegal under U.S. federal law (e.g., the Unlawful Internet Gambling Enforcement Act). Such activities are illegal and cannot be tolerated on your platform. Channel link: {channel_link}, violation link: {channel_violation}. I implore you to take immediate action to block this channel and prevent any further illegal activities.",
    "7": f"Dear Telegram Support, I have found a channel that is actively promoting the sale of narcotic substances, which is strictly prohibited under U.S. federal law (e.g., the Controlled Substances Act). This is not only a serious violation of your policies but also a criminal act that endangers public safety. Channel link: {channel_link}, violation link: {channel_violation}. I strongly urge you to take swift and decisive action to block this channel and prevent the spread of illegal substances.",
    "8": f"Dear Telegram Support, I have encountered a channel that is promoting hate speech and inciting violence against a particular nation, which violates U.S. federal law (e.g., the Hate Crimes Prevention Act). This content is harmful and divisive. Channel link: {channel_link}, violation link: {channel_violation}. I urgently request that you take immediate action to block this channel and ensure that such content is removed from your platform permanently.",
    "9": f"Dear Telegram Support, I have found a channel that is inciting religious intolerance and oppression, which is illegal under U.S. law (e.g., the Civil Rights Act). This kind of harmful content cannot be allowed to spread on your platform. Channel link: {channel_link}, violation link: {channel_violation}. I kindly request that you take immediate and firm action to block this channel and prevent any further incitement to religious violence.",
    "10": f"Dear Telegram Support, I have discovered a channel that is distributing pornographic materials, which is a clear violation of U.S. federal law (e.g., the Child Protection and Obscenity Enforcement Act). This content is illegal and harmful, and I urge you to take action immediately. Channel link: {channel_link}, violation link: {channel_violation}. I strongly urge you to block this channel and prevent any further dissemination of illegal and inappropriate content."
}
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
                    cprint(f"Отправлено на {receiver} от {sender_email}", "green")
                    sent_emails += 1000
                    time.sleep(5)   
  
if __name__ == "__main__":
    main()