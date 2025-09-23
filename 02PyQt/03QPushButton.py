"""
    信号与槽:
    在Qt中，信号和槽机制是一种非常强大的事件通信机制，这是一个重要概念，特别是对于初学者来说，理解它对于
    编写QT程序至关重要。
    信号（signals)  是由对象在特定事件发生时发出的消息，例如，QPushButton有一个c1icked()信号，当用户点击按钮时发出。
    槽(Slots) : 是用来响应信号的方法。一个槽可以是任何函数，当其关联的信号被发出时，该槽函数将被调用。
    连接信号和槽:  使用Qobject::connect(O方法将信号连接到惜。当信号发出时，关联的槽函数会自动执行，
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class mainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.ui_init()
    def ui_init(self):
        registerBtn = QPushButton(self)
        registerBtn.setText("注  册")
        registerBtn.resize(350,80)
        registerBtn.move(100,100)

        """设置样式"""
        registerBtn.setStyleSheet("""
                QPushButton{
                        background: #1D83D4;  /*设置背景颜色*/
                        color : white;   /*设置文字颜色*/
                        font-size :20px;
                        font-weight : bold;
                        border-radius  : 15px ; /*设置边框圆角*/ 
                }
                QPushButton:hover{
                        background: #229AFA;  /*设置背景颜色*/
                }
                QPushButton:pressed{
                        background: #1D83D4;  /*设置背景颜色*/
                        padding-left  : 10px;  /*按钮按下时微调内边距 实现文字下压效果*/
                        padding-top  : 10px;  
                }
                QPushButton:disabled{
                        background: gray;  /*设置背景颜色*/
                        
                }
        """)

        registerBtn.clicked.connect(self.register) #将 clicked信号和register槽函数绑定在一起

        # registerBtn.setEnabled(False)  # 启用或者禁用按钮状态

    def register(self):
        print("注册功能")


if __name__ == '__main__':
    app  = QApplication(sys.argv)
    window = mainWidget()
    window.show()
    sys.exit(app.exec_())