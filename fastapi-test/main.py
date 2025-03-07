from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
import asyncio

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    description: Union[str, None] = None

@app.get("/")
def read_root():
    return {"message": "FastAPIのサンプルです"}

@app.post("/items/")
def create_item(item: Item):
    print(f"データを登録します：{item.name},{item.price},{item.description}")
    return item

@app.get("/sleep_time/")
async def sleep_time(sec: int):
    await asyncio.sleep(sec)
    return {"message": f"{sec}秒"}
