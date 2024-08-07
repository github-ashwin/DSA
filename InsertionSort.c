// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // Write C code here
    int arr[] = {17,8,26,3,11,21};
    int size = 6;
    void InsertionSort(int arr[],int size)
    {
        for(int i=1;i<size;i++)
        {
            int j=i-1;
            int key = arr[i];
            
            while(key<arr[j] && j>=0)
            {
                arr[j+1]=arr[j];
                j=j-1;
            }
            arr[j+1]=key;
        }
        
        printf("Sorted Array:\n");
        for(int i=0;i<size;i++)
        {
            printf("%d\t",arr[i]);
        }
    }
    
    InsertionSort(arr,size);

    return 0;
}