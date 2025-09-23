"""
    滑动条
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QSlider,QVBoxLayout
import sys

"""常用创建窗口的方式"""
# 继承QWidget类所有的属性和方法
class mainWidget(QWidget):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()
        # 修改窗口标题
        self.setWindowTitle("创建pyqt窗口")
        # 修改窗口大小
        self.resize(200, 200)

        self.slider1 =  QSlider(Qt.Horizontal)  # Qt.Vertical 垂直方向  Qt.Horizontal 水平方向

        """基本参数设置"""
        # 设置最小值
        self.slider1.setMinimum(12)
        # 设置最大值
        self.slider1.setMaximum(48)
        # 设置步长
        self.slider1.setSingleStep(5)  # 键盘操作(左右方向键)才有效
        # 设置当前值
        self.slider1.setValue(24)
        # 打印当前值
        print(self.slider1.value())

        self.slider1.valueChanged.connect(self.value_change_slot)

        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.slider1)

        """样式设置"""
        self.slider1.setStyleSheet("""
                /*滑槽(轨道)样式*/
                QSlider::groove:horizontal{
                    background: #7E7F80;  
                    height:7px;
                    border-radius:3px;
                }/*滑块前面的轨道样式*/
                QSlider::sub-page:horizontal{
                    background: #0067C0;    /*蓝色 */
                }
                /*滑块样式*/
                QSlider::handle:horizontal{
                    background: #0067C0;  /*蓝色 */
                    width:14px;
                    height:14px;
                    border-radius:7px;
                    margin:-4px 0;
                    border : 2px solid white ; 
                }
                /*鼠标悬停样式*/
                QSlider::handle:hover{
                    background: #00437D;
                }
                /*按下样式*/
                QSlider::handle:pressed{
                    background: #0089FF;
                }
                
        """)
    def value_change_slot(self):
        # 打印当前值
        print("当前值:",self.slider1.value())

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




