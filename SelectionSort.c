// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // Write C code here
    int arr[] = {17,8,26,3,11,21};
    int size = 6;
    void SelectionSort(int arr[],int size)
    {
        for(int i=0;i<size-1;i++)
        {
            int min = i;
            for(int j=i+1;j<size;j++)
            {
                if (arr[j] < arr[min])
                {
                    min = j;
                }
            }

            int temp = arr[min];
            arr[min] = arr[i];
            arr[i] = temp;
        }
        
        printf("Sorted Array:\n");
        for(int i=0;i<size;i++)
        {
            printf("%d\t",arr[i]);
        }
    }
    
    SelectionSort(arr,size);

    return 0;
}