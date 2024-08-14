// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // Write C code here
    int arr[] = {17,8,26,3,11,21};
    int size = 6;
    void ShellSort(int arr[],int size)
    {
        for(int i=size/2;i>0;i=i/2)
        {
            
            for(int j=i;j<size;j++)
            {
                int key = arr[j];
                int k = j;

                while(k>=i && key<arr[k-i])
                {
                    arr[k] = arr[k-i];
                    k = k-i;
                }
                arr[k] = key;
            }
        }
        
        printf("Sorted Array:\n");
        for(int i=0;i<size;i++)
        {
            printf("%d\t",arr[i]);
        }
    }
    
    ShellSort(arr,size);

    return 0;
}