from dify_app import CASGVApp
from models import db


def init_app(app: CASGVApp):
    db.init_app(app)
