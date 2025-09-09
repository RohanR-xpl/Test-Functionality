import os
import json
import logging
import sys
from flask import Flask, Blueprint
from extensions import db
from set_config import SQLALCHEMY_DATABASE_URI
from models import base

logging.basicConfig(level=logging.DEBUG)

logging.info('------ Github Action Execution Started -------')

GITHUB_EVENT_PATH = os.getenv('GITHUB_EVENT_PATH')

event = {}

if GITHUB_EVENT_PATH and os.path.exists(GITHUB_EVENT_PATH):
    with open(GITHUB_EVENT_PATH, 'r') as f:
        event = json.load(f)
        event = event if event else {}

if not event:
    logging.error('FAILED : Could not find github event path')
    sys.exit(0)


def createApp():
    app = Flask(__name__)
    logging.info(SQLALCHEMY_DATABASE_URI)
    app.config.from_object('set_config')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

app = createApp()


def createModels():
    value = {
        'success':False
    }
    model = base.TestSuccess(**value)
    db.session.add(model)
    db.session.commit()
    logging.info('----Model Data Success ------')
    
createModels()

logging.info('------ Github Action Execution Ended -------')
