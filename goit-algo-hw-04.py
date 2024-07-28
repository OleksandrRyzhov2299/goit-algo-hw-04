import random
import timeit

a = [2, 1, 5, -2, 8]


def insertion_sort(list_x):
    for i in range(1,len(list_x)):
        print("i = ", i)
        y = list_x[i]
        print("y = ", y)
        g = i -1
        print("g = ", g)
        print("list_x[g] = ", list_x[g])
        while g >= 0 and y < list_x[g]:
            list_x[g + 1] = list_x[g]
            g -= 1
        list_x[g + 1] = y
        print(list_x)
    return list_x
insertion_sort(a)


def merge_sort(list_x):
    if len(list_x) <= 1:
        return list_x
    
    mid = len(list_x) // 2
    left = merge_sort(list_x[:mid])
    right = merge_sort(list_x[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



# Генеруємо випадкові дані для тестування
data_small = [random.randint(0, 1_000) for _ in range(1_000)]  # Менший масив
data_large = [random.randint(0, 10_000) for _ in range(10_000)]  # Великий масив

# Вимірювання часу виконання для маленького масиву
time_insertion_small = timeit.timeit(lambda: insertion_sort(data_small[:]), number=10)
time_merge_small = timeit.timeit(lambda: merge_sort(data_small[:]), number=10)
time_timsort_small = timeit.timeit(lambda: sorted(data_small[:]), number=10)

# Вимірювання часу виконання для великого масиву
time_insertion_large = timeit.timeit(lambda:
insertion_sort(data_large[:]), number=10)
time_merge_large = timeit.timeit(lambda: merge_sort(data_large[:]), number=10)
time_timsort_large = timeit.timeit(lambda: sorted(data_large[:]), number=10)

print(f"{'Алгоритм':<20}| {'Маленький масив':<20}| {'Великий масив':<20}")
print(f"{'-'*21}+{'-'*22}+{'-'*22}")
print(f"{'Сортування вставками':<20}| {time_insertion_small:<20.5f}| {time_insertion_large:<20.5f}")
print(f"{'Сортування злиттям':<20}| {time_merge_small:<20.5f}| {time_merge_large:<20.5f}")
print(f"{'Timsort':<20}| {time_timsort_small:<20.5f}| {time_timsort_large:<20.5f}")