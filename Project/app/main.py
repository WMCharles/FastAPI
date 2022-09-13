from random import randrange
from typing import Union
from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor # gives column name and values
import time

app = FastAPI()

my_posts = [{"title":"First Post", "content":"This is the first post", "id":1}, {"title":"Second Post", "content":"This is the second post", "id":2}]

# Connecting to database using Psycopg2

while True:
    try:
        conn = psycopg2.connect(host='192.168.43.163', dbname='test', user="charles", password='Access', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Connection was successful!")
        break
    except Exception as error:
        print("Connection to database failed!")
        print("Error ", error)
        time.sleep(2)

# Function to get single post
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

# Function to get single post & update
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

class Post(BaseModel):
    title:str
    content: Union[str, None] = None

# Base url
@app.get("/")
def root():
    return {"message":"Hello Welcome"}

# Retrieving all posts
@app.get("/posts")
def get_posts():
    return {"message": my_posts}

# Retrieving single post
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with {id} not found!")
    return {"post": post}

# Create Post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0,100)
    my_posts.append(post_dict)
    print(post_dict)
    return {"message": post_dict}

# Update Post
@app.put("/posts/{id}", status_code=status.HTTP_201_CREATED)
def update_post(id: int, post: Post):
    post_dict = post.dict()
    post_dict["id"] = id
    index = find_index_post(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found!")
    my_posts[index] = post_dict

    return {"message": post_dict}

# Delete Post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found!")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)