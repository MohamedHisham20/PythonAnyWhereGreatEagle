from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager

from database import db


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
    app.config["SECRET_KEY"] = "SECRET_KEY"
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="MohamedHisham1",
    password="UDareC0meHere",
    hostname="MohamedHisham1.mysql.pythonanywhere-services.com",
    databasename="MohamedHisham1$GreatEagle")
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    CORS(app, support_credentials=True)

    from Login import login
    from Register import register
    app.register_blueprint(login)
    app.register_blueprint(register)

    db.init_app(app)

    return app

app = create_app()

login_manager = LoginManager(app)
login_manager.login_view = 'login'
@app.route("/")
def welcome_page():
    return "<h1> Welcome </h1>"


if __name__ == '__main__':
    app.run(debug=True)


