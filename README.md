# Send Mail

Простой скрипт на Python для отправки электронной почты по протоколу smtp.
Оформлен в ввиде функции для импорта в другие скрипты. 

Информация для входа по умолчанию подгружается из текстового файла data содержащего 4 строки:
- email
- login
- password
- smtp server

**Пример использования**

```
from send_email import send

send('email', 'subject', 'message')

```
