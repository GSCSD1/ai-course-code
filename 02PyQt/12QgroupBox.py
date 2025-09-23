
"""
    组合框： 提供一个带有标题的边框容器，将相关控件组合在一起，使界面结构更清晰

    支持设置一个可选的复选框或单选按钮作为组的开关，控制整个组内控件的启用状态
"""
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout, QGroupBox, QPushButton
import sys

"""常用创建窗口的方式"""

class mainWidget(QWidget):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("带开关的QGroupBox")
        # 修改窗口大小
        self.resize(400, 300)
        mainLayout = QVBoxLayout(self)
        self.ui_init(mainLayout)

    def ui_init(self,layout):
        groupBox1 = QGroupBox('权限设置')
        groupBox1.setCheckable(True)  # 启用开关功能
        layout.addWidget(groupBox1)

        # 创建垂直布局
        group_layout =  QVBoxLayout()

        group_layout.addWidget(QCheckBox("允许修改资料"))
        group_layout.addWidget(QCheckBox("允许查看历史"))
        group_layout.addWidget(QPushButton("只读权限"))
        group_layout.addWidget(QPushButton("编辑权限"))

        groupBox1.setLayout(group_layout)

        groupBox1.toggled.connect(self.on_group_toggled)


    def on_group_toggled(self):
        print("<UNK>")



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
