import imaplib, email, re, clipboard
from time import sleep
from email.header import decode_header, make_header
# User Input
"""
user
password
emailSender
"""

# Waiting for mail (Analog type)
# fix when mail came on refresh mailbox and load new mail
sleep(3)

# we must find Security Solutions
user = ""
password = ""

imap = imaplib.IMAP4_SSL("imap.gmail.com")

try:
    imap.login(user, password)
except:
    print("Failed to Login")
    exit();

# Mailbox Settings
# imap.select("INBOX")
imap.select("INBOX")

# Load to Sender Settings
status, messages = imap.uid("search", None, '(FROM "email@email.com")')
messages = messages[0].split()

# Select value of List
recent = messages[-1]
res, msg = imap.uid('fetch', recent, "(RFC822)")
raw = msg[0][1]
email_message = email.message_from_bytes(raw)

body = email_message.get_payload(decode=True).decode()

# test code
print(body) 

# Search Pattern 
# it really slow we gonna find new way
re_pattern = re.compile(r">\d\d\d\d\d\d<")
result = re.findall(re_pattern, body)

extract_code = re.sub(r'[^0-9]', '', result[0])

try:
    clipboard.copy(extract_code)
except:
    print("Clipboard: Can't copy normally")