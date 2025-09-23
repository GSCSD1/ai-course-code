

# 时间复杂度 ： O(n^2)  稳定的排序算法
def insert_sort(alist):
    """插入排序"""

    """
        第一轮 ： alist[1] 和 alist[0]  比较   i=0  比较次数为1    j= [0,1)
        第二轮 ： alist[2] 和 alist[1]  比较   i=1  比较次数为2   j= [0,2)
                 alist[1] 和 alist[0]  比较
        第三轮 ： alist[3] 和 alist[2]  比较   i=2  比较次数为3   j= [0,3)
                 alist[2] 和 alist[1]  比较
                 alist[1] 和 alist[0]  比较
    """
    for i in range(len(alist)-1) :  # 控制比较轮数  [0,4)  2
        for j in range(i+1,0,-1):  #  3
            # 将待排序的元素按升序要求插入到已经排序好的序列中  不符合升序要求交换两个数
            if alist[j] < alist[j-1]:  # alist[1] 和 alist[0]
                alist[j],alist[j-1] = alist[j-1],alist[j]
            else:
                break

if  __name__ == '__main__':
    alist = [54,26,93,-1,77,31,44,55,20]
    insert_sort(alist)
    print(alist)