
from PyQt5.QtWidgets import QDialog,QVBoxLayout,QLineEdit,QPushButton
"""常用创建窗口的方式"""
# 继承QWidget类所有的属性和方法
class RegisterDialog(QDialog):
    def __init__(self,parent= None):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__(parent)  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("创建新账号")
        # 修改窗口大小
        self.resize(800, 800)
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(QLineEdit())
        mainLayout.addWidget(QLineEdit())
        btn1 =  QPushButton("创建账号")
        btn1.clicked.connect(self.register)
        mainLayout.addWidget(btn1)
        mainLayout.addWidget(QPushButton("取消"))

    def register(self):
        self.close()
        print("注册成功")
        self.accept()


    def accept(self):
        super().accept()



