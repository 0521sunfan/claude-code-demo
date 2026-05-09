def bubble_sort(arr):
    """
    冒泡排序算法
    
    参数:
        arr: 需要排序的列表
    
    返回:
        排序后的列表
    """
    n = len(arr)
    
    # 遍历数组中的所有元素
    for i in range(n):
        # 标志位，用于优化：如果某轮没有发生交换，说明已排好序
        swapped = False
        
        # 最后 i 个元素已经在正确位置，不需要比较
        for j in range(0, n - i - 1):
            # 比较相邻的两个元素
            if arr[j] > arr[j + 1]:
                # 交换
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果没有发生交换，说明数组已经排好序
        if not swapped:
            break
    
    return arr


if __name__ == "__main__":
    
    # 测试 1: 普通数组
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"原数组: {arr1}")
    result1 = bubble_sort(arr1.copy())
    print(f"排序后: {result1}")
    print()

    # 测试 2: 已排序数组（验证提前终止优化）
    arr2 = [1, 2, 3, 4, 5]
    print(f"原数组: {arr2}")
    result2 = bubble_sort(arr2.copy())
    print(f"排序后: {result2}")
    print()

    # 测试 3: 逆序数组
    arr3 = [5, 4, 3, 2, 1]
    print(f"原数组: {arr3}")
    result3 = bubble_sort(arr3.copy())
    print(f"排序后: {result3}")
