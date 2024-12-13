from sqlalchemy.orm import Session
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
            f"<Post(id={self.id}, content={self.content[:30]}, color={self.color}, "
            f"neg={self.neg}, neu={self.neu}, pos={self.pos}, added_at={self.added_at})>"
        )


# Crear un nuevo post
def create_post(db: Session, content: str, color: str, neg: float, neu: float, pos: float) -> Post:
    new_post = Post(content=content, color=color, neg=neg, neu=neu, pos=pos)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# Obtener todos los posts
def get_posts(db: Session) -> list[Post]:
    return db.query(Post).all()

# Obtener un post por ID
def get_post_by_id(db: Session, post_id: int) -> Post | None:
    return db.query(Post).filter(Post.id == post_id).first()

# Actualizar un post
def update_post(db: Session, post_id: int, content: str, color: str, neg: float, neu: float, pos: float) -> Post | None:
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.content = content
        post.color = color
        post.neg = neg
        post.neu = neu
        post.pos = pos
        db.commit()
        db.refresh(post)
        return post
    return None

# Eliminar un post
def delete_post(db: Session, post_id: int) -> bool:
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
        return True
    return False
