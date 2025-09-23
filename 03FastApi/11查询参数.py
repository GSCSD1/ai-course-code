"""
    查询参数 ： 用于传递额外信息的参数
    通常出现在url路径后面，以?开头，格式为key=value ，多个参数用&连接
    常用于过滤、排序或指定请求的附加条件，而不是直接表示资源本身。

"""
import uvicorn
from fastapi import FastAPI

# 用于在代码中说明变量或者函数参数的类型
from typing import Union,Optional

app = FastAPI()

# 构建查询参数  gj:Union[str,None] 为可选参数 ,可填可不填
@app.get('/jobs')
def get_jobs(zl:int,xl:Union[int,str]="本科",gj:Union[str,None]=None):
    print(type(xl))
    return{
        "zl":zl,  # 工作种类
        "xl":xl,  # 学历
        "gj":gj   # 工作岗位
    }

if __name__ == "__main__":
    uvicorn.run(
        app,   # 应用实例
        host='0.0.0.0', # 监听地址{"method":"get方法"}
        port=8080,   # 监听端口
        log_level="debug"  # 日志级别
    )