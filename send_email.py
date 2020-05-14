# Cкрипт отправки почты с gmail

# Импортируем необходимые библиотеки
# stplib для работы с протоколом smtp
import smtplib
# mime понадобятся для работы с кириллицей
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

f = open('data')
lines = f.readlines()

# Настройки вашего ящика
your_email = lines[0][0:-1]
your_login = lines[1][0:-1]
your_password = lines[2][0:-1]
smpt_server = lines[3][0:-1]
smtp_port = 587

# при импортировании скрипта можно вызвать send('Электронный адрес получателя', 'Тема', 'Письмо')
def send(email, subject, message):
    # указываем ящик отправителя и ящик полуаетля
    from_email = your_email
    to_email = email

    # сервер, порт, лдоги и пароль
    server = smpt_server
    port = smtp_port
    login = your_login
    password = your_password

    # немного магии для работы с кириллицей
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # присваем переменной message данные агрумента message
    message = message
    msg.attach(MIMEText(message, 'plain'))

    # отправка письма
    smtp_obj = smtplib.SMTP(server, port)
    smtp_obj.starttls()
    smtp_obj.login(login, password)
    smtp_obj.sendmail(from_email, to_email, msg.as_string())
    smtp_obj.quit()
