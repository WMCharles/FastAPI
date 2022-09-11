from random import randrange
from typing import Union
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

my_posts = [{"title":"First Post", "content":"This is the first post", "id":1}, {"title":"Second Post", "content":"This is the second post", "id":2}]

class Post(BaseModel):
    title:str
    content: Union[str, None] = None

# Base url
@app.get("/")
def root():
    return {"message":"Hello Welcome"}

# Retrieving posts
@app.get("/posts")
def get_posts():
    return {"message": my_posts}

# Create Post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0,100)
    my_posts.append(post_dict)
    print(post_dict)
    return {"message": post_dict}