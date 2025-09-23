import os.path

from PyQt5.QtCore import QFile
from PyQt5.QtGui import QIcon, QKeySequence, QColor
from PyQt5.QtWidgets import QApplication, QMenuBar, QMenu, QMainWindow, QAction, QToolBar, QToolButton, QTextEdit, \
    QFontDialog, QColorDialog, QMessageBox, QFileDialog
import sys

"""常用创建窗口的方式"""
# 继承QWidget类所有的属性和方法
class mainWidget(QMainWindow):
    def __init__(self):
        # 初始化父类的__init__方法 将self参数传进去
        super().__init__()  # QWidget.__init__(self)
        self.fileName = "无标题-记事本"
        self.file_path = ""
        # 修改窗口标题
        self.setWindowTitle("无标题-记事本")
        # 修改窗口大小
        self.resize(700, 600)
        # # 设置窗口位置
        # self.move(0,0)
        # 设置窗口图标
        icon =  QIcon('../images/icon/1.png')
        self.setWindowIcon(icon)


        self.ui_init()
    def ui_init(self):

        self.textEdit = QTextEdit(self)
        """创建菜单栏"""
        self.create_menu_bar()
        """创建工具栏"""
        self.create_tool_bar()
        # 文本发生改变时触发信号
        self.textEdit.textChanged.connect(self.update_title)

        self.setCentralWidget(self.textEdit)  # 将文本编辑控件放到核心区域


    def create_menu_bar(self):
        # 添加菜单栏类
        menubar =  QMenuBar(self)
        self.setMenuBar(menubar)

        # 在菜单中添加文件菜单 QMenu
        file_menu =  QMenu("文件(F)",self)
        menubar.addMenu(file_menu)

        # 在菜单中添加编辑菜单 QMenu
        edit_menu = QMenu("编辑(E)", self)
        menubar.addMenu(edit_menu)

        # 在文件栏中添加动作  QAction 并设计图标
        # 新建
        self.new_action =  QAction(QIcon('../images/icon/new.png'),"新建(N)",self)
        self.new_action.setShortcut(QKeySequence.New)
        self.new_action.triggered.connect(self.new_action_slot)
        file_menu.addAction(self.new_action)

        # 打开
        open_action = QAction(QIcon('../images/icon/open.png'), "打开(O)", self)
        open_action.setShortcut(QKeySequence.Open)
        open_action.triggered.connect(self.open_action_slot)
        file_menu.addAction(open_action)

        # 保存
        self.save_action = QAction(QIcon('../images/icon/save.png'), "保存(S)", self)
        self.save_action.setShortcut(QKeySequence.Save)
        self.save_action.triggered.connect(self.save_action_slot)
        file_menu.addAction(self.save_action)

        # 另存
        saveAs_action = QAction(QIcon('../images/icon/save.png'), "另存为(A)", self)
        saveAs_action.setShortcut(QKeySequence.SaveAs)
        saveAs_action.triggered.connect(self.saveAs_action_slot)
        file_menu.addAction(saveAs_action)

        # 复制
        copy_action = QAction(QIcon('../images/icon/copy.png'), "复制(C)", self)
        copy_action.setShortcut(QKeySequence.Copy)
        copy_action.triggered.connect(self.textEdit.copy)
        edit_menu.addAction(copy_action)

        # 粘贴
        paste_action = QAction(QIcon('../images/icon/paste.png'), "粘贴(P)", self)
        paste_action.setShortcut(QKeySequence.Paste)
        paste_action.triggered.connect(self.textEdit.paste)
        edit_menu.addAction(paste_action)

        # 剪切
        cut_action = QAction(QIcon('../images/icon/cut.png'), "剪切(T)", self)
        cut_action.setShortcut(QKeySequence.Cut)
        cut_action.triggered.connect(self.textEdit.cut)
        edit_menu.addAction(cut_action)

        # 撤销
        undo_action = QAction(QIcon('../images/icon/undo.png'), "撤销(U)", self)
        undo_action.setShortcut(QKeySequence.Undo)
        undo_action.triggered.connect(self.textEdit.undo)
        edit_menu.addAction(undo_action)

        # 恢复
        redo_action = QAction(QIcon('../images/icon/redo.png'), "恢复(R)", self)
        redo_action.setShortcut(QKeySequence.Redo)
        redo_action.triggered.connect(self.textEdit.redo)
        edit_menu.addAction(redo_action)

    def create_tool_bar(self):
        # 添加工具栏
        tool_bar = QToolBar()
        # 将工具栏加入到主窗口
        self.addToolBar(tool_bar)

        tool_bar.addAction(self.new_action)
        tool_bar.addAction(self.save_action)

        # 字体工具按钮
        font_btn = QToolButton()
        font_btn.setIcon(QIcon('../images/icon/font.png'))
        font_btn.clicked.connect(self.update_font)
        tool_bar.addWidget(font_btn)


        # 颜色工具按钮
        color_btn = QToolButton()
        color_btn.setIcon(QIcon('../images/icon/color.png'))
        color_btn.clicked.connect(self.update_color)
        tool_bar.addWidget(color_btn)

    def update_title(self):
        self.setWindowTitle( '*' + self.fileName)

    def update_font(self):
        # 获取用户用户选择的字体属性 (元组  ： 字体 + 是否确认)
        font,is_ok =  QFontDialog.getFont(self)
        if is_ok:
            # self.textEdit.setFont(font)
            self.textEdit.setCurrentFont(font)   # 应用选择的字体
        else:
            print("用户取消了字体选择")

    def update_color(self):
        # 打开颜色对话框 会给我们返回一个QColor对象 表示用户选择的颜色
        color =  QColorDialog.getColor(QColor(),self)
        self.textEdit.setTextColor(color)  # 设置选中文字颜色


    def new_action_slot(self):
        print("new_action_slot")
        # 判断文本内容是否被修改
        result = self.textEdit.document().isModified()
        if result == False:
            self.textEdit.clear()
            self.fileName = "无标题-记事本"
            self.setWindowTitle(self.fileName)
        else:
            ret = QMessageBox.warning(None,"notepad","是否保存当前修改内容",QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
            if ret == QMessageBox.Yes:
                # 第二个参数为文件对话框的标题  param3： 打开的文件路径 parma4：文件过滤器
                filepath =  QFileDialog.getSaveFileName(self,"另存为",'./',"记事本TXT(*.txt)")
                # 写文件
                text = self.textEdit.toPlainText()  # 获取文本编辑器中文本内容
                with open(filepath[0],"w") as f:
                    f.write(text)
                print(f"{filepath}写入成功")
                self.textEdit.document().setModified(False)
                self.textEdit.clear()
                self.setWindowTitle(self.fileName)
            elif ret == QMessageBox.No:
                self.textEdit.clear()
                self.setWindowTitle(self.fileName)


    def open_action_slot(self):
        print("open_action_slot")
        result =  self.textEdit.document().isModified()
        if result:# 文件被修改  先询问是否保存再打开文件
            ret = QMessageBox.question(None,"notepad","是否保存当前修改内容",QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
            if ret == QMessageBox.Yes:
                self.save_action_slot()

            elif ret == QMessageBox.No:
                self.textEdit.clear()
                self.setWindowTitle(self.fileName)

            else:
                return

        self.file_path = QFileDialog.getOpenFileName(self, "打开", './', "记事本TXT(*.txt)")[0]
        if os.path.isfile(self.file_path):
            """QFILE实现"""
            # # 创建文件对象
            # fs =  QFile(self.file_path)
            # # 打开文件
            # fs.open(QFile.ReadOnly)
            #
            # if fs.isOpen():
            #     # 读取文件内容  读取到的数据类型是QByteArray
            #     data = fs.readAll()
            #     self.textEdit.setPlainText(bytes(data).decode("utf-8"))
            #     self.fileName = os.path.basename(self.file_path)
            #     self.setWindowTitle(self.fileName)
            #     self.textEdit.document().setModified(False)
            """原生库实现"""
            print(self.file_path)
            with open(self.file_path, "r") as f:
                text = f.read()
                self.textEdit.setPlainText(text)
                self.fileName = os.path.basename(self.file_path)
                self.setWindowTitle(self.fileName)
                self.textEdit.document().setModified(False)



    def save_action_slot(self):
        """无标题-记事本 内容被修改  对未打开的文件进行修改"""
        if '无标题' in self.fileName:
            """无标题保存"""
            self.saveAs_action_slot()

        else :
            """有标题保存"""
            text = self.textEdit.toPlainText()
            with open(self.file_path, 'w') as f:
                f.write(text)
            print(f"{self.file_path} 内容已保存")
            self.fileName = os.path.basename(self.file_path)
            self.setWindowTitle(self.fileName)

    def saveAs_action_slot(self):
        print("saveAs_action_slot")
        # 第二个参数为文件对话框的标题  param3： 打开的文件路径 parma4：文件过滤器
        self.file_path = QFileDialog.getSaveFileName(self, "另存为", './', "记事本TXT(*.txt)")[0]
        if  os.path.isfile(self.file_path):
            # 写文件

            """QFILE实现"""
            # 创建文件对象
            fs =  QFile(self.file_path)
            # 打开文件
            fs.open(QFile.WriteOnly)
            if fs.isOpen():
                text = self.textEdit.toPlainText()  # 获取文本编辑器中文本内容
                # 读取文件内容  读取到的数据类型是QByteArray
                fs.write(text.encode("utf-8"))
                print(f"{self.file_path}写入成功")
                self.textEdit.document().setModified(False)
                self.fileName = os.path.basename(self.file_path)
                print(self.fileName)
                self.setWindowTitle(self.fileName)

            """原生库实现"""
            # text = self.textEdit.toPlainText()  # 获取文本编辑器中文本内容
            # with open(self.file_path, "w") as f:
            #     f.write(text)
            # print(f"{self.file_path}写入成功")
            # self.textEdit.document().setModified(False)
            # self.fileName = os.path.basename(self.file_path)
            # print(self.fileName)
            # self.setWindowTitle(self.fileName)

    def read_file(self,file_path):
        if os.path.isfile(file_path):
            print(self.file_path)
            with open(file_path, "r",encoding='utf-8') as f:
                text = f.read()
                self.textEdit.setPlainText(text)
                self.fileName = os.path.basename(file_path)
                self.setWindowTitle(self.fileName)
                self.textEdit.document().setModified(False)
                self.file_path = file_path

if __name__ == '__main__':
    """程序启动的基本流程"""
    # 创建qApplication类   sys.argv为了通过命令行传参，但是大部分场景已经不在需要
    print(sys.argv)
    app = QApplication(sys.argv)
    # 创建窗口对象 QWidget为UI界面
    window =  mainWidget()

    if len(sys.argv)>1:
        window.read_file(sys.argv[1])

    # 显示窗口
    window.show()
    # 程序关闭之后自动释放资源
    sys.exit(app.exec_())


