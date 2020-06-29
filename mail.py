import email
import imaplib

EMAIL = '###'  # Email login
PASSWORD = '###'  # Email password
SERVER = '###'  # Сервер для работы с почтой


mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)
mail.select('inbox')  # чтение папки "Входящие". При выводе сообщений от конкретного отправителя в отдельную папку
                      # можно избавиться от условия в line 38


def real_gmail():
    mail.select('inbox')
    status, data = mail.search(None, 'UNSEEN')
    mail_ids = []
    for block in data:
        mail_ids += block.split()
    for i in mail_ids:
        status, data = mail.fetch(i, '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])
                mail_from = message['from']
                mail_subject = message['subject']

                if message.is_multipart():
                    mail_content = ''

                    for part in message.get_payload():

                        if part.get_content_type() == 'text/plain':
                            mail_content += part.get_payload()
                else:
                    mail_content = message.get_payload()
                     #if mail_from ==  'any'
                       #print(f'Сообщение от: {mail_from}')
                       #print(f'Subject: {mail_subject}')
                       #print(f'Content: {mail_content}')
                return mail_from


if __name__ == '__main__':
    try:
        while True:
            real_gmail()
    finally:
        print("Thanks")