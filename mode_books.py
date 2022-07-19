from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/students")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Users(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    book_name = Column(String(24), default=None, nullable=False, comment="书籍名称")
    book_words = Column(Integer, default=None, nullable=False, comment="书籍字数")
    book_type = Column(String(24), default=None, nullable=False, comment="书籍种类")
    book_status = Column(String(24), default=None, nullable=False, comment="书籍状态")
    create_time = Column(DateTime)
    update_time = Column(DateTime)

    def __repr__(self):
        bId = self.book_id
        bName = self.book_name
        bWords = self.book_words
        bType = self.book_type
        bStatus = self.book_status
        cTime = self.create_time
        uTime = self.update_time
        return f"Books: book_id:{bId}," \
               f"book_name:{bName}," \
               f"book_words:{bWords}," \
               f"book_type:{bType}," \
               f"book_Status:{bStatus}," \
               f"create_time:{cTime}," \
               f"update_time:{uTime}"


Base.metadata.create_all(engine)

if __name__ == '__main__':
    print("查询全部")
    query_result = session.query(Users).all()
    for result in query_result:
        print(f"查询结果：{result}")