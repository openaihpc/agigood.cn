from configs import dify_config
from dify_app import CASGVApp


def init_app(app: CASGVApp):
    app.secret_key = dify_config.SECRET_KEY
