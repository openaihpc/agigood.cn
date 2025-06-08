from dify_app import CASGVApp


def init_app(app: CASGVApp):
    import warnings

    warnings.simplefilter("ignore", ResourceWarning)
