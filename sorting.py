def insertion_sort(arr):
    """
    Сортировка методом вставок O(N^2)
    """
    for i in range(1, len(arr)):
        for j in range(0, i-1):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

    return arr


def choice_sort(arr):
    """
    Сортировка методом выбора O(N^2)
    """
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


def bubble_sort(arr):
    """
    Сортировка методом пузырька O(N^2)
    """
    for i in range(0, len(arr)):
        for j in range(len(arr)-i):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def test_method(method_name):
    arr = [3, 12, 25, 15, 1, 9, 33, 0, 7]
    arr_true_sorted = [0, 1, 3, 7, 9, 12, 15, 25, 33]
    arr2 = method_name(arr)
    print(arr)
    print(arr2)
    if arr2 == arr_true_sorted:
        print("pass")
    else:
        print("fail")


if __name__ == "__main__":
    print("INSERTION")
    test_method(insertion_sort)
    print("CHOICE")
    test_method(choice_sort)
    print("BUBBLE")
    test_method(choice_sort)
