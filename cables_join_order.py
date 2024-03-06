import heapq

def cable_join_order(iterable):
    # Створюємо мінімальну купу з усіх елементів ітерабельного об'єкта.
    h = []
    i = 1
    for value in iterable:
        heapq.heappush(h, value)
    
    # Визначаємо пари з найменшою довжиною.
    while len(h) > 1:
        join_1 = heapq.heappop(h)
        join_2 = heapq.heappop(h)

        print(f'Joint {i}: {join_1} and {join_2}')

    # Створюємо новий елемент як суму двох найменших та додаємо його до купи.
        sum = join_1 + join_2

        heapq.heappush(h, sum)

        i += 1

# Масив для сортування
arr = [12, 11, 13, 5, 6, 7]
cable_join_order(arr)

