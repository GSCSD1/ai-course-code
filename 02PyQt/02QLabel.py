"""
    QLabel : 显示文字 静态图  动态图

"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QMovie
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
import sys

# 继承QWidget类所有的属性和方法
class mainWidget(QWidget):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        # 修改窗口标题
        self.setWindowTitle("创建pyqt窗口")
        # 修改窗口大小
        self.resize(500, 500)
        # # 设置窗口位置
        # self.move(0,0)
        # 设置窗口图标
        icon =  QIcon('../images/1.png')
        self.setWindowIcon(icon)
        self.ui_init()  # 界面初始化

    def ui_init(self):
        """显示文字"""
        textLabel =  QLabel(self)
        # 显示文本
        textLabel.setText("购物管理系统")
        # 设置样式
        textLabel.setStyleSheet("""
            font-family:宋体;
            font-size : 15px;
            font-weight : bold; /*bold 加粗字体 */
        """)
        # 设置显示位置
        textLabel.move(0,50)
        # 设置标签大小
        textLabel.resize(100,100)

        """显示静态图片"""
        imageLabel = QLabel(self)
        # imageLabel.setPixmap(QPixmap('../images/1.png'))
        imageLabel.move(200,100)
        # 设置图片大小 方法1 图片大小和标签大小一致
        imageLabel.resize(100,100)
        # imageLabel.setScaledContents(True)  #内容自适应标签大小
        # 方法2 设置图片大小   图片大小和标签大小不一致
        # 创建pixmap对象
        pixmap = QPixmap('../images/1.png')
        # 第一个参数和第二个参数为要设置的图片尺寸  KeepAspectRatio保持默认纵横比
        pixmap_scled =  pixmap.scaled(300,200,Qt.KeepAspectRatio)
        imageLabel.setPixmap(pixmap_scled)

        """显示gif图"""
        movie =  QMovie('../images/fan.gif')
        gitLabel = QLabel(self)
        gitLabel.setMovie(movie)
        gitLabel.move(20,300)
        gitLabel.setStyleSheet("""
            QLabel{
                border: 3px solid gray;  /*设置边框为实线(solid) 线宽3px 颜色为gray*/
            }
            QLabel:hover{     /*hover 鼠标悬停 */
                border: 3px solid red;
            }
        """
        )
        movie.start()  # 播放动图
        movie.stop()


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