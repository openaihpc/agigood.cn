from dify_app import CASGVApp


def init_app(app: CASGVApp):
    import flask_migrate  # type: ignore

    from extensions.ext_database import db

    flask_migrate.Migrate(app, db)
