import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHanlder:
    def __init__(self) -> None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, '..', '..', '..', '..'))
        db_path = os.path.join(project_root, 'storage.db')

        self.__connection_string = f'sqlite:///{db_path}'
        self.__engine = None
        self.session = None

    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()

        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


db_connection_handler = DBConnectionHanlder()
