from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/students")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(32), default=None, nullable=False, comment="用户姓名")
    user_password = Column(String(16), default=None, nullable=False, comment="用户密码")
    book_id = Column(Integer)
    user_type = Column(Integer, default=None, nullable=False, comment="用户种类")
    create_time = Column(DateTime)
    update_time = Column(DateTime)

    def __repr__(self):
        uId = self.user_id
        uName = self.user_name
        uPsd = self.user_password
        bId = self.book_id
        uType = self.user_type
        cTime = self.create_time
        uTime = self.update_time
        return f"User: user_id:{uId}, " \
               f"user_name:{uName}, " \
               f"password:{uPsd}, " \
               f"book_id:{bId}," \
               f"user_type:{uType}," \
               f"create_time:{cTime}," \
               f"update_time:{uTime}"


Base.metadata.create_all(engine)

def check(name, psd):
    check_result = session.query(Users).filter(Users.user_name == name, Users.user_password == psd).first()
    return check_result


if __name__ == '__main__':
    print("查询全部")
    query_result = session.query(Users).all()
    for result in query_result:
        print(f"查询结果：{result}")
    # check_result = session.query(Users).filter(Users.user_name == 'admin', Users.user_password == "11111").first()
    # print(check_result)
    a = check("admin", "11111")
    print(a)





