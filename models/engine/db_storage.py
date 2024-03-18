
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """ create tables"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query data"""
        obj = {}
        if cls:
            query = self.__session.query(eval(cls))
            for val in query:
                key = "{}.{}".format(type(val).__name__, val.id)
                obj[key] = val

        else:
            classes = ['State', 'City', 'User', 'Place', 'Review', 'Amenity']
            for cl in classes:
                query = self.__session.query(cl)
                for val in query:
                    key = "{}.{}".format(type(val).__name__, val.id)
                    obj[key] = val
        return (obj)
    
    def new(self, obj): 
        """add new element to table"""
        self.__session.add(obj)

    def save(self):
        """commit changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete element from table
        """
        if obj:
            self.session.delete(obj)
    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)