from fastapi import FastAPI

app = FastAPI()

fake_db = [{"item_name":"Foo"}, {"item_name":"Bar"}, {"item_name":"Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit:int = 10):
    return fake_db[skip: skip + limit]