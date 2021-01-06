from flask import Flask
from send_mail import m_send

app = Flask(__name__)

from app import routes