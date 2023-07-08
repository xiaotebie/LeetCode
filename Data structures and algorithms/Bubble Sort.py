"""
这里学习冒泡排序
1.exchange_sort 最简单的交换排序
2. bubble_sort 内循环从后往前遍历
3.bubble_sort2 内循环从前往后遍历
4.bubble_sort3 完整版冒泡，flag标记后续元素是否已经排序完成
"""
import random


# 最简单的交换排序，（冒泡排序初级版）
# 通过遍历整个数组，交换元素顺序进行排序
# 原理：
# 每次循环，依次将第i个元素与它后边的所有元素比较，小的放在arr[i]的位置
# 所以第一次循环的arr[0]是所有元素最小的
# 第二次的arr[1]是第二小的，依次类推
# 核心思想：在每一次外部循环中，我们都会找出未排序部分的最小元素，并将其放到正确的位置上。这个“正确的位置”就是当前未排序部分的第一个位置，也就是arr[i]。
def exchange_sort(arr):
    length = len(arr)
    for i in range(length):
        print("外：", arr)
        print("i=", i)
        for j in range(i + 1, length):

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            print("  j=", j)
            print("  内：", arr)

            print()
    return arr


# 每次循环，会将最小的一个数放到数组未排序部分的最前
# 则每次内循环range为length - i - 1，意味着每循环一次，range减小1
# 因为最前的数字已经是最小，无需再操作
# 为什么是倒序遍历：因为需要将最小的移动到最左边，所以需要从最右边开始比较，最后操作最左边的元素才能将最小的元素移动到最左边
def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        print(arr)
        for j in range(length - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


# 每次循环，会将最大的一个数放到数组的最后
# 则每次内循环range为length - i - 1，意味着每循环一次，range减小1
# 因为最后的数字已经是最大，无需再操作
# 为什么是顺序遍历：因为需要将最大的移动到最右边，所以需要从最左边开始比较，最后操作最右边的元素才能将最大的元素移动到最右边
def bubble_sort2(arr):
    length = len(arr)
    print("开始", arr)
    for i in range(length):

        for j in range(0, length - i - 1):  # 从0开始，到length - i - 1
            print("   range大小：", length - i - 1)

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print("   内", arr)
        print("外", arr)
    return arr


# 这是改进的最终版本的冒泡排序：
# 如果本次外循环未进行元素交换则说明：
# 1.当前位置后面的元素已经排序完成
# 2.前边的元素也已经被排序，则说明排序已经完成可提前退出
def bubble_sort3(arr):
    length = len(arr)
    flag = True  # flag用来作为标记
    for i in range(length):
        flag = False  # 初始为False
        print(arr)
        for j in range(length - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]  # 交换arr[j]与arr[j - 1]的值
                flag = True  # 如果有数据交换，则flag为True
        if not flag:  # 若flag为False 则退出循环
            break
    return arr


def swap(arr, i, j):
    if i < len(arr) and j < len(arr):
        arr[i], arr[j] = arr[j], arr[i]
    else:
        print("错误：索引超出数组范围")
    return arr


a = [5, 7, 4, 3, 9, 6, 1, 0, 2, 8]
print(exchange_sort(a))
