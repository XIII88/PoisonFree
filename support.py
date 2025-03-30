from pystyle import Write, Colors
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import os
import time
from datetime import datetime
import logging
import requests

logging.basicConfig(filename='email_errors.log', level=logging.ERROR, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

recipients = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',  'sticker@telegram.org', 'support@telegram.org', 'support@telegram.org', 'dmca@telegram.org', 'security@telegram.org', 'sms@telegram.org', 'info@telegram.org', 'marta@telegram.org', 'spam@telegram.org', 'alex@telegram.org', 'abuse@telegram.org', 'pavel@telegram.org', 'durov@telegram.org', 'elies@telegram.org', 'ceo@telegram.org', 'mr@telegram.org', 'levlam@telegram.org', 'perekopsky@telegram.org', 'recover@telegram.org', 'germany@telegram.org', 'hyman@telegram.org', 'qa@telegram.org', 'Stickers@telegram.org', 'ir@telegram.org', 'vadim@telegram.org', 'shyam@telegram.org', 'stopca@telegram.org', '>support@telegram.org', 'ask@telegram.org', '125support@telegram.org', 'me@telegram.org', 'enquiries@telegram.org', 'api_support@telegram.org', 'marketing@telegram.org', 'ca@telegram.org', 'recovery@telegram.org', 'http@telegram.org', 'corp@telegram.org', 'corona@telegram.org', 'ton@telegram.org', 'sticker@telegram.org']

senders = {
    "huyznaet06@gmail.com": "cyeb pnyi ctpj xxdx",
    "alabuga793@gmail.com": "tzuk rehw syaw ozme",
    "editt1345@gmail.com": "hezf xuel hzvz jzur",
    "dlatt7055@gmail.com": "tpzd nxle odaw uqwf",
    "dlyabravla655@gmail.com": "kprn ihvr bgia vdys",
    "dlatt6677@gmail.com": "usun ruef otzx zcrh",
    "edittendo0@gmail.com": "mzdl lrmx puyq epur",
    "shshsbsbsbwbwvw@gmail.com": "jqrx qivo qxjy jejt",
    "IvanKarma2000@gmail.com": "irlr cggo xksq tlbb",
    "misha28272727@gmail.com": "kgwqxvkgjyccibkm",
    "vladimiradmiralov664@gmail.com": "papq hkip geao rkuz", 
    "qstkennethadams388@gmail.com": "itpz jkrh mtwp escx",
    "usppaullewis171@gmail.com": "lpiy xqwi apmc xzmv",
    "ftkgeorgeanderson367@gmail.com": "okut ecjk hstl nucy",
    "nieedwardbrown533@gmail.com": "wvig utku ovjk appd",
    "h56400139@gmail.com": "byrl egno xguy ksvf",
    "den.kotelnikov220@gmail.com": "xprw tftm lldy ranp",
    "trevorzxasuniga214@gmail.com": "egnr eucw jvxg jatq",
    "dellapreston50@gmail.com": "qoit huon rzsd eewo",
    "neilfdhioley765@gmail.com": "rgco uwiy qrdc gvqh",
    "hhzcharlesbaker201@gmail.com": "mcxq vzgm quxy smhh",
    "samuelmnjassey32@gmail.com": "lgct cjiw nufr zxjg",
    "allisonikse1922@gmail.com": "tozo xrzu qndn mwuq",
    "corysnja1996@gmail.com": "pfjk ocbf augx cgiy",
    "maddietrdk1999@gmail.com": "rhqb ssiz csar cvot",
    "edwardmason@mail.ru": "4oTj43mFWD",
    "wilsonwhitney@gmail.com": "OgZ6*&ASSatqgh5Q",
     "nwest@yahoo.com": "EU7%U@Sdj4c@PlLu",
     "zina.podshivalova.92@mail.ru": "u4CL3YxVutmiuTvmTrbu",
"leha.novitskiy.71@mail.ru": "qQZd1gMqkU906Xk2hgJJ",
"rimma.aleksandrovicha.72@mail.ru": "biL4m6h0h4xQrDB3PnPp",
"polina.karaseva.1987@mail.ru": "mxZUqPPTrZHK99jUfPhB",
"prokhor.sablin.82@mail.ru": "vN7FjmmCmAD0JnQsANyc",
"kade.kostya@mail.ru": "U0hdXu7y3c1AVeT1Vpn9",
"yelizaveta.novokshonova.71@mail.ru": "aKPpgaPDuwaKbX1pbcq3",
"pozdovp@mail.ru": "EGDd20c7s82Z0s9LmrXc",
"siyasinovy@mail.ru": "z2ZdsRL04JvBYZrrjrvv",
"nina.gref.73@mail.ru": "sitw1XTxCVgji061iqj7",
"fil.golubkin.80@mail.ru": "PeaLrzjbn408DEeiqmQq",
"venedikt.babinov.71@mail.ru": "tBewA1HQm29c2Zkira96",
"den.verderevskiy.67@mail.ru": "fndp7qr67dpfXBAu0ePH",
"olga.viranovskaya.92@mail.ru": "50QSPrecgk5cMdk1YsBm", 
"zina.podshivalova.92@mail.ru": "u4CL3YxVutmiuTvmTrbu",
"leha.novitskiy.71@mail.ru": "qQZd1gMqkU906Xk2hgJJ",
"rimma.aleksandrovicha.72@mail.ru": "biL4m6h0h4xQrDB3PnPp",
"polina.karaseva.1987@mail.ru": "mxZUqPPTrZHK99jUfPhB",
"prokhor.sablin.82@mail.ru": "vN7FjmmCmAD0JnQsANyc",
"kade.kostya@mail.ru": "U0hdXu7y3c1AVeT1Vpn9",
"yelizaveta.novokshonova.71@mail.ru": "aKPpgaPDuwaKbX1pbcq3",
"pozdovp@mail.ru": "EGDd20c7s82Z0s9LmrXc",
"siyasinovy@mail.ru": "z2ZdsRL04JvBYZrrjrvv",
"nina.gref.73@mail.ru": "sitw1XTxCVgji061iqj7",
"fil.golubkin.80@mail.ru": "PeaLrzjbn408DEeiqmQq",
"venedikt.babinov.71@mail.ru": "tBewA1HQm29c2Zkira96",
"den.verderevskiy.67@mail.ru": "fndp7qr67dpfXBAu0ePH",
"olga.viranovskaya.92@mail.ru": "50QSPrecgk5cMdk1YsBm",
"sylvain.cavart@airgeneva.org": "cafous",
"tineke.kollenaar@tele2.nl": "albertina1960",
"diego1313@orange.fr": "diego1313",
"mouler@t-online.de": "Bifteki8",
"thiele.jeni94@t-online.de": "WISZ1LB6",
"original@vp.pl": "kingai06",
"pompiceklukasek@email.cz": "satisfakce",
"emmabochhoff@web.de": "ahwwik2310",
"meier.joan@web.de": "Kleve1991",
"piyushumathe2007@rediffmail.com": "sharpraz0r",
"kisa472204@eyou.com": "Kisa472204",
"elisa@studioverde.it": "Studio2016",
"a.rougecarrassat@wanadoo.fr": "alexis",
"subintensiva.alatri@aslfrosinone.it": "subintensiva",
"tim.91@orange.fr": "carcasse91",
"home@oktay-atas.de": "ciyrikli",
"nothingb@seznam.cz": "niceho",
"heinrich.buss1@ewetel.net": "nadja1",
"order@devilskiss.net": "sickness",
"365shop@tele2.nl": "Kayalar61!",
"tetard007@orange.fr": "Code55680%",
"jolad345@gazeta.pl": "pingus1",
"spuk@vwi-magdeburg.de": "spuk1234",
"trasparenza@fattoriadellapiana.it": "fattoria900",
"flex439@web.de": "killa936",
"masalamlyne@wanadoo.fr": "pascal1",
"patryk.radulski@web.de": "rasiak156",
"titeamande@wanadoo.fr": "Alright1",
"alexandra@graciebears.com": "Ve1sheda",
"benkoemakat@rediffmail.com": "739749",
"sylvain-pellieux@wanadoo.fr": "nathoo",
"sonne0007@gmx.de": "Fynn2010",
}

smtp_servers = {
    "gmail.com": ("smtp.gmail.com", 587),
    "yandex.ru": ("smtp.yandex.ru", 465),
    "mail.ru": ("smtp.mail.ru", 465),
    "rambler.ru": ("smtp.rambler.ru", 465),
    "yahoo.com": ("smtp.mail.yahoo.com", 465),
    "outlook.com": ("smtp.office365.com", 587),
    "icloud.com": ("smtp.mail.me.com", 587),
    "aol.com": ("smtp.aol.com", 587),
    "zoho.com": ("smtp.zoho.com", 587),
    "protonmail.com": ("smtp.protonmail.com", 587),
    "t-online.de": ("secure.emailsrvr.com", 587),
    "gmx.de": ("mail.gmx.com", 587),
    "hotmail.de": ("smtp.live.com", 587),
    "web.de": ("smtp.web.de", 587),
    "gmx.net": ("mail.gmx.net", 587),
    "posteo.de": ("posteo.de", 587),
    "mailbox.org": ("smtp.mailbox.org", 587),
    "1und1.de": ("smtp.1und1.de", 587),
    "strato.de": ("smtp.strato.de", 465)
}

phones = [    "+79456789012",
    "+79567890123",
    "+79899899880",
    "+79921219497",
    "+79142713399",
    "+79841183364",
    "+79052638740",
    "+79782795033",
    "+380950754198",
    "+79891247275",
    "+79021240848",
    "+79000529517",
    "+380950726459",
    "+79043665039",
    "+79966287301",
    "+380969916088",
    "+79616459702",
    "+79002940036",
    "+79193704818",
    "+79000586068",
    "+79000586069",
    "+79193704818",
    "+79256440540",
    "+77475568493",
    "+380981272681",
    "+79824054695",
    "+79224693139",
    "+79824054695",
    "+79129102228",
    "+79287288244",
    "+79315774082",
    "+380981272681",
    "+79000243902",
    "+79511037113",
    "+79931336089",
    "+77071211538",
    "+79509820128",
    "+79961334370",
    "+79608680310",
    "+79872753935",
    "+79999097359",
    "+79372460746",
    "+79227963514",
    "+79170163123",
    "+79147722064",
    "+79085534084",
    "+79047384037",
    "+79049692438",
    "+79028652699",
    "+79967322520",
    "+79644441515",
    "+79775983461",
    "+79534863408",
    "+79003281691",
    "+74957888878",
    "+78432262150",
    "+79509695754",
    "+79047640249",
    "+79505776241",
    "+380995102459",
    "+79773864851",
    "+79224585935",
    "+79174432402",
    "+73478322051"]

site_emails = [
     "leonidkadnicanskij36@gmail.com",
    "leonidkadnihcyansky@gmail.com",
    "fidana20090919@gmail.com",
    "tcabin7@gmail.com",
    "timacabin43@gmail.com",
    "bekovadali7292@gmail.com",
    "yasminbekova01@gmail.com",
    "artemsonkak@gmail.com",
    "hazovgenis@gmail.com",
    "khazov14.d@gmail.com",
    "aspectsstyle@gmail.com",
    "ropvims@gmail.com",
    "artskripan042@gmail.com",
    "irensib042@gmail.com",
    "wmempresarial.br@gmail.com",
    "tat.abramova@gmail.com",
    "keikeyo@gmail.com",
    "ivashkin.stanislav@gmail.com",
    "aqasifallahverdiyev@gmail.com",
    "shilovskii99@mail.ru",
    "olgacauk@gmail.com",
    "pomaca73@gmail.com",
    "tatiana.gulyaeva88@gmail.com",
    "zmievskymail@gmail.com",
    "tololbbk1@gmail.com" ,
    "sofya.trubnikova00@mail.ru",
    "Trubnikova1979@mail.ru",
    "irinakhramova1987@mail.ru",
    "do.petrova82@mail.ru",
    "SEVERKLEVER@MAIL.RU",
    "postolatiy_sergey@mail.ru",
    "irinatovna@mail.ru",
    "skripam@mail.ru",
    "cheshko-polina@mail.ru",
    "find_sophie@mail.ru",
    "sos_sos29@mail.ru",
    "artur2802@mail.ru",
    "fyrz@mail.ru",
    "monolit-director@mail.ru",
    "shilovskii99@mail.ru",
    "alex_vl@mail.ru"
]


user_agents = ['Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.7228.0 Mobile Safari/537.36',  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/90.0.0.0 Safari/605.1.15',  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.6291.0 Safari/537.36',  'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.1257.0 Mobile Safari/537.36',  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/79.0.0.0 Safari/605.1.15',  'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.5234.0 Mobile Safari/537.36',  'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/79.0 Mobile/15E148 Safari/604.1',  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.3170.0 Safari/537.36',  'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/66',  'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/73.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.7979.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/108.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/38.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.5070.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.7640.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/49.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4688.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/90.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3182.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.9176.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/71', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/73.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.6900.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/59.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.6232.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/45.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6601.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/105.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.7252.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/32.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.3745.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.8312.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/74', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.7859.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/62.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/83.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/107.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/87.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/98.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/89.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/99.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/39.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/68.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.1093.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/95', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/31.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.1717.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.1639.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/84.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/82', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.6195.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.3017.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3335.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.4466.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.4905.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/70.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.5389.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/106.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.3074.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/89', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/33.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/102.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.1499.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.8932.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/82.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/44', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.6515.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3933.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/86.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/36.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/40.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.3634.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.3570.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.4896.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/49.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/98.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.1496.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/107.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.9879.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.4786.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3647.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/44.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/37', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.9729.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2112.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.9285.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/76.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/73.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/46.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/60', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/90.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/90.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.9414.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/76.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.1507.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/56.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/50.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.5340.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/40.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.4635.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.2267.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.5340.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/75.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.6461.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.7362.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/93.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/55.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/66.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/100', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/101.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/71', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.7889.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.7788.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2949.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4965.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/110.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/101', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.4721.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.4612.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/32.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/92.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/52.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.2576.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.7392.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.4318.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1560.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/46', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2164.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/33', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/67.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/48.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/71.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/45.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.2636.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.2814.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/50', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/78.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/64.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.7833.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/44.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.2117.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/65.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/101', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/71.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/55.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.3465.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/31.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/54.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/94', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.5422.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/40', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/45.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/99.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/33.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/58', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.4983.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/45', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.6868.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4830.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/41.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.1986.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.9720.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/107', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/89.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.9772.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/91.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/42', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/104.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.3028.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.2463.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.1771.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/43', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3376.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/90.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/82.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/70.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/40.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/106.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.8977.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/83.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.2539.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/79.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/109.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/43.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.5074.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1922.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/62', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.7278.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.8083.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.5860.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/97', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/69.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/87.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/74.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.3812.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/49', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.1806.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/64', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.3967.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/58', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/103', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/58', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.8301.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.6675.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/104.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/37.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/41', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/84', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/53.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/87.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/50', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/73', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.2367.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.8872.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/71.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.5491.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/88.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/75.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.9417.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/69', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/73', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/104.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/75.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.8185.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/41', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/40.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/71.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.8457.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/62.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/94', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.7731.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.9276.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.9877.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/71', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/96.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/84', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/53.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.7101.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/82', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/58.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.7699.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/101.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.9741.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.2076.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/94.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/107', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.2734.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.7498.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/48.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/39.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.1934.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/56', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/95.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/68', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/66.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.3051.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/108.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/69.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.7492.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/68.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.5390.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/96', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.7305.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.8231.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.1640.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/57.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/82', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/68.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.6458.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/59.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/109', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.4143.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/43.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/37.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/31', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.8486.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/75.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.5546.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/100', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/85.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/62.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/71.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.9586.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.6001.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/106.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.2674.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/110', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.1572.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.1092.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.6848.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.1745.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.5962.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.6689.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/87.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/45', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.1236.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/107', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.1363.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.6092.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/71.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.1338.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/101.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/104.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/49.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/55.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.7705.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.5004.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.6638.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.9097.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/82.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/51.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/89', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.1172.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.6564.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/85', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/94', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/37', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/85', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/66.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/82', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/51.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.2898.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/86', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.8809.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.8068.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/102', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/49', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/93.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/33', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/107', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/98', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/31.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/37.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/89.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3986.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.1647.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.1464.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/34.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/39.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/88.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.2734.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/33.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4813.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/100.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.6150.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/66.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.7085.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.9402.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.6927.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/81.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.8547.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/77.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/68.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/75.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.9348.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/108', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/97', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.6498.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/67', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/42.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/69.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/85.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.8685.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.1607.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/71.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.4086.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.7086.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4371.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/86.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/34.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/74.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/69.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/74.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/81', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/72', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/77.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/47.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/74.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.4157.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.3913.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/82.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.1758.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/32', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.5228.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.1290.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/41.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/110.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.9713.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/45', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/47.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/45.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/94', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/59.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/80.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.7719.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.7689.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.9428.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/60.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/77', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/53.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/71', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.7989.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/34', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/58.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/86.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/53.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/89.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/76.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/54.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/84.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.8945.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.8717.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/51', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/91.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.5383.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.8860.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/35.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/60.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/90', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/80.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.3950.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/110.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.8942.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/33', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/62.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.4911.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.1394.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/43.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/52.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/100', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/37', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/70.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/44.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/93', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/34.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/98.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/63', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/94', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1270.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/99.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/38.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/74.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.8435.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/39.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.7307.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.2227.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4721.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/40.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/64.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/81', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/64.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/95', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/85.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/53.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/107.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/109.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/37', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/66', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.3463.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/53', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.9032.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/45', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.1294.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1320.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4067.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/33.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/103.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/101.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/65.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/76.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.1748.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.6817.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/77.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/84.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/52', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/57', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/86.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.6256.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/96.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/70.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/43.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.5944.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/41.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/50.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/88.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.9324.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/41.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.1338.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2256.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/46', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/75.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/99.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/44', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/32.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/107.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/38.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/52', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.1419.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.5427.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.8058.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/59.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/64.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/103.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/80.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.2402.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.8880.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/89.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/48.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/109', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/93.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.2811.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.5898.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.4123.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.9317.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/67', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/109', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.6530.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3008.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/93.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/88', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.6611.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.8134.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/41', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.9058.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/86', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.4663.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4988.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.5523.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.4574.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.9360.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/95.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/34.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/96', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/98.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.6775.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.9855.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/52.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/49.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.9919.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/38.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.6616.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/48.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.2729.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/53', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/34.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3359.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/104.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/87.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/39.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.3300.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.3357.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.6330.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.5208.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.1730.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.3238.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/79.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.3746.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/40.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2286.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/77.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/51', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/50', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/63', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/109', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.7770.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1543.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/36.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/92', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5595.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.5688.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.2962.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/95.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/54.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.2878.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/76.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/101', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3328.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.7012.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/63.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/51.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/97', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/52.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/88.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4758.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/77.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.8308.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2087.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/36.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/97', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/108', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.8143.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.5089.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/90', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/93.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.1679.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/84.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.7231.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/70.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.1659.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/109.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/30.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/64.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/103.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/55.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/56.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/98', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/108.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/100.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.6730.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/55.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.5084.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.5347.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.4006.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4953.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/102.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/98.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.6358.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4811.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/84.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3156.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.6827.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/103.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.7230.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.7284.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.2865.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/37.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.7656.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.9562.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.4151.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.2689.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/110.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/32.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.8146.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/85', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/33.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/58', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/102.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.3322.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.5851.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/54.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/53', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.7551.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/47.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.1389.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/62', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3007.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/77.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/84', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.6042.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.9395.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.8539.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.1121.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.9607.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.8871.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/108', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/88.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.8923.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/47', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/98.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.5651.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/36.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.8702.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2095.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/63', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.6968.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3959.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.1171.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/81.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.2429.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.3607.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/34.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/107.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.4352.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.7412.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.2107.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.6032.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.6592.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.2572.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/100.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/62.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.7784.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.8006.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/72.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1293.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/43.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/44.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/101.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/95.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/50.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.2019.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.1204.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/92.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.1628.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.5890.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/63.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/59', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.4040.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/71.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/84.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/53.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/58', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.8210.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/47.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.3804.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.6440.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/87', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.8662.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.8072.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.3155.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.9716.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/95.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/41', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.7369.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.7646.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.3722.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/56.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/70.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/46.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/43', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.8645.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.7748.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/68.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/32.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/74', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/96', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/31.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/65.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/48.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/66', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/58', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.2285.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/77', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.3454.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.3935.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/51.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/81.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.9143.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/41', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/80.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.7239.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/39', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.6903.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/82', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.1578.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/71.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.4386.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.2044.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.7612.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4014.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.6967.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.8254.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/78.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/84.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/56.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.7206.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/90', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.2240.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.5544.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/44.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/106.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.5596.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/51.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/47.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/94.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/63', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.4980.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/31.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4016.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/62.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/51.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/96', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.2123.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/93.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.7998.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.1118.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.9491.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/34.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/33', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1088.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/92', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.9752.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.6595.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/109.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.7934.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/92.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/56.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.5225.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/67', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/73.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/88.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.7967.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/94.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.5960.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/45.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.4327.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3656.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/34.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/84.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/56', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/63', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.2213.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/45.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.2774.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.6697.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5937.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.4100.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/71.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.6001.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/107.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.4204.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/54.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.7023.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.8630.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.8476.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.9601.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5405.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/101.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/51', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/41.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/60', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/64.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/44.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.3660.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.5582.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.5907.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5830.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/103.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.5041.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/40', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/77.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/51.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/83', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4649.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.9579.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/48', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/77', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.8803.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.1332.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/108.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.7619.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.9059.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4884.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/107.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/41.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/68.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.9829.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/109.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/63.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/37', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/85.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/62.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/62.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.4275.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/90.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.5796.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/85.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/59.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/89.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.9309.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/45.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.7516.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.7138.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4899.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3514.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.8104.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.2581.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/104.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/104.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/88.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/101', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.4448.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/101.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/102', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.2178.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2835.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/63.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/53', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/100.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4112.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.5618.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/77', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/58.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.1066.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.2823.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/54.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/99.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.8476.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/106', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/65.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.6161.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/99.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.4890.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.9531.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/49', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/71', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.8824.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/57.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/103', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/86', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.6351.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/104.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/66.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/70', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.1670.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/31.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.9903.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.5590.0 Safari/537.36', 
]
# тут я оставил список прокси в коде они не участвуют для отправки из-за того что большенство неработают поже я переберу и верну их для отправки 
proxies = [
    'http://202.218.201.72:17939',
 'http://18.122.40.50:2220',
 'http://244.77.108.100:9283',
 'http://12.184.66.154:18759',
 'http://226.146.191.65:14598',
 'http://120.117.224.158:49109',
 'http://38.232.195.108:11370',
 'http://136.255.10.172:58928',
 'http://58.34.253.156:32649',
 'http://82.78.193.43:24459',
 'http://88.187.206.252:40128',
 'http://171.240.20.45:59213',
 'http://253.246.195.66:52130',
 'http://35.133.191.116:30780',
 'http://96.79.77.250:12242',
 'http://107.70.49.1:27316',
 'http://205.176.71.30:49449',
 'http://140.199.5.193:51373',
 'http://178.218.189.136:57033',
 'http://233.6.142.179:47337',
 'http://128.105.196.245:23670',
 'http://215.197.243.15:43871',
 'http://128.222.34.86:54871',
 'http://81.101.89.21:43810',
 'http://16.247.191.12:61626',
 'http://196.175.29.229:16200',
 'http://112.254.10.177:23409',
 'http://168.25.66.28:33201',
 'http://104.204.225.110:38544',
 'http://151.107.115.161:64112',
 'http://248.65.186.23:40144',
 'http://130.234.213.169:41094',
 'http://189.128.16.14:36921',
 'http://171.56.248.100:32959',
 'http://109.176.234.152:11927',
 'http://128.198.34.137:28557',
 'http://22.149.49.226:43053',
 'http://25.232.116.253:53618',
 'http://135.218.58.140:62402',
 'http://252.120.80.100:61893',
 'http://28.118.61.193:28118',
 'http://149.12.84.27:47261',
 'http://122.61.167.92:51303',
 'http://18.251.247.250:43034',
 'http://253.68.108.44:14170',
 'http://179.165.203.70:8043',
 'http://251.145.112.81:13827',
 'http://19.169.119.254:15847',
 'http://147.93.75.125:18243',
 'http://201.101.24.19:37792',
 'http://40.47.70.155:18563',
 'http://184.245.61.176:9542',
 'http://244.33.42.102:53489',
 'http://217.230.164.31:38817',
 'http://238.114.208.55:30995',
 'http://126.81.96.169:28430',
 'http://145.164.107.241:13261',
 'http://219.228.66.24:13925',
 'http://191.138.3.116:10333',
 'http://226.81.184.145:48195',
 'http://66.99.38.197:6742',
 'http://207.129.227.182:44220',
 'http://131.75.62.131:54258',
 'http://104.251.102.5:6701',
 'http://219.63.80.246:52076',
 'http://138.123.43.92:31165',
 'http://208.123.127.1:34013',
 'http://28.121.232.77:28106',
 'http://14.149.112.25:55239',
 'http://120.25.44.219:61738',
 'http://84.137.82.199:14049',
 'http://243.195.203.127:40937',
 'http://168.120.44.31:56167',
 'http://46.19.140.7:4311',
 'http://102.226.33.18:47003',
 'http://89.170.187.35:35958',
 'http://138.14.102.97:26524',
 'http://151.93.192.123:35835',
 'http://120.160.215.137:16974',
 'http://117.23.171.37:64863',
 'http://206.111.102.243:14346',
 'http://193.51.17.69:9560',
 'http://168.251.173.208:44440',
 'http://89.178.159.123:20751',
 'http://219.251.52.28:46946',
 'http://59.33.78.248:11909',
 'http://246.89.100.138:60979',
 'http://173.166.154.18:35841',
 'http://162.171.192.58:16555',
 'http://187.88.245.135:19096',
 'http://177.138.44.233:57103',
 'http://58.44.253.252:24086',
 'http://13.130.234.59:35408',
 'http://145.8.151.212:17963',
 'http://8.137.19.145:60896',
 'http://8.216.13.64:49630',
 'http://112.108.155.253:42525',
 'http://25.25.111.79:39737',
 'http://196.163.250.162:62599',
 'http://36.62.40.99:63751',
 'http://252.11.21.100:38410',
 'http://18.3.223.183:12722',
 'http://142.155.75.52:60833',
 'http://200.222.69.176:56094',
 'http://192.118.176.113:26086',
 'http://64.166.192.238:38077',
 'http://35.49.28.208:26325',
 'http://218.160.36.7:47578',
 'http://91.232.25.9:26491',
 'http://55.193.35.108:12301',
 'http://161.15.169.31:51218',
 'http://221.161.21.98:2903',
 'http://7.179.123.251:14260',
 'http://48.160.76.65:50971',
 'http://132.93.236.35:55621',
 'http://180.120.69.184:3956',
 'http://218.222.95.9:5968',
 'http://70.50.214.98:52765',
 'http://84.95.210.242:36848',
 'http://40.129.229.201:10584',
 'http://246.41.183.51:33731',
 'http://233.31.34.144:36067',
 'http://243.124.200.115:23227',
 'http://169.26.153.231:57855',
 'http://1.162.19.187:34363',
 'http://62.31.35.236:54993',
 'http://232.47.174.88:46860',
 'http://240.114.75.90:59904',
 'http://208.132.179.198:62336',
 'http://160.215.64.238:29697',
 'http://191.18.77.58:46598',
 'http://197.127.66.60:36861',
 'http://74.59.92.71:53260',
 'http://250.112.67.87:19333',
 'http://138.102.4.104:53297',
 'http://140.150.94.118:48354',
 'http://244.3.53.34:7712',
 'http://57.173.134.194:6780',
 'http://254.110.159.27:28870',
 'http://3.153.169.7:23141',
 'http://160.121.58.226:61431',
 'http://19.213.178.245:31315',
 'http://33.147.125.126:27615',
 'http://132.175.121.207:1690',
 'http://170.64.194.170:26156',
 'http://136.230.40.20:34806',
 'http://212.96.220.201:10151',
 'http://51.8.167.87:26685',
 'http://255.15.48.234:18403',
 'http://66.189.48.3:30633',
 'http://64.97.69.214:3281',
 'http://194.51.60.192:58848',
 'http://56.40.211.105:49561',
 'http://48.254.227.41:38950',
 'http://254.26.148.252:43774',
 'http://1.124.71.124:60363',
 'http://14.22.146.19:26950',
 'http://35.98.186.51:35867',
 'http://195.188.100.19:40096',
 'http://203.235.43.198:3906',
 'http://252.230.254.228:21865',
 'http://243.87.222.21:3609',
 'http://168.7.184.6:48953',
 'http://100.122.185.241:48619',
 'http://3.18.198.99:63433',
 'http://46.236.240.235:33408',
 'http://132.103.166.227:41539',
 'http://226.210.12.175:41820',
 'http://135.255.14.129:36301',
 'http://85.206.157.146:53157',
 'http://141.37.12.154:56739',
 'http://231.170.52.138:24223',
 'http://55.156.93.95:23665',
 'http://146.64.149.175:37869',
 'http://77.0.90.42:49071',
 'http://68.119.47.228:10247',
 'http://156.27.231.126:34711',
 'http://70.248.4.66:11384',
 'http://51.0.60.165:37203',
 'http://165.52.223.31:19384',
 'http://135.251.151.108:40195',
 'http://217.88.30.119:49714',
 'http://66.105.12.190:23622',
 'http://7.119.109.6:15621',
 'http://173.196.222.21:46681',
 'http://53.191.198.219:62505',
 'http://76.126.32.138:38524',
 'http://105.31.166.77:61270',
 'http://57.97.94.8:17614',
 'http://185.205.147.192:17322',
 'http://252.124.8.155:34516',
 'http://216.172.229.76:65420',
 'http://196.81.208.4:13002',
 'http://84.196.30.194:64113',
 'http://108.233.15.254:61868',
 'http://143.221.10.65:62710',
 'http://106.186.68.29:13814',
 'http://30.113.251.47:37044',
 'http://116.235.47.130:6787',
 'http://116.250.121.231:15940',
 'http://60.93.0.237:35295',
 'http://247.151.225.35:17214',
 'http://10.207.48.140:35461',
 'http://42.190.251.90:17533',
 'http://77.66.191.166:25431',
 'http://50.20.36.116:30662',
 'http://199.53.47.18:23237',
 'http://45.131.79.185:3951',
 'http://54.133.54.73:63745',
 'http://247.67.8.160:8945',
 'http://239.221.62.243:31922',
 'http://154.43.84.233:53466',
 'http://71.142.78.22:60880',
 'http://194.108.205.196:44772',
 'http://253.39.153.196:10631',
 'http://173.209.171.13:57607',
 'http://107.240.108.141:50288',
 'http://107.231.78.23:25790',
 'http://254.20.58.129:41906',
 'http://97.155.12.138:25997',
 'http://45.91.133.218:19334',
 'http://52.177.187.223:4311',
 'http://155.178.178.163:36617',
 'http://20.138.59.122:17499',
 'http://34.92.188.37:53929',
 'http://194.127.14.221:59264',
 'http://106.176.113.104:21946',
 'http://203.18.158.83:55817',
 'http://107.219.235.237:38728',
 'http://72.252.9.241:8238',
 'http://241.158.225.125:21786',
 'http://25.190.98.109:52198',
 'http://210.117.174.128:56764',
 'http://233.33.36.67:55019',
 'http://172.135.167.146:6016',
 'http://139.98.110.9:48937',
 'http://225.195.141.46:51761',
 'http://203.246.127.24:11448',
 'http://196.108.35.106:29335',
 'http://191.9.115.189:15443',
 'http://189.153.26.103:48010',
 'http://97.215.65.37:11764',
 'http://175.66.121.146:8165',
 'http://49.130.89.225:35167',
 'http://126.199.184.86:60242',
 'http://216.223.209.188:2130',
 'http://61.98.117.85:24901',
 'http://41.40.77.36:3116',
 'http://250.123.121.105:47127',
 'http://203.55.5.148:27463',
 'http://206.149.69.30:30035',
 'http://107.239.170.135:12842',
 'http://237.240.15.176:65244',
 'http://72.199.124.105:52100',
 'http://135.69.17.51:16655',
 'http://132.54.80.115:53531',
 'http://4.252.94.154:53751',
 'http://123.240.65.55:9425',
 'http://188.135.90.41:58371',
 'http://60.152.96.243:34789',
 'http://87.153.58.42:64220',
 'http://78.213.126.31:10926',
 'http://253.166.29.165:34865',
 'http://194.157.239.103:50366',
 'http://83.76.114.214:37492',
 'http://135.80.8.125:22438',
 'http://27.35.110.57:8047',
 'http://202.39.83.203:12004',
 'http://174.35.34.170:33656',
 'http://140.39.131.155:50903',
 'http://69.237.53.78:63658',
 'http://163.52.95.16:55454',
 'http://86.19.143.103:42624',
 'http://147.0.69.235:21847',
 'http://161.124.198.109:40764',
 'http://37.213.146.48:3531',
 'http://132.131.174.55:48194',
 'http://100.83.28.104:53585',
 'http://193.129.83.114:7605',
 'http://112.43.252.24:13840',
 'http://201.66.225.115:11585',
 'http://225.213.233.14:30313',
 'http://220.150.22.33:55875',
 'http://88.129.185.184:19256',
 'http://110.133.232.110:24137',
 'http://8.183.99.125:37185',
 'http://245.96.116.72:19035',
 'http://104.4.245.184:51348',
 'http://227.213.188.33:60098',
 'http://144.80.203.34:57080',
 'http://133.70.124.103:3322',
 'http://223.27.44.39:32561',
 'http://195.159.156.154:41809',
 'http://35.253.113.28:53769',
 'http://172.134.136.90:38435',
 'http://33.190.125.153:30351',
 'http://164.52.8.61:44288',
 'http://120.131.41.24:59126',
 'http://212.86.79.200:23316',
 'http://154.199.38.70:3874',
 'http://255.207.193.209:48457',
 'http://202.59.90.131:46065',
 'http://27.231.167.195:46293',
 'http://116.237.220.148:52599',
 'http://19.52.220.135:46822',
 'http://227.151.109.142:53255',
 'http://169.120.19.123:3606',
 'http://111.147.130.29:45798',
 'http://18.208.40.100:38342',
 'http://101.200.238.18:1749',
 'http://105.104.249.44:19227',
 'http://63.194.112.182:42607',
 'http://221.111.196.187:34802',
 'http://147.186.180.158:17406',
 'http://159.193.0.101:34057',
 'http://151.93.217.235:43823',
 'http://111.28.115.197:36229',
 'http://175.141.78.146:57432',
 'http://131.74.251.41:2177',
 'http://184.193.81.147:8670',
 'http://251.19.30.148:33191',
 'http://206.12.95.45:12482',
 'http://82.115.254.198:11700',
 'http://146.181.67.150:42303',
 'http://171.240.198.253:19517',
 'http://7.24.180.21:52173',
 'http://12.85.66.206:43089',
 'http://64.105.171.85:31748',
 'http://53.237.24.71:39350',
 'http://220.102.204.226:25800',
 'http://243.27.235.195:35547',
 'http://129.82.97.230:49203',
 'http://133.6.79.219:12760',
 'http://135.52.151.87:54286',
 'http://119.8.232.12:10338',
 'http://50.148.81.85:8153',
 'http://95.65.218.18:31431',
 'http://180.71.163.20:10474',
 'http://39.216.119.29:50324',
 'http://141.137.110.96:30088',
 'http://9.62.151.241:59701',
 'http://68.73.191.4:18243',
 'http://33.65.17.10:5307',
 'http://238.146.183.182:35180',
 'http://48.105.34.211:47471',
 'http://30.159.209.56:6495',
 'http://61.162.93.61:41465',
 'http://145.24.174.255:23744',
 'http://35.75.141.82:15576',
 'http://36.28.206.236:29053',
 'http://124.107.47.45:28898',
 'http://129.109.144.157:17578',
 'http://55.24.58.83:50188',
 'http://63.44.0.163:27384',
 'http://66.156.164.141:19813',
 'http://236.95.42.176:37741',
 'http://250.69.66.222:16537',
 'http://12.223.114.135:53851',
 'http://9.151.114.178:44528',
 'http://128.235.249.249:29788',
 'http://209.195.154.62:28006',
 'http://122.38.252.133:42970',
 'http://88.54.203.88:24062',
 'http://223.36.236.152:53338',
 'http://43.67.55.202:20166',
 'http://84.153.211.70:2231',
 'http://120.255.176.113:7081',
 'http://191.109.142.185:40472',
 'http://137.133.161.221:28238',
 'http://84.164.237.24:25761',
 'http://225.128.63.184:7218',
 'http://92.54.7.70:17082',
 'http://86.161.223.182:11355',
 'http://186.204.155.188:55441',
 'http://215.145.148.194:56226',
 'http://248.147.146.92:41037',
 'http://234.88.172.121:23808',
 'http://40.0.58.158:37010',
 'http://190.97.52.157:2403',
 'http://57.153.90.244:14543',
 'http://81.25.84.189:56782',
 'http://202.28.74.252:62088',
 'http://8.78.102.188:36490',
 'http://117.58.91.215:60960',
 'http://51.146.185.184:22712',
 'http://12.30.62.115:14653',
 'http://245.20.200.58:28188',
 'http://2.154.248.45:35902',
 'http://195.160.17.231:15618',
 'http://14.243.106.22:47103',
 'http://70.250.40.179:23044',
 'http://27.50.253.99:50320',
 'http://148.250.7.186:27843',
 'http://217.255.19.134:14885',
 'http://115.118.220.198:3171',
 'http://184.234.157.18:61006',
 'http://244.251.73.212:35244',
 'http://127.113.183.253:34815',
 'http://70.237.103.135:51528',
 'http://143.201.142.110:24694',
 'http://153.121.60.162:15665',
 'http://152.136.62.251:36707',
 'http://158.98.197.170:6272',
 'http://71.236.190.115:26081',
 'http://41.121.17.192:37275',
 'http://218.82.89.245:33565',
 'http://82.24.223.28:33297',
 'http://183.57.162.230:30250',
 'http://185.232.170.56:33643',
 'http://243.114.253.111:12030',
 'http://30.90.228.202:4714',
 'http://100.0.107.1:49228',
 'http://126.103.89.187:61802',
 'http://225.224.73.233:15971',
 'http://213.129.175.47:52462',
 'http://33.188.148.220:40487',
 'http://211.141.120.160:15388',
 'http://168.215.101.130:59352',
 'http://255.137.15.80:11637',
 'http://118.84.162.70:52010',
 'http://224.79.218.212:39074',
 'http://101.69.87.141:18705',
 'http://95.126.24.148:65050',
 'http://223.204.191.252:47345',
 'http://138.221.1.69:1681',
 'http://247.25.6.40:61151',
 'http://228.219.27.3:64321',
 'http://255.79.225.16:59054',
 'http://30.123.183.246:12706',
 'http://130.176.53.22:11433',
 'http://76.147.177.56:7095',
 'http://103.113.141.123:45136',
 'http://231.213.140.170:5613',
 'http://163.170.217.78:42059',
 'http://58.199.18.89:13682',
 'http://47.153.239.189:2718',
 'http://172.103.222.24:9379',
 'http://202.40.247.148:64589',
 'http://144.104.118.0:42910',
 'http://44.51.95.128:26530',
 'http://135.161.82.124:46165',
 'http://132.250.108.147:46108',
 'http://218.227.64.108:26393',
 'http://12.201.2.189:11613',
 'http://46.204.158.231:59228',
 'http://179.88.181.197:57732',
 'http://105.161.89.28:2113',
 'http://183.48.119.1:34094',
 'http://112.237.48.237:64926',
 'http://201.6.38.180:19179',
 'http://91.202.214.19:25822',
 'http://198.51.146.52:37438',
 'http://59.78.208.174:37927',
 'http://126.171.163.78:6976',
 'http://150.235.99.159:16183',
 'http://99.65.183.50:2040',
 'http://122.192.190.21:2694',
 'http://2.80.128.106:50619',
 'http://34.40.239.248:12786',
 'http://28.182.36.245:58085',
 'http://100.244.209.207:37657',
 'http://254.109.124.244:13927',
 'http://76.95.99.162:38798',
 'http://81.217.73.175:18066',
 'http://81.79.213.59:9631',
 'http://91.134.160.79:15306',
 'http://126.61.221.85:3556',
 'http://238.170.27.39:54679',
 'http://185.36.188.32:44887',
 'http://69.179.215.193:29667',
 'http://25.201.62.97:46794',
 'http://131.76.47.126:4146',
 'http://174.63.62.149:61200',
 'http://43.58.249.123:6528',
 'http://68.42.214.3:46629',
 'http://72.206.224.113:16569',
 'http://223.41.238.113:62831',
 'http://245.39.235.203:65411',
 'http://77.5.78.209:41962',
 'http://44.60.21.237:65498',
 'http://94.46.170.62:36390',
 'http://214.112.142.33:56712',
 'http://217.11.211.32:26120',
 'http://237.151.238.96:41055',
 'http://187.192.47.234:30014',
 'http://3.159.253.100:11425',
 'http://82.114.162.13:37083',
 'http://56.138.48.180:14729',
 'http://164.49.199.121:13376',
 'http://245.151.151.121:15733',
 'http://194.23.103.156:39184',
 'http://216.147.34.144:3466',
 'http://76.15.144.59:37585',
 'http://244.243.126.188:31838',
 'http://233.185.247.42:15607',
 'http://37.13.8.93:49771',
 'http://191.241.116.72:19838',
 'http://119.35.208.96:30413',
 'http://174.53.94.78:11782',
 'http://156.109.180.78:29113',
 'http://45.98.98.227:54785',
 'http://108.222.180.150:7190',
 'http://109.13.224.43:6221',
 'http://188.103.200.160:64395',
 'http://69.91.37.162:38257',
 'http://243.106.132.251:15865',
 'http://210.73.56.92:23786',
 'http://37.17.212.137:29476',
 'http://105.163.93.76:48603',
 'http://126.157.247.91:26481',
 'http://35.104.25.51:34310',
 'http://174.15.244.128:26697',
 'http://170.155.77.185:20612',
 'http://47.228.183.214:27402',
 'http://44.93.1.134:25278',
 'http://186.62.32.185:39308',
 'http://128.189.164.194:59003',
 'http://254.138.138.129:57252',
 'http://162.119.127.212:12845',
 'http://230.49.235.130:45300',
 'http://137.64.150.95:7483',
 'http://254.193.76.202:62226',
 'http://22.2.250.117:62632',
 'http://103.187.251.28:21316',
 'http://125.139.94.127:24569',
 'http://209.148.56.180:29514',
 'http://237.47.43.223:51869',
 'http://170.92.180.163:48677',
 'http://9.159.122.249:7641',
 'http://60.98.60.199:44283',
 'http://251.56.188.226:42842',
 'http://95.251.198.164:4485',
 'http://29.220.194.212:45293',
 'http://215.139.23.31:48759',
 'http://61.167.201.8:24311',
 'http://16.218.125.209:5003',
 'http://139.1.139.134:16555',
 'http://246.66.68.129:21927',
 'http://71.212.223.79:59825',
 'http://6.133.235.42:25939',
 'http://122.12.86.38:21322',
 'http://94.191.96.18:17723',
 'http://123.200.95.171:47643',
 'http://142.98.178.151:51515',
 'http://18.142.63.65:33472',
 'http://151.179.138.241:49979',
 'http://191.247.53.53:21556',
 'http://254.51.210.206:11039',
 'http://166.69.101.185:5698',
 'http://14.79.235.6:56969',
 'http://58.172.216.141:59125',
 'http://231.38.79.12:21896',
 'http://187.64.106.253:49241',
 'http://232.47.155.55:49962',
 'http://251.226.206.22:58441',
 'http://86.213.123.168:24256',
 'http://234.165.91.235:5497',
 'http://251.223.126.35:64916',
 'http://2.50.5.81:36314',
 'http://191.35.212.25:27736',
 'http://66.184.1.103:25182',
 'http://80.242.79.226:63003',
 'http://83.74.252.67:36510',
 'http://125.95.252.122:16208',
 'http://122.21.99.0:17123',
 'http://1.159.193.255:25002',
 'http://171.140.97.172:43482',
 'http://251.174.93.173:49140',
 'http://118.249.80.155:43101',
 'http://77.63.221.41:28729',
 'http://152.41.79.10:50793',
 'http://124.109.129.81:17820',
 'http://141.18.178.32:47186',
 'http://160.207.31.55:17608',
 'http://169.158.209.114:57037',
 'http://205.137.48.59:59873',
 'http://117.114.134.47:60103',
 'http://220.37.27.62:20133',
 'http://129.152.145.199:27235',
 'http://122.136.21.110:30707',
 'http://197.45.31.69:29553',
 'http://108.219.156.254:54781',
 'http://16.208.243.176:29302',
 'http://249.190.134.21:48753',
 'http://21.62.182.119:38234',
 'http://156.138.31.219:24886',
 'http://207.35.122.221:12942',
 'http://76.202.145.77:29080',
 'http://128.45.113.222:35003',
 'http://77.75.75.57:30883',
 'http://121.117.101.115:2608',
 'http://186.183.18.176:1810',
 'http://83.151.236.30:22036',
 'http://47.128.244.104:30426',
 'http://115.227.238.140:48459',
 'http://184.99.58.121:55258',
 'http://117.20.163.78:23751',
 'http://35.151.97.251:1049',
 'http://22.133.72.6:51469',
 'http://112.202.103.198:52072',
 'http://64.21.133.214:30801',
 'http://34.198.158.213:43542',
 'http://179.59.10.241:30330',
 'http://34.57.101.122:13108',
 'http://87.217.180.20:62039',
 'http://101.26.194.223:31583',
 'http://94.183.20.76:19257',
 'http://170.171.179.10:62366',
 'http://183.87.52.138:63905',
 'http://111.226.174.133:6410',
 'http://175.214.160.119:17172',
 'http://42.141.223.110:31100',
 'http://188.93.113.191:58739',
 'http://203.131.41.0:52247',
 'http://184.188.100.92:44934',
 'http://106.35.4.153:62105',
 'http://248.88.235.170:17088',
 'http://199.64.86.161:37456',
 'http://176.106.72.234:53490',
 'http://19.194.166.169:51274',
 'http://13.162.236.90:51180',
 'http://216.92.153.250:29945',
 'http://154.146.118.84:53023',
 'http://228.93.48.49:51659',
 'http://40.97.151.243:39359',
 'http://106.90.64.28:4736',
 'http://237.82.252.69:21866',
 'http://100.232.202.124:35684',
 'http://228.252.97.16:60691',
 'http://178.188.144.73:46673',
 'http://150.165.214.203:51571',
 'http://141.152.62.206:38144',
 'http://88.233.12.171:49002',
 'http://163.51.119.225:38931',
 'http://163.160.220.227:35995',
 'http://51.219.101.172:43927',
 'http://19.134.181.70:23791',
 'http://133.82.43.200:16045',
 'http://173.110.43.43:46843',
 'http://168.91.248.60:52442',
 'http://234.46.251.183:29991',
 'http://42.89.158.68:3029',
 'http://25.60.161.221:7580',
 'http://25.235.116.44:16124',
 'http://155.100.63.241:18746',
 'http://132.12.86.73:1047',
 'http://197.12.246.200:1767',
 'http://52.142.54.145:45145',
 'http://214.217.6.167:56781',
 'http://41.111.126.80:61733',
 'http://34.177.24.201:60665',
 'http://228.188.89.113:30112',
 'http://126.49.94.189:5369',
 'http://83.7.123.172:6520',
 'http://250.181.203.145:22916',
 'http://75.51.248.197:55373',
 'http://121.190.165.79:7479',
 'http://13.44.231.41:1120',
 'http://20.73.172.145:62710',
 'http://189.16.229.2:14756',
 'http://204.255.102.100:10212',
 'http://230.210.17.12:36570',
 'http://63.24.14.23:45806',
 'http://69.18.216.16:31848',
 'http://247.21.152.190:13077',
 'http://236.157.111.203:29377',
 'http://251.191.33.26:11160',
 'http://60.53.97.193:11331',
 'http://134.18.129.25:28964',
 'http://66.151.24.13:12674',
 'http://190.164.108.98:28509',
 'http://174.53.188.12:12840',
 'http://25.59.65.176:8974',
 'http://176.4.121.182:27941',
 'http://195.103.182.51:18246',
 'http://107.238.87.230:5960',
 'http://3.59.236.126:7489',
 'http://206.157.97.39:26798',
 'http://254.169.154.42:53111',
 'http://2.239.225.139:1644',
 'http://190.145.50.17:24478',
 'http://109.6.245.42:48464',
 'http://47.55.124.218:54704',
 'http://156.60.241.206:22561',
 'http://251.63.202.223:15690',
 'http://203.183.82.57:46989',
 'http://77.239.162.143:58091',
 'http://186.173.13.186:48143',
 'http://107.16.123.223:15591',
 'http://149.149.97.130:53410',
 'http://74.88.24.59:33270',
 'http://33.161.71.230:24073',
 'http://108.31.126.90:48905',
 'http://205.55.192.43:26010',
 'http://165.144.31.0:9882',
 'http://179.226.17.123:43220',
 'http://141.28.209.189:47993',
 'http://21.219.137.0:37406',
 'http://203.4.51.116:4868',
 'http://175.238.200.236:39636',
 'http://105.134.200.71:51632',
 'http://58.66.61.166:2453',
 'http://155.1.111.86:34816',
 'http://252.34.197.56:4338',
 'http://252.88.18.30:14879',
 'http://169.7.205.247:40963',
 'http://17.83.114.19:20446',
 'http://120.109.184.40:21450',
 'http://148.69.48.105:38177',
 'http://156.123.83.59:46303',
 'http://71.81.142.207:3696',
 'http://250.166.142.57:53276',
 'http://60.173.208.1:39170',
 'http://191.2.139.182:56107',
 'http://180.78.196.147:45553',
 'http://94.69.161.229:48422',
 'http://54.29.153.45:24008',
 'http://81.157.119.93:54668',
 'http://229.50.47.49:58857',
 'http://133.243.244.226:9460',
 'http://82.177.208.246:4705',
 'http://222.206.247.100:36833',
 'http://211.67.162.133:62050',
 'http://32.12.84.242:44049',
 'http://229.66.229.59:3354',
 'http://188.166.154.225:26518',
 'http://172.120.213.182:48245',
 'http://124.19.69.160:32024',
 'http://159.11.201.21:25290',
 'http://229.143.70.103:63195',
 'http://69.245.40.196:24942',
 'http://89.70.150.118:33431',
 'http://112.185.223.133:6891',
 'http://157.9.13.62:2704',
 'http://223.62.181.82:60831',
 'http://245.236.110.214:16800',
 'http://23.63.70.29:16853',
 'http://180.134.51.63:12478',
 'http://178.20.97.235:34598',
 'http://131.113.241.126:52710',
 'http://103.0.233.37:33911',
 'http://76.181.206.143:40719',
 'http://41.101.217.241:16192',
 'http://141.19.106.124:44999',
 'http://57.63.224.87:16860',
 'http://209.99.62.29:56281',
 'http://176.0.255.222:9099',
 'http://217.5.3.202:41693',
 'http://208.165.238.96:25718',
 'http://90.234.228.117:36438',
 'http://238.168.13.156:56774',
 'http://52.29.38.46:41844',
 'http://71.204.134.27:47823',
 'http://113.86.18.208:55479',
 'http://223.230.212.50:24043',
 'http://254.174.250.243:14991',
 'http://186.237.64.243:59517',
 'http://184.32.112.140:53110',
 'http://55.47.86.8:54183',
 'http://68.82.158.130:54622',
 'http://210.148.204.15:1841',
 'http://244.34.59.202:19996',
 'http://16.145.74.27:21655',
 'http://225.59.96.84:48020',
 'http://228.147.160.132:49064',
 'http://21.121.233.0:22645',
 'http://166.39.197.41:41877',
 'http://240.166.146.212:4727',
 'http://74.193.151.150:44949',
 'http://5.223.52.220:42927',
 'http://5.170.139.28:47822',
 'http://165.156.219.203:38811',
 'http://146.75.45.45:11230',
 'http://154.203.61.164:55755',
 'http://181.218.77.158:64732',
 'http://218.225.189.99:9964',
 'http://41.34.253.16:62262',
 'http://216.85.103.116:62891',
 'http://131.2.182.231:44088',
 'http://156.242.71.70:45672',
 'http://84.156.208.11:38734',
 'http://3.34.43.186:12270',
 'http://232.243.194.128:23485',
 'http://54.66.18.73:30855',
 'http://49.83.255.140:49143',
 'http://202.149.82.254:12489',
 'http://51.114.223.83:47019',
 'http://236.230.249.230:54637',
 'http://197.60.147.212:8039',
 'http://196.221.109.36:26942',
 'http://3.204.23.106:40528',
 'http://200.23.163.149:35299',
 'http://153.53.158.23:3458',
 'http://97.188.193.174:41354',
 'http://160.242.87.69:28680',
 'http://239.77.125.169:28746',
 'http://79.63.36.29:8533',
 'http://143.80.87.62:21853',
 'http://144.208.141.105:39488',
 'http://97.9.11.48:6088',
 'http://59.239.101.95:36818',
 'http://224.48.167.220:49817',
 'http://210.46.68.184:10566',
 'http://205.162.147.231:14593',
 'http://133.125.192.217:26375',
 'http://192.101.76.75:53870',
 'http://213.135.20.59:59816',
 'http://216.247.56.38:27906',
 'http://223.140.222.80:57101',
 'http://253.92.129.68:32074',
 'http://205.107.248.232:24665',
 'http://142.212.174.69:39445',
 'http://37.104.69.92:52571',
 'http://163.231.249.150:32624',
 'http://199.209.252.20:25672',
 'http://31.220.81.14:31496',
 'http://70.70.225.62:35824',
 'http://10.41.247.180:29507',
 'http://223.76.245.113:32336',
 'http://78.157.199.53:13355',
 'http://166.255.239.74:25750',
 'http://158.25.24.191:22757',
 'http://71.150.181.195:28000',
 'http://79.206.156.63:1238',
 'http://4.125.212.164:25287',
 'http://120.181.114.75:54002',
 'http://116.30.129.11:47752',
 'http://57.110.209.154:1958',
 'http://215.213.130.2:42873',
 'http://50.175.63.189:19163',
 'http://183.161.140.91:51707',
 'http://107.116.204.123:31541',
 'http://111.163.87.189:33118',
 'http://150.139.109.202:47649',
 'http://238.30.253.85:27255',
 'http://33.143.212.145:6266',
 'http://176.7.58.88:54787',
 'http://169.198.26.76:7882',
 'http://17.119.74.233:36103',
 'http://74.98.182.254:12777',
 'http://62.25.113.131:52102',
 'http://195.183.152.157:56301',
 'http://160.134.88.232:54824',
 'http://195.107.50.21:16757',
 'http://127.166.205.14:57476',
 'http://244.145.27.248:6639',
 'http://117.25.37.174:38409',
 'http://209.32.188.65:11217',
 'http://124.138.3.144:59513',
 'http://11.138.172.63:47581',
 'http://2.135.150.224:8595',
 'http://27.195.22.11:35026',
 'http://26.132.169.22:23191',
 'http://182.239.248.177:13300',
 'http://93.52.26.61:33529',
 'http://22.0.50.181:37511',
 'http://34.69.151.223:59448',
 'http://12.161.47.51:44393',
 'http://138.36.125.36:43617',
 'http://103.71.8.26:33396',
 'http://182.153.203.236:61164',
 'http://94.0.88.223:33384',
 'http://228.175.42.160:24851',
 'http://23.243.118.117:6503',
 'http://83.249.137.32:21284',
 'http://27.10.245.129:65362',
 'http://133.203.80.22:22856',
 'http://202.0.97.176:50974',
 'http://1.141.243.35:53030',
 'http://94.169.155.193:9656',
 'http://93.248.60.7:44631',
 'http://40.229.118.30:54566',
 'http://89.217.250.168:49891',
 'http://110.177.130.205:28402',
 'http://227.126.123.44:50385',
 'http://83.42.115.197:14865',
 'http://184.90.169.91:45386',
 'http://227.54.160.0:39818',
 'http://66.5.144.186:19689',
 'http://59.137.223.227:2036',
 'http://92.20.230.96:5133',
 'http://253.231.110.146:54598',
 'http://160.27.253.241:54555',
 'http://211.75.94.209:60755',
 'http://36.91.137.236:36257',
 'http://165.104.232.200:34830',
 'http://135.160.179.28:30780',
 'http://27.153.221.199:40507',
 'http://118.243.11.187:47773',
 'http://36.151.31.155:46495',
 'http://90.73.149.15:64136',
 'http://231.179.42.167:11167',
 'http://38.226.233.197:56392',
 'http://107.188.116.154:51673',
 'http://9.36.109.2:46010',
 'http://249.114.209.141:9599',
 'http://186.97.177.215:39718',
 'http://76.47.166.218:48047',
 'http://35.125.142.249:8183',
 'http://150.129.133.134:24850',
 'http://110.17.87.173:26466',
 'http://226.171.23.242:61914',
 'http://122.122.36.76:62967',
 'http://199.243.187.132:45538',
 'http://178.79.217.120:63444',
 'http://238.167.116.224:31030',
 'http://39.185.71.250:43278',
 'http://73.154.97.253:48131',
 'http://17.88.131.158:38540',
 'http://17.77.95.21:22618',
 'http://20.122.154.35:30001',
 'http://129.55.92.234:29936',
 'http://204.103.32.216:18484',
 'http://215.18.220.227:30117',
 'http://245.13.45.0:16947',
 'http://206.253.100.7:29816',
 'http://250.109.111.82:46893',
 'http://170.62.15.180:26368',
 'http://184.204.99.48:20699',
 'http://92.175.184.62:32776',
 'http://141.218.18.250:13179',
 'http://121.55.239.237:50818',
 'http://51.76.128.247:9344',
 'http://198.146.224.4:36208',
 'http://86.142.141.12:27394',
 'http://41.95.247.11:38352',
 'http://224.21.194.216:31841',
 'http://53.212.222.208:29928',
 'http://251.198.176.82:10336',
 'http://161.27.177.41:28660',
 'http://251.147.128.69:30057',
 'http://216.153.30.119:56595',
 'http://93.237.77.54:3637',
 'http://65.4.99.80:60877',
 'http://60.130.52.49:35023',
 'http://174.59.237.11:41483',
 'http://50.170.82.79:47696',
 'http://128.152.225.150:55088',
 'http://92.252.199.4:24200',
 'http://200.177.65.142:64484',
 'http://222.197.147.184:37143',
 'http://166.75.18.138:49456',
 'http://190.11.97.165:44948',
 'http://222.80.87.143:32214',
 'http://123.25.115.28:37775',
 'http://175.105.69.136:43696',
 'http://5.47.14.44:2786',
 'http://76.155.91.183:10949',
 'http://20.252.246.130:26619',
 'http://44.82.243.18:30871',
 'http://99.2.42.247:31919',
 'http://47.131.227.127:61568',
 'http://5.236.205.187:60735',
 'http://136.40.73.126:55587',
 'http://41.202.209.137:23828',
 'http://193.214.136.11:17299',
 'http://163.72.212.10:4946',
 'http://4.225.7.148:14877',
 'http://128.120.128.191:15437',
 'http://92.149.174.20:31873',
 'http://176.59.137.246:63859',
 'http://214.47.134.41:24200',
 'http://223.212.189.228:60023',
 'http://194.75.177.52:61320',
 'http://87.130.106.194:58717',
 'http://224.139.160.216:33447',
 'http://245.179.198.201:10164',
 'http://86.99.139.238:44732',
 'http://160.159.206.170:63251',
 'http://129.102.179.8:59589',
 'http://129.239.89.128:43442',
 'http://218.136.228.220:19019',
 'http://4.4.42.37:22383',
 'http://164.140.0.55:27857',
 'http://235.99.213.69:4562',
 'http://186.17.251.70:13437',
 'http://139.205.79.153:35241',
 'http://57.97.84.143:32675',
 'http://64.91.102.233:59483',
 'http://68.205.166.208:17707',
 'http://151.78.38.15:32262',
 'http://85.159.152.123:9548',
 'http://42.189.246.56:43858',
 'http://95.3.236.13:37633',
 'http://186.128.158.107:44003',
 'http://198.62.0.60:60370',
 'http://223.239.192.236:64125',
 'http://13.33.45.117:36265',
 'http://178.255.14.96:7585',
 'http://46.227.212.44:22670',
 'http://162.225.47.176:48232',
 'http://134.218.182.33:44049',
 'http://26.13.118.96:16098',
 'http://87.179.238.27:64140',
 'http://29.117.129.195:30451',
 'http://8.39.79.58:7390',
 'http://18.212.226.104:17669',
 'http://45.150.79.226:42639',
 'http://186.233.71.193:11792',
 'http://141.89.253.167:2484'
]

ban = """
                        ██████████████████████████████████
                        █▄─█─▄█▄─▄▄─█▄─▀█▄─▄█─▄▄─█▄─▀█▀─▄█
                        ██▄▀▄███─▄█▀██─█▄▀─██─██─██─█▄█─██
                        ▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀ 
              By Poison                                               ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
  •@DefenderDB        •Tg: @softQWK1XIII⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


  1) Отправить письмо в поддержку Tg
  2) Проверить почты на работоспособность
  3) Отправить письмо на указанный адрес
  4) Отправить жалобу на сайт Telegram
  5) Проверить User-Agent на работоспособность
  6) Включить/Выключить цвета
  7) Проверить прокси на работоспособность
  8) Выход
  
"""

use_colors = True

def print_menu():
    if use_colors:
        Write.Print(ban, Colors.black_to_green, interval=0.0001)
    else:
        print(ban)

def send_email(receiver, sender_email, sender_password, subject, body):
    domain = sender_email.split('@')[1]
    if domain not in smtp_servers:
        if use_colors:
            Write.Print(f"  Неизвестный домен почты {sender_email}.\n", Colors.red, interval=0.0001)
        else:
            print(f"  Неизвестный домен почты {sender_email}.")
        return False

    smtp_server, smtp_port = smtp_servers[domain]

    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver, msg.as_string())
            time.sleep(3)

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if use_colors:
            Write.Print(f"  Письмо успешно отправлено с {sender_email} на {receiver} в {current_time}.\n", Colors.green, interval=0.0001)
        else:
            print(f"  Письмо успешно отправлено с {sender_email} на {receiver} в {current_time}.")
        return True
    except Exception as e:
        if use_colors:
            Write.Print(f"  Ошибка при отправке письма: {e}\n", Colors.red, interval=0.0001)
        else:
            print(f"  Ошибка при отправке письма: {e}")
        logging.error(f"Ошибка при отправке письма с {sender_email} на {receiver}: {e}")
        return False

import socket

def check_email(sender_email, sender_password):
    domain = sender_email.split('@')[1]
    if domain not in smtp_servers:
        if use_colors:
            Write.Print(f"  Неизвестный домен почты {sender_email}.\n", Colors.red, interval=0.0001)
        else:
            print(f"  Неизвестный домен почты {sender_email}.")
        return False

    smtp_server, smtp_port = smtp_servers[domain]

    try:
        with smtplib.SMTP(smtp_server, smtp_port, timeout=10) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender_email, sender_password)
            if use_colors:
                Write.Print(f"  Почта {sender_email} работает.\n", Colors.green, interval=0.0001)
            else:
                print(f"  Почта {sender_email} работает.")
            return True
    except smtplib.SMTPAuthenticationError as e:
        if use_colors:
            Write.Print(f"  Ошибка аутентификации для почты {sender_email}: {e}\n", Colors.red, interval=0.0001)
        else:
            print(f"  Ошибка аутентификации для почты {sender_email}: {e}")
        logging.error(f"Ошибка аутентификации для почты {sender_email}: {e}")
        return False
    except (smtplib.SMTPException, TimeoutError) as e:
        if use_colors:
            Write.Print(f"  Почта {sender_email} не работает: {e}\n", Colors.red, interval=0.0001)
        else:
            print(f"  Почта {sender_email} не работает: {e}")
        logging.error(f"Почта {sender_email} не работает: {e}")
        return False

def check_emails():
    for sender_email, sender_password in senders.items():
        check_email(sender_email, sender_password)

def send_custom_email():
    receiver = Write.Input("  Введите почту получателя: ", Colors.black_to_green if use_colors else Colors.white, interval=0.0001)
    subject = Write.Input("  Введите тему письма: ", Colors.black_to_green if use_colors else Colors.white, interval=0.0001)
    message = Write.Input("  Введите текст письма: ", Colors.black_to_green if use_colors else Colors.white, interval=0.0001)
    num_requests = int(Write.Input("  Введите количество запросов: ", Colors.black_to_green if use_colors else Colors.white, interval=0.0001))

    for _ in range(num_requests):
        sender_email, sender_password = random.choice(list(senders.items()))
        send_email(receiver, sender_email, sender_password, subject, message)
        delay = random.uniform(5, 10)  
        time.sleep(delay)

    Write.Input("  Нажмите Enter для возврата в меню...", Colors.black_to_green if use_colors else Colors.white, interval=0.0001)
    # Ето часть кода где отправка будет через прокси
Для_Прокси = """
def send_complaint(phone, email, complaint_text):
    url = "https://telegram.org/support"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": random.choice(user_agents)
    }
    data = {
        "message": complaint_text,
        "email": email,
        "phone": phone,
        "setln": "ru"
    }
    
    for proxy in proxies:
        proxies_dict = {
            "http": proxy,
            "https": proxy
        }
        try:
            response = requests.post(url, headers=headers, data=data, proxies=proxies_dict, timeout=10)
            if response.status_code == 200:
                return True, phone, email
        except (requests.exceptions.RequestException, requests.exceptions.Timeout):
            continue
    
    return False, phone, email

def send_complaint_to_tg():
    complaint_text = Write.Input("  Введите текст жалобы: ", Colors.black_to_green if use_colors else Colors.white, interval=0.0001)
    num_requests = int(Write.Input("  Введите количество запросов: ", Colors.black_to_green if use_colors else Colors.white, interval=0.0001))

    for _ in range(num_requests):
        phone = random.choice(phones)
        email = random.choice(site_emails)
        success, used_phone, used_email = send_complaint(phone, email, complaint_text)
        if success:
            if use_colors:
                Write.Print(f"  Жалоба успешно отправлена на номер {used_phone} и почту {used_email}.\n", Colors.green, interval=0.0001)
            else:
                print(f"  Жалоба успешно отправлена на номер {used_phone} и почту {used_email}.")
        else:
            if use_colors:
                Write.Print("  Нет рабочих прокси для отправки жалобы.\n", Colors.red, interval=0.0001)
            else:
                print("  Нет рабочих прокси для отправки жалобы.")
        delay = random.uniform(5, 10)  
        time.sleep(delay)

    Write.Input("  Нажмите Enter для возврата в меню...", Colors.black_to_green if use_colors else Colors.white, interval=0.0001)
"""
# Тут отправка без прокси выше есть часит кола где можете сами заменить чтобы он использовал прокси 
# -----от-----
def send_complaint(phone, email, complaint_text):
    url = "https://telegram.org/support"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": random.choice(user_agents)
    }
    data = {
        "message": complaint_text,
        "email": email,
        "phone": phone,
        "setln": "ru"
    }
    
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        if response.status_code == 200:
            return True, phone, email
    except (requests.exceptions.RequestException, requests.exceptions.Timeout):
        return False, phone, email
    
    return False, phone, email

def send_complaint_to_tg():
    complaint_text = Write.Input("  Введите текст жалобы: ", Colors.black_to_green if use_colors else Colors.white, interval=0.0001)
    num_requests = int(Write.Input("  Введите количество запросов: ", Colors.black_to_green if use_colors else Colors.white, interval=0.0001))

    for _ in range(num_requests):
        phone = random.choice(phones)
        email = random.choice(site_emails)
        success, used_phone, used_email = send_complaint(phone, email, complaint_text)
        if success:
            if use_colors:
                Write.Print(f"  Жалоба успешно отправлена номер: {used_phone} почтa: {used_email}.\n", Colors.green, interval=0.0001)
            else:
                print(f"  Жалоба успешно отправлена номер: {used_phone} почтa: {used_email}")
        else:
            if use_colors:
                Write.Print("  Ошибка при отправке жалобы.\n", Colors.red, interval=0.0001)
            else:
                print("  Ошибка при отправке жалобы.")
        delay = random.uniform(5, 10)  
        time.sleep(delay)

    Write.Input("  Нажмите Enter для возврата в меню...", Colors.black_to_green if use_colors else Colors.white, interval=0.0001)
# ----до-----

def toggle_colors():
    global use_colors
    use_colors = not use_colors
    if use_colors:
        Write.Print("  Цвета включены.\n", Colors.green, interval=0.0001)
    else:
        print("  Цвета выключены.")

def check_proxy(proxy):
    try:
        response = requests.get("http://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            return True
    except:
        pass
    return False

def check_proxies():
    for proxy in proxies:
        if check_proxy(proxy):
            if use_colors:
                Write.Print(f"  Прокси {proxy} работает.\n", Colors.green, interval=0.0001)
            else:
                print(f"  Прокси {proxy} работает.")
        else:
            if use_colors:
                Write.Print(f"  Прокси {proxy} не работает.\n", Colors.red, interval=0.0001)
            else:
                print(f"  Прокси {proxy} не работает.")

def check_user_agent(user_agent):
    headers = {
        "User-Agent": user_agent
    }
    try:
        response = requests.get("http://httpbin.org/user-agent", headers=headers, timeout=5)
        if response.status_code == 200:
            return True
    except:
        pass
    return False

def check_user_agents():
    for user_agent in user_agents:
        if check_user_agent(user_agent):
            if use_colors:
                Write.Print(f"  User-Agent {user_agent} работает.\n", Colors.green, interval=0.0001)
            else:
                print(f"  User-Agent {user_agent} работает.")
        else:
            if use_colors:
                Write.Print(f"  User-Agent {user_agent} не работает.\n", Colors.red, interval=0.0001)
            else:
                print(f"  User-Agent {user_agent} не работает.")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_menu()
        choice = Write.Input("  Выберите действие: ", Colors.black_to_green if use_colors else Colors.white, interval=0.0001)

        if choice == '1':
            subject = Write.Input("  Введите тему письма: ", Colors.black_to_green if use_colors else Colors.white, interval=0.0001)
            message = Write.Input("  Введите текст письма: ", Colors.black_to_green if use_colors else Colors.white, interval=0.0001)
            num_requests = int(Write.Input("  Введите количество запросов: ", Colors.black_to_green if use_colors else Colors.white, interval=0.0001))

            for _ in range(num_requests):
                sender_email, sender_password = random.choice(list(senders.items()))
                recipient_email = random.choice(recipients)
                send_email(recipient_email, sender_email, sender_password, subject, message)
                delay = random.uniform(5, 10)  
                time.sleep(delay)

            Write.Input("  Нажмите Enter для возврата в меню...", Colors.black_to_green if use_colors else Colors.white, interval=0.0001)

        elif choice == '2':
            check_emails()
            Write.Input("  Нажмите Enter для возврата в меню...", Colors.black_to_green if use_colors else Colors.white, interval=0.0001)

        elif choice == '3':
            send_custom_email()

        elif choice == '4':
            send_complaint_to_tg()

        elif choice == '8':
            if use_colors:
                Write.Print("  Выход из программы...\n", Colors.black_to_green, interval=0.0001)
            else:
                print("  Выход из программы...")
            break

        elif choice == '6':
            toggle_colors()
            Write.Input("  Нажмите Enter для возврата в меню...", Colors.black_to_green if use_colors else Colors.white, interval=0.0001)

        elif choice == '7':
            check_proxies()
            Write.Input("  Нажмите Enter для возврата в меню...", Colors.black_to_green if use_colors else Colors.white, interval=0.0001)

        elif choice == '5':
            check_user_agents()
            Write.Input("  Нажмите Enter для возврата в меню...", Colors.black_to_green if use_colors else Colors.white, interval=0.0001)

if __name__ == "__main__":
    main()  