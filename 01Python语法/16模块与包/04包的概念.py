"""
    包： 是一个有层次目录结构，用来更好的管理模块，通俗来讲就是一个目录。
    里面存放python文件和或者新的目录，每一个包里面都需要一个__init__.py

    注意： 对于python3.3之后 这个文件不需要自己创建

    __init__.py ：
            1、标识包的目录，告诉python解释器该文件所在的目录
            应该被视为一个包而不是一个普通目录。
            2、执行初始化代码，在调用包里面模块时，该文件里面的代码也会被运行
            3、控制包的导入行为，通过__all__来控制哪些模块被导入
            4、提供包级别的命名空间
            5、批量导入模块
    from 包名  import 模块
    import 包名.模块名

    在python中，可以使用绝对路径或相对路径，需要根据项目结构和实际需求来选择合适的导入路径
    绝地路径从项目的根目录开始  先对路径相当于当前模块的位置
"""

from mypackage import  module1,moudle2
import mypackage.module1


mypackage.module1.info_print1()
moudle2.info_print2()

