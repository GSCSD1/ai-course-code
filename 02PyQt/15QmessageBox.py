"""
在 PyQt5 中， QMessageBox 是一个非常常用的类，用于显示消息框。它通常用于向用户显示信息、警告、错误或询问用户的选择。 QMessageBox 是一个模态对话框，
意味着在用户关闭消息框之前，应用程序的其他部分无法与用户交互。
QMessageBox 的主要作用是通过弹出消息框与用户进行交互。它可以用于以下场景：
关于对话框
显示信息对话框：如操作成功、操作失败等提示信息。
显示警告对话框：如用户输入无效、文件不存在等警告信息。
显示错误对话框：如程序运行时发生错误。
显示提问对话框：如确认删除、确认退出等操作。
"""
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox
import sys


"""常用创建窗口的方式"""
# 继承QWidget类所有的属性和方法
class mainWidget(QWidget):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("消息框的使用")
        # 修改窗口大小
        self.resize(500, 500)

        mainLayout = QVBoxLayout(self)


        self.buttons = [] # 存储所有的按钮对象
        for text in ["关于对话框","显示消息对话框","显示错误对话框","显示警告对话框","显示提问对话框"]:
            self.buttons.append(QPushButton(text))  # 存储按钮对象
            mainLayout.addWidget(self.buttons[-1])  # 将按钮加入到布局

        """绑定槽函数"""
        for button in self.buttons:

            button.clicked.connect(self.showDialog)

    def showDialog(self):
        text =  self.sender().text()
        if text in  "关于对话框":  # 第一个参数为标题  第二个参数为内容
            QMessageBox.about(None,"关于对话框","这是关于对话框")
            # print("关于对话框功能")
        elif text  in  "显示消息对话框":
            QMessageBox.information(None,"消息","这是消息对话框")
        elif text  in  "显示错误对话框":
            QMessageBox.critical(None,"错误","这是错误对话框")
        elif text in "显示警告对话框":  # 第三个参数表示有哪些选项  第四个参数为默认选择
           ret =  QMessageBox.warning(None, "警告", "这是警告对话框", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
           if ret == QMessageBox.Yes:
               print("用户选择了YES")
           else :
               print("用户选择了No")
        elif text in "显示提问对话框":
            ret = QMessageBox.question(None, "提问", "这是提问对话框", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if ret == QMessageBox.Yes:
                print("用户选择了YES")
            else:
                print("用户选择了No")

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

