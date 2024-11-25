from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "HJGSHJS*&&*@#@&HSJAGDHJDHJFD"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/qlhtks?charset=utf8mb4" % quote('Tien@151103')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8 # 1 trang co 8 san pham

db = SQLAlchemy(app)
login = LoginManager(app=app)