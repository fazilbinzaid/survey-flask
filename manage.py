import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# custom imports
from settings import CONFIG
from src.app import app, db

app.config.from_object(CONFIG)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
