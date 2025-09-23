"""
    restful 规范  增 POST   删DELETE  改PUT  查GET

    练习 ： 通过get方法实现获取所有商品属性      shoplist
           通过get方法实现获取所有用户的属性    users
           通过get方法实现获取所有歌名         musiclist
"""
from fastapi import FastAPI
import uvicorn
# 创建fastapi应用实例
app = FastAPI()

# 定义GET方法的路由 路径为/get ,访问时返回json响应
@app.get('/get')
def get_test():
    return {"method":"get方法"}
@app.post(
            '/post',
            tags = ["这是post测试接口"],
            summary="this is post测试 summary",
            description="this is post测试 description",
            response_description="this is post测试 response_description....",
            deprecated= False)  # 标记接口是否废弃 ， false表示为废弃
def post_test():
    return {"method":"post方法"}

@app.put('/put')
def put_test():
    return {"method":"put方法"}

@app.delete('/delete')
def delete_test():
    return {"method":"delete方法"}

if __name__ == "__main__":
    uvicorn.run(
        app,   # 应用实例
        host='0.0.0.0', # 监听地址{"method":"get方法"}
        port=8080,   # 监听端口
        log_level="debug"  # 日志级别
    )


