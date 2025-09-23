

"""
    只有get方法没有请求体参数，其余都有该参数
    请求体参数 ： 传递结构化 大容量 或复杂的数据
    pydantic  一般用于请求体参数

     练习 ： 创建商品信息   在products路径下通过请求体参数将商品信息写入到文件
"""
import uvicorn
from fastapi import FastAPI,HTTPException
from typing import Union,Optional
from pydantic import BaseModel,Field  # BaseModel主要用于数据验证 Field用于定义额外的验证规则
from PyQt5.QtSql import QSqlQuery,QSqlDatabase



class MysqlLite:
    def __init__(self):
        """
            连接数据库
        """
        try:
                 # 创建数据库连接
                self.database = QSqlDatabase.addDatabase('QSQLITE')
                 # 设置数据库名称
                self.database.setDatabaseName("user.db")
                # 连接数据库
                self.database.open()
        except Exception as e:
            print("无法连接数据库",e)

    def operation_sql(self,sql):
        """
            执行sql语句
        """
        # 创建查询对象
        self.query = QSqlQuery()
        # 执行sql语句
        self.query.exec_(sql)

    def selectData(self, sql):
        self.operation_sql(sql)
        # 获取查询到的数据   record()返回一个QSqlRecord对象 包含查询结果的字段数量 字段名信息
        self.result = self.query.record()
        print(self.result)

        while self.query.next():  # 遍历每一行的数据
            for i in range(self.result.count()):
                print(self.query.value(i), end=" ")
            print()

app = FastAPI()


class RegisterRquest(BaseModel):
    username:str
    email:str =Field(pattern="^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$")
    password:str
    is_admin:int = Field(default=0,ge=0,le=1)  # 0普通用户 1管理员


# 用户注册
@app.post("/auth/register")
def register(request:RegisterRquest):
    # 创建数据库连接
    my_sqlite = MysqlLite()
    # 判断用户名是否已经存在
    print(request.username)
    my_sqlite.operation_sql("select * from user_info")
    my_sqlite.query.record()
    while my_sqlite.query.next():  # 遍历每一行的数据
        print("每一行数据")
        if my_sqlite.query.value(1) == request.username:  # 判断用户名是否在数据库中
            print(my_sqlite.query.value(1))
            raise HTTPException(status_code=400, detail="用户名已存在")
        if my_sqlite.query.value(2) == request.email:  # 判断用户名是否在数据库中
            print(my_sqlite.query.value(2))
            raise HTTPException(status_code=400, detail="邮箱已存在")

    username = request.username
    email = request.email
    password = request.password
    is_admin = request.is_admin

    my_sqlite.operation_sql(f"insert into user_info values(null,'{username}','{email}','{password}',{is_admin})")

    return {
              "msg"  : "注册成功",
              "data" : request.model_dump()
    }


class LoginRquest(BaseModel):
    username:str
    password:str

# 用户登录
@app.post("/auth/login")
def login(request:LoginRquest):
    # 创建数据库连接
    my_sqlite = MysqlLite()
    my_sqlite.operation_sql("select * from user_info")
    my_sqlite.query.record()
    while my_sqlite.query.next():  # 遍历每一行的数据
        if my_sqlite.query.value(1) == request.username and my_sqlite.query.value(3) == request.password:  # 判断用户名是否在数据库中
            break
    else:  # 没有找到用户名
        raise  HTTPException(status_code=400, detail="登录失败")

    return {
        "msg": "登录成功",
        "data": request.model_dump()
    }


if __name__ == "__main__":
    uvicorn.run(
        app,   # 应用实例
        host='0.0.0.0', # 监听地址{"method":"get方法"}
        port=8080,   # 监听端口
        log_level="debug"  # 日志级别
    )
