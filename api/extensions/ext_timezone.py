import os
import time

from dify_app import CASGVApp


def init_app(app: CASGVApp):
    os.environ["TZ"] = "UTC"
    # windows platform not support tzset
    if hasattr(time, "tzset"):
        time.tzset()
