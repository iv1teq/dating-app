import flask
import os
# from flask_sqlalchemy import SQLAlchemy


app = flask.Flask(
    import_name = "app",
    static_folder = "static",
    static_url_path = "/static",
    template_folder = "templates",
    instance_path = os.path.abspath(os.path.join(__file__, "..", "instance"))
)


# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)



# Создание модели данных (таблицы)
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return f'<User {self.username}>'




# Создание файла БД:
# Запустите Python в терминале и создайте таблицы:
# python
# from app import app, db, User
# with app.app_context():
#     db.create_all()