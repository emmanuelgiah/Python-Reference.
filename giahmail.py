import sys
import smtplib

if len(sys.argv) > 1:
	mail = ' '.join(sys.argv[1:]);

smtpObj = smtplib.SMTP('smtp.google.com', 587)
smtpObj.ehlo();