import imaplib, email, re, clipboard
from time import sleep
from email.header import decode_header, make_header

# waiting for mail
sleep(3)

user = ""
password = ""

imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(user, password)

# Mailbox Settings
imap.select("INBOX")
# default
# imap.select("INBOX")

# Sender Settings
status, messages = imap.uid("search", None, '(FROM "@gmail.com")')
messages = messages[0].split()

# Select value of List
recent = messages[-1]
res, msg = imap.uid('fetch', recent, "(RFC822)")
raw = msg[0][1]
email_message = email.message_from_bytes(raw)

body = email_message.get_payload(decode=True).decode()

# Search Pattern 
re_pattern = re.compile(r">\d\d\d\d\d\d<")
result = re.findall(re_pattern, body)

extract_code = re.sub(r'[^0-9]', '', result[0])

clipboard.copy(extract_code)