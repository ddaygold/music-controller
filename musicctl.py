import imaplib
import smtplib
import sys
import email
import email.message as emailmessage
import subprocess
import alsaaudio
import logging
import argparse
import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--credfile',required=True)
    args = parser.parse_args()

    '''
    The credfile is where the login details are stored for use by the script. Obviously they should not be in the 
    git repo ;)

    The credfile is a simple text file with a field per line in this order:
        username
        password (cleartext)
        email address to notify of muting
        imap server address
        imap server port
        smtp server address
        smtp server port
        logfile path

    '''
    credfile = open(args.credfile,'r')
    USER,PASS,MAILING_LIST,IMAP_SERVER,IMAP_PORT_STRING,SMTP_SERVER,SMTP_PORT_STRING,LOG_FILE = [x.strip() for x in credfile.readlines()]
    IMAP_PORT = int(IMAP_PORT_STRING)
    SMTP_PORT = int(SMTP_PORT_STRING)

    #logging block
    logger = logging.getLogger('music-controller')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(LOG_FILE)
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info('Starting up')


    #THis is the default audio device, which might not work for other people
    m = alsaaudio.Mixer(control='Master',id=0,cardindex=0)

    sender =smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    sender.login(USER,PASS)

    recv = imaplib.IMAP4_SSL(IMAP_SERVER,IMAP_PORT)
    recv.login(USER,PASS)
    recv.select()

    typ, data = recv.search(None, 'ALL')
    data_set = set(int(x) for x in data[0].split())
    r_set = set()
    toget = data_set - r_set
    for target in data_set:
        typ, data = recv.fetch(target, '(RFC822)')
        mail = data[0][1]
        message = email.message_from_string(mail)
        subject = message['Subject'].strip()
        logger.info('working on '+subject)
        author = message['From']
        if subject.startswith('MUTE'):
            logger.info('Found a mute command, muting')
            m.setmute(1)
            msg = emailmessage.Message()
            msg['To'] = MAILING_LIST
            msg['From'] = USER
            msg['Subject'] = str(datetime.datetime.now()) + ' Muting'
            sender.sendmail(USER,MAILING_LIST,str(msg))
        logger.info('Deleting '+subject)
        recv.store(target,'+FLAGS','\\Deleted')
        recv.expunge()
    sender.quit()

if __name__ == "__main__":
        main()
