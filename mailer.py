
import json
import re
import requests
import facebook
import time

def get_facebook_data():
	# Code to retrieve the extended token using the short lived access token
	# graph = facebook.GraphAPI('SHORT_LIVED_ACCESS_TOKEN')
	# app_id = 'xxxxxxx'
	# app_secret = 'xxxxxxxxxxx'
	# extended_token = graph.extend_access_token(app_id, app_secret)
	# print extended_token

	epoch_time = int(time.time())
	prod_links = ""
	resp = requests.get('https://graph.facebook.com/{FACEBOOK_GROUP_ID}/feed?__paging_token=enc_xxxxxxxxxxxxxxxx&until='+ str(epoch_time) + '&limit=100&access_token={EXTENDED_ACCESS_TOKEN}')

	resp_json = json.loads(resp.content)

	data_list = resp_json['data']
	for item in data_list:
		if item.has_key('message') and ("table" in item['message'] or "desk" in item['message']):
			id = re.search(r"\$(\d{1,})", item['message'])
			prod_links = prod_links + "Link - " + "https://www.facebook.com/groups/{FACEBOOK_GROUP_ID}/" + item['id'][-15:] + "\n" #Construct link from data received to be sent in the email

	send_email("{EMIAL_ID_OF_SENDER}", "{PASSWORD_FOR_SENDER_EMAIL}", "{RECIPIENT_MAIL_ADDRESS}", "{SUBJECT_OF_OUTGOING_MAIL}", prod_links)

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

get_facebook_data()