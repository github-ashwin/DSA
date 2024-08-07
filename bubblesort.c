// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // Write C code here
    int arr[5];
    printf("\nEnter array elements\n");
    for(int i=0;i<5;i++)
    {
        scanf("%d",&arr[i]);
    }
    
    void BubbleSort(int arr[])
    {
        printf("\nArray before sorting:\n");
        for(int i=0;i<5;i++)
        {
            printf("%d\t",arr[i]);
        }
        
        for(int i=0;i<5;i++)
        {
            int flag=0; //Optimization
            for(int j=0;j<5-i-1;j++)
            {
                if(arr[j]>arr[j+1])
                {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    flag = 1;
                }
            }
            if(flag==0)
            break;
        }
        
        printf("\nArray after sorting:\n");
        for(int i=0;i<5;i++)
        {
            printf("%d\t",arr[i]);
        }
    }
    
    BubbleSort(arr);
    return 0;
}