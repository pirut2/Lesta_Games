def quicksort(array: list[int],   # суть алгоритма в перемещении указателя
              left_border: int, rirght_border: int) -> list[int]:
    if left_border >= rirght_border:
        return -1

    left, right = left_border, rirght_border
    # опорный элемент с которым будут сравниваться левый и правый концы списка
    pivot = array[(left_border+rirght_border)//2]

    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            (array[left],
             array[right]) = array[right], array[left]
            left += 1
            right -= 1

    # сортировка вызывается рекурсивно для двух частей
    quicksort(array, left_border, right)
    quicksort(array, left, rirght_border)


array = [2, 4, 7, 9, 1, 200009, 8, 19, 201, 22, 1,
         0, 123, 51, 6, 777, 123124, 22222222, 98, 4]

quicksort(array, left_border=0, rirght_border=len(array) - 1)
print(array)
