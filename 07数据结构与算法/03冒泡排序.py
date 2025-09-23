


# 最坏时间复杂度 ： O(n^2)  =   时间复杂度
# 最好时间复杂度 ： O(n)
def bubble_sort(alist):
    """
        冒泡排序    5 3 4 7 2
    """
    # 如果没有交换的情况，则说明排序完成，结束循环
    for i in range(len(alist)-1):  # i = 0    控制比较轮数
        flag = False
        for j in range(len(alist)-1-i):  # j = 4   控制比较次数
            # 比较相邻两个元素，不符合要求就交换位置
            if alist[j] > alist[j+1]:  # 交换位置  # 4  5
                flag = True
                alist[j],alist[j+1] = alist[j+1],alist[j]
        if flag == False:
            break

if __name__ == '__main__':
    li = [5, 3, 4, 7, 2]
    bubble_sort(li)
    print(li)