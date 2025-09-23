
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLineEdit,QPushButton
"""常用创建窗口的方式"""
# 继承QWidget类所有的属性和方法
class HomeWidget(QWidget):
    def __init__(self,parent=None,user_info:dict=None):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        self.user_info = user_info
        print("用户:",self.user_info)
        self.parent = parent
        # 修改窗口标题
        self.setWindowTitle("首页")
        # 修改窗口大小
        self.resize(800, 800)
        mainLayout = QVBoxLayout(self)
        btn1 =  QPushButton("返回登录界面")
        btn1.clicked.connect(self.home)
        mainLayout.addWidget(btn1)

        self.parent.signal.my_signal.connect(self.signal_slot)

    def signal_slot(self,username,email,age):
        print("HomeWidget:信号接收成功")
        print("HomeWidget:用户名:",username)
        print("HomeWidget:邮箱:",email)
        print("HomeWidget:年龄:",age)

    def home(self):
        if self.parent:
            self.close()
            self.parent.show()








