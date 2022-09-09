from fastapi import FastAPI # FastAPI python class that provides all the functionality for ur API

app = FastAPI() 
#creating an instance of FastAPI
#main point of interaction of your API


@app.get("/") #get request
async def root():
    return {"message": "Hello World"} #returns a dictionary3
