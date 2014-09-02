from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DatabaseConnection:
    def __init__(self, username, password, database):
        self.username = username
        self.password = password
        self.database_name = database

    def connect(self, base, *args, **kwargs):
        connection_template = "postgresql://{user}:{pwd}@localhost/{db}"
        connection_str = connection_template.format(
            user=self.username,
            pwd=self.password,
            db=self.database_name)

        self.engine = create_engine(connection_str, *args, **kwargs)
        base.metadata.create_all(self.engine)
        self.sessionmaker = sessionmaker(bind=self.engine)

    def session(self):
        return self.sessionmaker()

    @classmethod
    def from_config(cls, margot_config):
        username = margot_config['postgres']['username']
        password = margot_config['postgres']['password']
        database = margot_config['postgres']['database_name']
        return cls(username, password, database)


Base = declarative_base()
