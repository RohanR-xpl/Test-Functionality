import os
import json
import logging
import sys
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from set_config import SQLALCHEMY_DATABASE_URI

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
    db = SQLAlchemy()
    logging.info(SQLALCHEMY_DATABASE_URI)
    db.init_app(app)
    app.config.from_object('set_config')
    logging.info(app.config)
    return app

createApp()

logging.info('------ Github Action Execution Ended -------')
