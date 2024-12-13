from fastapi import FastAPI, HTTPException, Request, Depends
from analyzer import sentiment_analysis as sa
from analyzer import sentiment_color as sc
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from cors import add_cors_middleware
from crud import *
from database import get_db
from models.PostSchema import PostSchema
import models.TextInput as ti
from models.models import Post
from sqlalchemy.orm import Session

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()

add_cors_middleware(app)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, lambda req, exc: HTTPException(429, "Rate limit exceeded"))

analyzer = sa.SentimentAnalyzer()

# CRUD Endpoints
@app.post("/posts/")
def api_create_post(post: PostSchema, db: Session = Depends(get_db)):
    new_post = create_post(db, post.content, post.color, post.neg, post.neu, post.pos)
    return new_post

@app.get("/posts/")
def api_get_posts(db: Session = Depends(get_db)):
    return get_posts(db)

@app.get("/posts/{post_id}")
def api_get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    post = get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.put("/posts/{post_id}")
def api_update_post(post_id: int, content: str, color: str, neg: float, neu: float, pos: float, db: Session = Depends(get_db)):
    post = update_post(db, post_id, content, color, neg, neu, pos)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.delete("/posts/{post_id}")
def api_delete_post(post_id: int, db: Session = Depends(get_db)):
    success = delete_post(db, post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Post deleted"}

# Analyzer Endpoint
@app.post("/analyze/")
@limiter.limit("20/second")
async def analyze_text(input: ti.TextInput, request: Request):
    try:
        resultados = analyzer.analyze(input.text)
        color = sc.mezclar_colores(resultados)
        return {
            "text": input.text,
            "sentiment": resultados,
            "color": color
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
