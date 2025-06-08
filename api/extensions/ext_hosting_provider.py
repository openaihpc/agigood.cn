from core.hosting_configuration import HostingConfiguration

hosting_configuration = HostingConfiguration()


from dify_app import CASGVApp


def init_app(app: CASGVApp):
    hosting_configuration.init_app(app)
