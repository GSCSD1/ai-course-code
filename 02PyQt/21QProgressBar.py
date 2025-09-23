"""
   进度条 ：
"""
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication,QWidget,QProgressBar,QVBoxLayout
import sys
"""常用创建窗口的方式  模拟资源"""


# 继承QWidget类所有的属性和方法
class mainWidget(QWidget):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("进度条控件的使用")
        # 修改窗口大小
        self.resize(800, 800)

        mainLayout = QVBoxLayout(self)


        """基本设置"""
        # 创建计数器控件
        self.ProgressBar1= QProgressBar()
        mainLayout.addWidget(self.ProgressBar1)
        # 设置进度条的范围
        self.ProgressBar1.setRange(0,100)
        # 设置进度条初始值
        self.ProgressBar1.setValue(5)
        # 设置百分比文本是否可见
        self.ProgressBar1.setTextVisible(True)

        # 获取当前进度值
        print(self.ProgressBar1.value())

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.value_change_slot)
        self.timer.start()

        self.ProgressBar1.setStyleSheet("""
            QProgressBar{
                border:3px solid #4A90E2;
                border-radius:10px;
            }
             QProgressBar::chunk{  
                background-color: red;
                border-radius:10px;
            }
        """)

        self.ProgressBar1.setAlignment(Qt.AlignCenter)


    # 1s进一次
    def value_change_slot(self):
        # 获取当前进度值
        cur_num = self.ProgressBar1.value()+2

        if cur_num < 100:
            # 设置进度条初始值
            self.ProgressBar1.setValue(cur_num)
        else:
            self.ProgressBar1.setValue(100)
            self.timer.stop()





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


