#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import imaplib2 as imaplib
from email import Header
from email.parser import Parser


#Se definen los párametros de configuración del correo
HOST = 'imap.gmail.com'
PORT = '993'
USER = '####@gmail.com'
PAWD = '####'
HAM_F  = 'INBOX'

LIMIT = 40  # Cuantos correos se va  a buscar en la bandeja de entrada

# Se intenta hacer un loggeo de forma segura
g = imaplib.IMAP4_SSL(HOST)
try:
    r, info= g.login(USER, PAWD)
except Exception, e:
    print str(e)

# g contine la bandeja de entrada
g.select(HAM_F)


typ, msg_ids = g.search(None, ('ALL'))

if typ=='OK':
    ids = msg_ids[0].split(' ')
    f = open('./MsgsIDS.txt', 'w')
    for id in ids[:LIMIT]:

        (r,msg) = g.fetch(id, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
        pre_messageID = msg[0][1]
        print(pre_messageID)
        try:
            MessageID = re.compile(r'[0-9a-f]{8}.[0-9a-f]{8}.[0-9a-f]{5}.[0-9a-f]{4}SMTPIN_ADDED_BROKEN@mx.google.com').findall(pre_messageID)[0]
            print(MessageID)
            f.write(MessageID+"\n")
        except:
            continue


    f.close()
#rfc822msgid:A9EHm3cAvAQeii8vQWQV3Q@notifications.google.com
g.logout()
