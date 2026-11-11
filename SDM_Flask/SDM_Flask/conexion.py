from flask_mysqldb import MySQL


class ConexionDB:
    def __init__(self, app):
        self.mysql = MySQL()
        self.init_app(app)

    def init_app(self, app):
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = ''
        app.config['MYSQL_DB'] = 'sebastian'
        app.config['MYSQL_PORT'] = 3306
        self.mysql.init_app(app)
