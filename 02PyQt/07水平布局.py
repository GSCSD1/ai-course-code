"""
    水平布局 QHBoxLayout ： 控件从左向右排列  默认情况为等间距

            addWidget :  将控件加入到布局中
            addLayout :  将子布局加入到布局中
            addSpacing:  为布局添加空隙
            setStretch ： 设置控件伸缩比例
            setContentsMargins : 设置内边距  左上右下
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QPushButton
import sys


# 继承QWidget类所有的属性和方法
class mainWidget(QWidget):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("水平布局使用")
        # 修改窗口大小
        self.resize(800, 800)
        self.ui_init()

    def ui_init(self):
        # 创建水平布局
        mainLayout = QHBoxLayout()

        # 创建按钮
        btn1 =  QPushButton(text="按钮1")
        btn2 = QPushButton(text="按钮2")
        btn3 = QPushButton(text="按钮3")

        # 将控件加入布局
        mainLayout.addWidget(btn1)
        mainLayout.addWidget(btn2)
        # 为布局添加空隙
        mainLayout.addSpacing(50)
        mainLayout.addWidget(btn3)


        # 设置伸缩比例
        mainLayout.setStretch(0, 2)
        mainLayout.setStretch(1, 1)
        mainLayout.setStretch(3, 3)


        # 设置内边距  左上右下
        # mainLayout.setContentsMargins(10,100,30,30)

        # 设置对齐方式  Qt.AlignTop 顶对齐   Qt.AlignTop 底对齐
        mainLayout.setAlignment(Qt.AlignTop)


        # 将布局加入到主控件中
        self.setLayout(mainLayout)

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

