# When sending data from client to your API you'll need a request body
# When receiving data from API you'll receive it with a response body

# API has to send a response body. But clients doesn't necesarrily have to send a request body.
# To declare a request body you'll need Pydantic models
# its a data validation and management library that uses Python type annotation

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

# Data Model
# Description and Tax are optional thus, None.
# Validate data and return errors
class Item(BaseModel):
    name: str
    description: Union[str, None] = None # None to make it optional
    price:float
    tax: Union[float, None] = None

app = FastAPI()

@app.post("/items/{items_id}") #path operation
async def create_item(items_id: int, item: Item): #Item is the type
    return {"item_id":items_id, **item.dict()}