import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

n = 20000
arr = [random.randint(0, 100000) for _ in range(n)]

inicio = time.time()
bubble_sort(arr)
fin = time.time()

print(f"Ordenamiento en Python con {n} elementos: {fin - inicio} segundos")

