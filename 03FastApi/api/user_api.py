import json

from fastapi import APIRouter

# 创建子路由
router = APIRouter()

@router.get('/users')
def read_users():
    users = []
    with open(r'C:\Users\33122\Desktop\2507Code\03FastApi\db\user.txt', 'rt', encoding='utf-8') as f:
        for line in f:
            if line == '\n':
                continue
            users.append(json.loads(line))
            print(line)
    print(users)
    return users

@router.get('/auth/login/')
def login():
    return "login test"

@router.get('/auth/register/')
def register():
    return "register test"