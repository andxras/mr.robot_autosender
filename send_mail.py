import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from os import path, listdir

# local
import cfg as config


m = MIMEMultipart()
receiver_email  = config.RECEIVER_EMAIL
sender_email    = config.SENDER_EMAIL
password        = config.PASSW
evidence_path   = config.EVIDENCE_PATH
subject         = config.SUBJECT


def init_m() -> None:
    """ Initialize message dict
    """
    global m

    m['Subject'] = subject
    m['From'] = sender_email
    m['To'] = receiver_email


def r_attachments() -> None:
    """ Read attachments and insert into message
    """
    global m

    files = listdir(evidence_path)

    for fn in files:
        ext: str = fn.rsplit('.')[1]

        # handle images
        if ext in ['jpeg','jpg','png']:
            with open(evidence_path + fn, 'rb') as fp:
                img = MIMEImage(fp.read())
                img.add_header('Content-Disposition', 'attachment', filename = fn)
                m.attach(img)

        # handle text files
        if ext in ['csv', 'txt']:
            tf = MIMEText(open(evidence_path + fn).read())
            m.attach(tf)

        # handle pdf files
        if ext == 'pdf':
            pdf = MIMEApplication(open(fn, 'rb').read())
            pdf.add_header('Content-Disposition', 'attachment', filename = fn)
            m.attach(pdf)


    return


def m_send() -> bool:
    """ Send mail
    """
    global m

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(sender_email, password)

    init_m()
    r_attachments()

    try:
        session.sendmail(sender_email, [receiver_email], m.as_string())
        session.quit()
        
        return True
    except:
        session.quit()
    
    return False

f = m_send()
print(f)