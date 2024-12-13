from sqlalchemy import Column, Integer, String, Float, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

# Base declarativa para los modelos SQLAlchemy
Base = declarative_base()

# Modelo SQLAlchemy para la tabla `posts`
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False)
    color = Column(String(7), nullable=False)
    neg = Column(Float, nullable=False)
    neu = Column(Float, nullable=False)
    pos = Column(Float, nullable=False)
    added_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return (
            f"<PostModel(id={self.id}, content={self.content[:30]}, color={self.color}, "
            f"neg={self.neg}, neu={self.neu}, pos={self.pos}, added_at={self.added_at})>"
        )
