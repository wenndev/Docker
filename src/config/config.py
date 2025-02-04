from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# classes de conexão


class DBConnection:

    def __init__(self) -> None:
        self.__connection_string = "mysql+pymysql://root:dell@mysqldb/teste"
        self.session = None

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        return self

    def __exit__(self, exc_type, exc_value, trace):
        self.session.close()
