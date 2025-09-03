#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void bubbleSort(int arr[], int n)
{
    if (n == 1)
        return;

    int count = 0;
    for (int i=0; i<n-1; i++)
        if (arr[i] > arr[i+1]){
            swap(&arr[i], &arr[i+1]);
            count++;
        }

        if (count==0)
           return;

    bubbleSort(arr, n-1);
}

int main() {
    int n = 20000;
    int *arr = malloc(n * sizeof(int));
    srand(time(NULL));

    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 100000;
    }

    clock_t inicio = clock();
    bubbleSort(arr, n);
    clock_t fin = clock();

    double tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;
    printf("Ordenamiento en C con %d elementos: %f segundos\n", n, tiempo);

    free(arr);
    return 0;
}
