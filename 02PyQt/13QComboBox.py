"""
    下拉框 / 组合框
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox,QHBoxLayout,QLabel

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
        mainLayout = QHBoxLayout(self)  # 水平
        self.ui_init(mainLayout)

    def ui_init(self,layout):

        layout.addWidget(QLabel("模型:"))

        self.combo =   QComboBox()

        layout.addWidget(self.combo)

        # 对下拉框增加条目
        self.combo.addItem("YOLOv5")
        self.combo.addItem("YOLOv6")
        self.combo.addItem("YOLOv7")
        self.combo.addItem("YOLOv8")

        """样式设置"""
        self.combo.setStyleSheet("""
            QComboBox{
                background-color:black;
                color:white;
                font-size:20px;
                padding:10px;
                border-radius:10px;
                border:5px solid gray;
                }
            QComboBox:hover{  
                border:5px solid red;
            }
            QComboBox:on{   /*下拉菜单打开状态*/
                border:5px solid green;
                font-size:50px;
                selection-background-color:red;  
            }
            /* 下拉列表样式 */
            QComboBox QAbstractItemView {
                border:10px solid blue;       /*设置边框颜色 */
                selection-background-color: #4A90E2; /* 选中项背景色 蓝色*/
                selection-color: orange;         /* 选中项文本颜色 */
                background-color: red;      /* 列表背景色 */
                color: white;                   /* 列表文本颜色 */
                border-radius: 15px;             /* 列表圆角 */
            }

        """)

        layout.setStretch(0,1)
        layout.setStretch(1, 3)

        self.combo.currentIndexChanged.connect(self.selcetChanged)
        print(f"下拉框元素个数{self.combo.count()}")
        i = 2
        print(f"下拉框第{i}索引值为{self.combo.itemText(i)}")


    def selcetChanged(self):

        print(f"{self.combo.currentText()}")


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
