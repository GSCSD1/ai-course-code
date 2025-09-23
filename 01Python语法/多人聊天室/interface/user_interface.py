"""绝对路径"""
import sys
sys.path.append("..")
from db import db_handle


# from 多人聊天室.db import db_handle
# 相对路径导入  ..表示上一级路径  .表示当前路径
# from ..db import db_handle




def login(username,password):
    """
    用户登录接口
    :param username:
    :param password:
    :return: 返回登录是否成功
    """
    # 在数据库中查询用户名
    db_user,db_pwd =  db_handle.select_user(username)
    if db_user and db_pwd == password:
        return True
    else:
        return False