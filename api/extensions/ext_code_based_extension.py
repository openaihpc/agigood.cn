from core.extension.extension import Extension
from dify_app import CASGVApp


def init_app(app: CASGVApp):
    code_based_extension.init()


code_based_extension = Extension()
