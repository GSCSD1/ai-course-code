# 创建节点类型
class Node:
    def __init__(self,data):
        self.prev = None  # 指向上一个节点
        self.data = data
        self.next = None  # 指向下一个节点


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # 头节点
        self.length = 0  # 链表长度
        self.tail = None  # 尾节点

    def is_empty(self):
        return self.length == 0
    def insert(self,index,value):
        if not 0<=index<=self.length:
            print(f"位置{index}不对，插个毛")
            return False
        new_node = Node(value)
        if index==0:
            if self.is_empty():
                 self.head = self.tail = new_node  # 将head与tail全部指向新节点
            else :  # 链表不为空   有待验证
                 self.head.prev = new_node
                 new_node.next = self.head
                 self.head = new_node
        else :  # 插中间或尾部
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            if current_node.next is None: # 到达尾节点 执行插入尾部的业务逻辑
                current_node.next  = new_node
                new_node.prev = current_node
                self.tail = new_node
                new_node.next = None
            else : # 执行插入中间的业务逻辑
                new_node.next = current_node.next
                current_node.next.prev = new_node
                new_node.prev = current_node
                current_node.next = new_node

        self.length += 1
        return True

    def delete(self, index):
        # 删除：删除index位置的节点
        """
                index: 要删除的索引位置
        """
        if not self.is_empty():  # 判断是否有数据
            # 判断index是否为合法的范围   0 <= index<=length
            if not 0 <= index < self.length:
                print(f"位置{index}不对，删不了")
                return False

            if index == 0:  # 删除头部
                self.head = self.head.next
                self.head.prev = None
            elif  index == self.length-1:  # 当前节点为尾节点
                    self.tail.prev.next = None
                    self.tail = self.tail.prev
            else:  # 删除中间或尾部
                current_node = self.head
                for i in range(index-1):
                    current_node = current_node.next
                else :   # 删除中间
                    current_node.next = current_node.next.next
                    current_node.next.prev = current_node
            self.length -= 1

        else:
            return False

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

    # 显示节点数据
    def display(self):
        # 判断是否有数据
        if not self.is_empty():
            curent_node = self.head
            print('链表里有,', end='')
            while curent_node is not None:
                print(curent_node.data, end='->')
                curent_node = curent_node.next

        print('None')


if __name__ == '__main__':
    dll = DoublyLinkedList()  # 创建双向链表
    dll.insert(0,666)
    dll.insert(1, 777)
    dll.insert(2, 888)
    dll.insert(3, 999)
    dll.insert(4, 9999)
    dll.display()
    dll.delete(4)
    dll.display()
    dll.find(456)