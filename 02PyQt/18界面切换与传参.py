
"""
PyQt界面切换
            界面切换之后的界面大部分情况为一下两种:
                                                QWidget界面        只能有一个界面显示
                                                QDialog界面        两个界面同时显示，但只有对话框界面可以交互

            传参方式：
                    1、通过对象传参
                    2、通过信号量传参
                                        发送信号    pyqtSignal::emit
                                        接收信号    pyqtSignal::connect
"""
import requests
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton
import sys

#  导入界面
from registerDialog import RegisterDialog
from homeWidget import HomeWidget

class MySingal(QObject):
    # 定义信号 可以传递两个字符串参数和一个整形参数
    my_signal = pyqtSignal(str,str,int)


"""常用创建窗口的方式"""
# 继承QWidget类所有的属性和方法
class mainWidget(QWidget):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("界面切换与传参")
        # 修改窗口大小
        self.resize(300, 300)

        # 创建信号实例
        self.signal =  MySingal()


        mainLayout = QVBoxLayout(self)
        self.usernameEdit = QLineEdit()
        self.passwordEdit = QLineEdit()

        mainLayout.addWidget(self.usernameEdit)
        mainLayout.addWidget(self.passwordEdit)

        btn1 = QPushButton("登录")
        btn1.clicked.connect(self.login_slot)
        btn2 =QPushButton("注册")
        btn2.clicked.connect(self.register_slot)
        btn3 =QPushButton("退出")
        mainLayout.addWidget(btn1)
        mainLayout.addWidget(btn2)
        mainLayout.addWidget(btn3)

        """子界面初始化"""

    def register_slot(self):
        # 创建注册对话框界面
        self.registerDialog = RegisterDialog(self)
        res =  self.registerDialog.exec_()  # 阻塞等待用户关闭，并返回窗口结果
        print("注册界面返回值:",res)


    def login_slot(self):

        """通过信号量传参"""
        """通过对象传参"""
        username =  self.usernameEdit.text()
        password  = self.passwordEdit.text()

        param1 = {"username": username, "password": password}

        response =  requests.post(f"http://127.0.0.1:8080/auth/login",json = param1)
        print(response.json())
        if response.status_code == 200:
            print("登录成功")
            self.close()  # 关闭登录界面
            self.HomeWidget = HomeWidget(self, {"username": username, "email": "321312@qq.com"})

            self.HomeWidget.show()  # 显示首页界面
            self.signal.my_signal.emit("pg", "pg@qq.com", 1)  # 发送信号
        else:
            print("登录失败")
            self.usernameEdit.clear()
            self.passwordEdit.clear()



if __name__ == '__main__':
    """程序启动的基本流程"""
    # 创建qApplication类   sys.argv为了通过命令行传参，但是大部分场景已经不在需要
    # print(sys.argv)
    app = QApplication(sys.argv)
    # 创建窗口对象 QWidget为UI界面
    window =  mainWidget()
    # 显示窗口
    window.show()
    # 程序关闭之后自动释放资源
    sys.exit(app.exec_())


