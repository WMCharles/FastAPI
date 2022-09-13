from random import randrange
from typing import Union
from fastapi import FastAPI, status, HTTPException, Response, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor # gives column name and values
import time
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Connecting to database using Psycopg2

while True:
    try:
        conn = psycopg2.connect(host='192.168.43.163', dbname='fastapi', user="charles", password='Access', cursor_factory=RealDictCursor)
        cursor = conn.cursor() #enables us to do database operations
        print("DB Connection was successful!")
        break
    except Exception as error:
        print("Connection to database failed!")
        print("Error ", error)
        time.sleep(2)

class Post(BaseModel):
    title:str
    content: Union[str, None] = None
    published: bool = True

# Base url
@app.get("/")
def root():
    return {"message":"Hello Welcome"}

# Retrieving all posts
@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return {"Posts": posts}

# Retrieving single post
@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", [str(id)],)
    # post = cursor.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} not found!")
    return {"post": post}

# Create Post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
    # post = cursor.fetchone()
    # conn.commit()

    # post = models.Post(title=post.title, content=post.content, published=post.published)
    post = models.Post(**post.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return {"message": post}

# Update Post
@app.put("/posts/{id}", status_code=status.HTTP_201_CREATED)
def update_post(id: int, post: Post, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title =%s, content=%s WHERE id=%s RETURNING *""", (post.title, post.content, str(id)))
    # post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    update_post = post_query.first()

    if not update_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} not found!")

    post_query.update(post.dict(), synchronize_session=False)
    db.commit()


    return {"post": post_query.first()}

# Delete Post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", [str(id)])
    # post = cursor.fetchone()
    # conn.commit()

    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} not found!")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)