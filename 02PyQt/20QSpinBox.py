"""
    计数器控件
"""

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QSpinBox,QVBoxLayout
import sys

"""常用创建窗口的方式"""
# 继承QWidget类所有的属性和方法
class mainWidget(QWidget):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("计数器控件的使用")
        # 修改窗口大小
        self.resize(800, 800)

        mainLayout = QVBoxLayout(self)


        # 创建计数器控件
        self.spinBox1= QSpinBox()
        mainLayout.addWidget(self.spinBox1)

        """基本设置"""
        # 设置范围
        self.spinBox1.setRange(10,30)
        # 设置初始值
        self.spinBox1.setValue(20)
        # 步长
        self.spinBox1.setSingleStep(2)
        # 获取值
        print(self.spinBox1.value())

        self.spinBox1.valueChanged.connect(self.value_change_slot)

        self.spinBox1.setStyleSheet("""
            QSpinBox{
                border:2px solid #4CAF50;
                border-radius:8px;
                font-size:50px;
                padding:10 20; /*上下 左右边距设置*/
                background-color:#f0f8ff;
            }
            QSpinBox:hover{
                border:2px solid red;
            }
        """)

    def value_change_slot(self):
        # 获取值
        print(self.spinBox1.value())


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


