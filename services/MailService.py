from flask import Flask, copy_current_request_context
from flaskext.mail import Mail, Message
from mako.template import Template
from mako.lookup import TemplateLookup
import threading


class MailService():
	def __init__(self, app):
		self.app = app
		self.setupConfiguration()
		self.mail = Mail(app)
		self.lookup = TemplateLookup(directories=['mail'], output_encoding='utf-8', encoding_errors='replace')


	def setupConfiguration(self):
		self.app.config['MAIL_USERNAME'] = "nny.fwk@gmail.com"
		self.app.config['MAIL_PASSWORD'] = "sarasaza"
		self.app.config['DEFAULT_MAIL_SENDER'] = "enjoy-events"
		self.app.config['MAIL_SERVER'] = "smtp.gmail.com"
		self.app.config['MAIL_PORT'] = "465"
		self.app.config['MAIL_USE_SSL'] = True
		

	def createUser(self, user):
		msg = Message("Bienvenido a Enjoy-events", recipients=[user.email])
		msg.html = self.lookup.get_template("registration.html").render(user=user)
		self.sendMail(msg)

	def assistance(self, assistance, user):
		msg = Message("Vas a asistir al evento %s" % assistance.event.name, recipients=[user.email])
		msg.html = self.lookup.get_template("assistance.html").render(assistance=assistance)
		self.sendMail(msg)

	def sendMail(self, msg):
		try:
			@copy_current_request_context
			def sendMessage(self, msg):
				self.mail.send(msg)
			if self.app.config['SEND_EMAILS']:
				sender = threading.Thread(name='mailService', target=sendMessage, args=(self, msg))
				#sender.start()
		except Exception as err:
			print err

