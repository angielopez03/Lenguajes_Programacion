import random
import time

class bubbleSort:

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def __str__(self):
        return " ".join([str(x) 
                        for x in self.array])

    def bubbleSortRecursive(self, n=None):
        if n is None:
            n = self.length
        count = 0

        if n == 1:
            return
        for i in range(n - 1):
            if self.array[i] > self.array[i + 1]:
                self.array[i], self.array[i +
                1] = self.array[i + 1], self.array[i]
                count = count + 1
        if (count==0):
            return

        self.bubbleSortRecursive(n - 1)

def main():
    n = 20000
    arr = [random.randint(0, 100000) for _ in range(n)]
    
    sort = bubbleSort(array)
    
    sort.bubbleSortRecursive()
    print("Sorted array :\n", sort)

    inicio = time.time()
    bubbleSort(arr)
    fin = time.time()

    print(f"Ordenamiento en Python con {n} elementos: {fin - inicio} segundos")


if __name__ == "__main__":
    main()





