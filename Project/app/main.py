from random import randrange
from typing import Union
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

my_posts = [{"title":"First Post", "content":"This is the first post", "id":1}, {"title":"Second Post", "content":"This is the second post", "id":2}]

# Function to get single post
def get_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

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
    post = get_post(id)
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