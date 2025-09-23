
"""
    路径参数(在路径里面设置参数)
    编写接口 ：    http://ip:port/products/{product_id}  获取单个商品详情信息
    例如 ； http://ip:port/products/1 获取编号为1的商品详情信息
"""
import uvicorn
from fastapi import FastAPI

app = FastAPI()

# 路由匹配优先级  从上到下
@app.get('/user/1')
def get_user():
    return {'id_1':1}

@app.get('/user/{id}')
def get_user(id:int):
    return {'id_2':id}

# @app.get('/user/{username}')  # 不建议这种写法 会导致报错且容易混淆
# def get_user(username:str):
#     return {'id_3':username}



if __name__ == "__main__":
    uvicorn.run(
        app,   # 应用实例
        host='0.0.0.0', # 监听地址{"method":"get方法"}
        port=8080,   # 监听端口
        log_level="debug"  # 日志级别
    )



