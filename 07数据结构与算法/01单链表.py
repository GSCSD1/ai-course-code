
# 创建节点类型
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None  # 指向下一个节点
# 创建单链表类型
class SinglyLinkedList:
    def __init__(self):
        self.head = None # 头节点
        self.length = 0  # 链表长度

    def is_empty(self):
        return self.length == 0

    def insert(self,index,value):
        """
            index: 表示要插入位置的索引
            value: 要插入的值
        """
        # 判断index是否为合法的范围   0 <= index<=length
        if not  0<=index<=self.length:
            print(f"位置{index}不对，插个毛")
            return False
        new_node =  Node(value)  # 创建节点
        if index==0:  # 插在头部
             # 链表为空
             if self.is_empty():
                 self.head = new_node
              # 链表不为空  有待验证
             else:
                 new_node.next = self.head
                 self.head = new_node
        else:    # 插在中间或尾部
            current_node =self.head
            for _ in range(index-1):
                current_node = current_node.next
            # 新节点存储当前的下一个节点地址
            new_node.next = current_node.next
            current_node.next = new_node
        self.length += 1

        return True


    def delete(self,index):
        # 删除：删除index位置的节点
        """
                index: 要删除的索引位置
        """
        if not self.is_empty(): # 判断是否有数据
            # 判断index是否为合法的范围   0 <= index<=length
            if not 0 <= index < self.length:
                print(f"位置{index}不对，删不了")
                return False
            if index==0: # 删除头部
                self.head = self.head.next
            else:  # 删除中间和尾部
                current_node = self.head
                for _ in range(index-1):
                    current_node = current_node.next
                current_node.next  = current_node.next.next
            self.length -= 1
        return True


    def find(self,value):
        """
            查找 ： 按值查位置
        """
        current_node = self.head
        index =  0
        while current_node:
            if current_node.data == value:
                print(f"找到了! {value}在位置{index}")
                return index
            current_node = current_node.next
            index += 1
        print(f"{value}不在这儿!")
        return -1

    # 遍历数据
    def display(self):

        # 判断是否有数据
        if not self.is_empty() :
            curent_node = self.head
            print('链表里有,', end='')
            while curent_node is not None:
                print(curent_node.data,end='->')
                curent_node = curent_node.next

        print('None')

# 测试一把
if __name__ == '__main__':
    sl = SinglyLinkedList()
    sl.insert(0,666)   # 往头部插
    sl.insert(1, 111)  # 往尾部插
    sl.insert(2, 222)
    sl.insert(3, 333)
    sl.insert(2, 2222) # 往中间插
    sl.insert(0, 100)  # 往头部插
    sl.insert(6, 6666)    # 往尾部插

    sl.display()
    sl.delete(1)
    sl.display()
    sl.find(111)