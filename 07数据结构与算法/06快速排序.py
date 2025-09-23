

#  时间复杂度 = 平均时间复杂度：调用一次的时间复杂度是O(n) * logn   O(nlogn)
# 最差时间复杂度  如果是已经排好的数组：O(n^2)       1 2 3 4 5 6 7  ->  mid: 1  right:2 3 4 5 6 7   -> mid: 2  right:3 4 5 6 7

#
def quick_sort(alist):
    # 终止递归的条件
    if len(alist) <= 1:  # n/2/2/2/... = 1   n = 1*2*2*2*2....  得出整个函数递归次数为logn
        return alist
    # 选择基准值
    pivot = alist[0]
    left = []
    mid = []
    right = []
    for i in alist:
        if i<pivot:  # 如果当前数小于基准值
            left.append(i)
        elif i == pivot:
            mid.append(i)
        else:
            right.append(i)

    return quick_sort(left) + mid + quick_sort(right)

if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    print(quick_sort(alist))
