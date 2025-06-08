from dify_app import CASGVApp


def init_app(app: CASGVApp):
    from events import event_handlers  # noqa: F401
