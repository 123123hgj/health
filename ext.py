from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
#初始化db,将命名惯例naming_convention传给SQL_Alchemy,解决“ValueError: Constraint must have a name"的问题
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))

login_manager = LoginManager()
bcrypt = Bcrypt()