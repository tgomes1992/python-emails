import email
import imaplib


EMAIL = 'tt7.thiago@gmail.com'
PASSWORD = "dpgethrasbketuzg"
SERVER = 'imap.gmail.com'

mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)

mail.select('inbox')

status, data = mail.search(None, 'ALL')

mail_ids = []


for block in data:
    # a função split chamada sem nenhum parâmetro
    # transforma texto ou bytes em listas usando como
    # ponto de divisão o espaço em branco:
    # b'1 2 3'.split() => [b'1', b'2', b'3']
    mail_ids += block.split()



baixado = mail.fetch(mail_ids[1],'(RFC822)')


print(str(baixado)[30:40])






