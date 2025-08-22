# FastAPI REST API 作业起始代码

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 示例数据模型
class Item(BaseModel):
    name: str
    description: str = None

items = {}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return items.get(item_id, {"error": "Item not found"})

@app.post("/items/")
def create_item(item_id: int, item: Item):
    items[item_id] = item.dict()
    return items[item_id]

# 更多接口和功能请根据作业要求补充
