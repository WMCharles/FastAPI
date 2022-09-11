from fastapi import FastAPI

app = FastAPI()

my_posts = [{"title":"First Post", "content":"This is the first post", "id":1}, {"title":"Second Post", "content":"This is the second post", "id":2}]

# Base url
@app.get("/")
def root():
    return {"message":"Hello Welcome"}

# Retrieving posts
@app.get("/posts")
def get_posts():
    return {"message": my_posts}