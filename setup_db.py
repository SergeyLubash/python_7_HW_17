from flask_sqlalchemy import SQLAlchemy

# Создаем объект алхимии, который будут использовать все:
# и модели
# и приложение
# и блупринты

db = SQLAlchemy()