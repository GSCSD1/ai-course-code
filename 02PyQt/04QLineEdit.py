"""
    单行输入框
    lineEdit::setEchoMode   设置回显模式
        '''
            QLineEdit.Normal 正常输入模式
            QLineEdit.NoEcho ：不显示任何输入内容
            QLineEdit.Password ：以密文形式显示输入内容。
            QLineEdit.PasswordEchoOnEdit ：编辑时显示明文，失去焦点后显示密文。
        '''
        lineEdit::setValidator  设置验证器
        '''
            QIntValidator() :     整数验证器  只允许输入数字
            QDoubleValidator():   小数验证器  只允许输入小数
            QRegExpValidator()：   参数为QRegExp对象 正则验证器  匹配正则内容
        '''
"""
import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtWidgets import QApplication, QWidget,QLineEdit


# 继承QWidget类所有的属性和方法
class mainWidget(QWidget):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("单行编辑框使用")
        # 修改窗口大小
        self.resize(700, 700)
        self.ui_init()

    def ui_init(self):
        userNameEdit =  QLineEdit(self)
        passWordEdit = QLineEdit(self)
        userNameEdit.move(50,50)
        passWordEdit.move(50,150)
        userNameEdit.resize(300,40)
        passWordEdit.resize(300, 40)

        """编辑框样式设置"""
        editStyleSheet = """
        QLineEdit{
                border : 2px solid gray;   /*边框颜色是灰色 细宽为2px solid 实线  */
                border-radius: 15px;    /* 边框圆角弧度 ： 15px*/
                background-color: #F0F0F0;
                font-size:24px;
            }
            QLineEdit:hover{    /*鼠标悬停*/
                border-color:#44C1D6;  
                
            }
            QLineEdit:focus{   /*聚焦*/
               border-color:green;  
               background-color: white;;
                
            }
        """
        userNameEdit.setStyleSheet(editStyleSheet)
        passWordEdit.setStyleSheet(editStyleSheet)
        passWordEdit.setText("123")


        """占位符文本设置"""
        userNameEdit.setPlaceholderText("请输入账号或邮箱")
        passWordEdit.setPlaceholderText("请输入密码")

        """回显模式"""
        # passWordEdit.setEchoMode(QLineEdit.NoEcho) # 不显示任何输入内容
        passWordEdit.setEchoMode(QLineEdit.Password) # 密文形式显示
        # passWordEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)  #  编辑时显示明文，失去焦点后显示密文。

        """验证器"""
        # userNameEdit.setValidator(QIntValidator())
        # userNameEdit.setValidator(QDoubleValidator())
        # userNameEdit.setValidator(QRegExpValidator(QRegExp("[0-9a-z]+"))) # 正则验证器 只允许数字和小写字母

        """得到输入框的内容"""
        print("text:",userNameEdit.text())
        print("text:",passWordEdit.text())

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


