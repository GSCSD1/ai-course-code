

# 查询用户名是否在文件库中，返回查询到的用户名和密码
def select_user(user):
    """
    :param user: 用户名
    :return:
    """
    db_User= None
    db_Passwd = None
    with open('./db/user.txt', 'r') as f:
        for line in f: # 读取每行文件中的账号和密码
            if user == line.split(':')[0]: # 判断账号
                db_User = user
                db_Passwd = line.split(':')[1].strip('\n')
                break
    return db_User, db_Passwd
