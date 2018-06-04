import email_config
import email_lists
import time
import datetime
import smtplib

# Send email from address in email_config 
def send_email(to_addr, subject, message_text):
    message = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (email_config.FROM_ADDR, to_addr, subject, message_text)

    try:
        server = smtplib.SMTP_SSL(email_config.SMTP_SSL_ADDR, email_config.PORT)
        server.login(email_config.FROM_ADDR, email_config.PASSWORD)
        server.sendmail(email_config.FROM_ADDR, to_addr, message)
        server.quit()    
        print('Email to ' + to_addr + ' has been sent.')
    except:
        print('Email to ' + to_addr + ' could NOT be sent.\t:(')


for email in email_lists.tasks:
    combined_msg = ''

    for msg in email_lists.tasks[email]:
        combined_msg += msg + '\n'

    send_email(email, "{SCT BOT} Mfg. Progress Updater " + datetime.datetime.today().strftime('%Y-%m-%d'), combined_msg)

    # Take a quick nap because sending these emails does weird stuff
    time.sleep(2)