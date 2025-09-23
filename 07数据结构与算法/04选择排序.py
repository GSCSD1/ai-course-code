


# 时间复杂度 : O(n^2)   不稳定的算法
def select_sort(alist):
    """选择排序"""
    for i in range(len(alist)-1): # 1
        # 假定最小值的下标
        min_index = i    #  1
        for j in range(i+1,len(alist)):  # range(2,5)
            # 如果当前元素比最小值小，则将最小值下标改为当前元素下标
            if  alist[j] < alist[min_index] :
                min_index = j

        # 如果假定的最小值下标发生了变化，那么将最小值下标和i的下标交换
        if min_index != i :
            alist[i],alist[min_index] = alist[min_index],alist[i]


if __name__ == '__main__':
    li = [54,26,93,17,77,31,44,55,20]
    select_sort(li)
    print(li)