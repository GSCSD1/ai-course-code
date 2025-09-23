import os

from fastapi import APIRouter
import json
import  aiofiles
# 创建子路由
router = APIRouter()

@router.get("/products")
async def read_products():
    """
        通过get方法实现获取所有商品属性
    """
    products = []
    with aiofiles.open(r'C:\Users\33122\Desktop\2507Code\03FastApi\db\products.txt','rt',encoding='utf-8') as f:
       async for line in f:
            if line == '\n':
                continue
            products.append(json.loads(line))
            print(line)

    print(products)
    return products


@router.get("/music")
def read_musicList():
    """
            通过get方法获取所有音乐名
    """
    file = os.listdir(r"C:\Users\33122\Desktop\2507Code\03FastApi\music")
    musicList = [  name for name in file if name.endswith(".mp3") ]
    print(musicList)

    return "read_musicList test"
