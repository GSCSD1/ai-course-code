


# 方式1：  时间复杂度   logn * O(1) = O(logn)
def binart_search1(alist,item):

    left_index = 0
    right_index = len(alist)-1
    mid = len(alist)//2

    while left_index <= right_index:  # n/2/2/2.. = 1   logn * O(1)
        if item == alist[mid]:  # 找到目标值
            return True
        elif item< alist[mid]:  # 移动right光标
            right_index = mid-1
            # 向下取整
            mid = (right_index+left_index)//2
        elif item > alist[mid]: # 移动left光标
            left_index = mid+1
            mid = (right_index+left_index)//2

    return False


# 方式二：
def binart_search2(alist,item):

    # 数列长度
    n = len(alist)
    # 递归的结束条件
    if n == 0:
        return False

    # 中间值
    mid = n//2

    if item == alist[mid]:
        return True
    elif item < alist[mid]:
        return binart_search(alist[0:mid],item)
    else:
        return binart_search(alist[mid+1:],item)



if __name__ == '__main__':
    alist = [1,2,3,4,5,6,7,8,9,10]
    print(binart_search1(alist,-100))

