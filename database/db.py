from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import database.models as models


class Database:
    __url = 'postgresql+psycopg2://localhost:5432/materials_db'
    __engine = None
    __session = None
    __log_path = './log'

    @staticmethod
    def __log(message):
        with open(Database.__log_path, 'a') as logger:
            logger.write(f'{datetime.now()}: {message}\n')

    @staticmethod
    def init(drop_all=False):
        Database.__engine = create_engine(Database.__url)
        Database.__log('engine initialized')
        if drop_all:
            models.Base.metadata.drop_all(Database.__engine)
            Database.__log('tables are dropped')
        models.Base.metadata.create_all(Database.__engine)
        Database.__log('tables are created')
        Database.__session = sessionmaker(bind=Database.__engine)
        Database.__log('session object is initialized')

    @staticmethod
    def recreate_tables():
        if Database.__engine is None:
            Database.__log('failed to recreated tables - engine is not initialized')
            return
        models.Base.metadata.drop_all(Database.__engine)
        models.Base.metadata.create_all(Database.__engine)
        Database.__log('tables are successfully recreated')

    @staticmethod
    def get_session():
        if Database.__session is None:
            Database.__log('failed to create session - session object is not initialized')
            return None
        s = Database.__session()
        s.expire_on_commit = False
        return s


if __name__ == '__main__':
    print('Drop tables? [n]/y')
    drop = input()
    if drop == 'y':
        Database.init(drop_all=True)
    else:
        Database.init(drop_all=False)

    # s = Database.get_session()
    # if s is not None:
    #     s.add(models.Material(name='Physics. Principles with application',
    #                           authors='Douglas C. Giancoli',
    #                           edition=7))
    #     s.commit()
    #     s.close()
