// Online C compiler to run C program online
#include <stdio.h>
#include <string.h>

int main() {
    // Write C code here
    char name[3][10]; //to store names
    char key[10]; //to store key
    
    void readName(char name[3][10])
    {
        for(int i=0;i<3;i++)
        {
            printf("\nEnter Names:\n");
            scanf("%s",name[i]);
        }
    }
    
    void displayName(char name[][10])
    {
        printf("\nNames are:\n");
        for(int i=0;i<3;i++)
        {
            printf("%s\n",name[i]);
        }
    }
    
    void check(char name[][10],char key[10])
    {
        printf("\nEnter the key to be searched\n");
        scanf("%s",key);
        
        for(int i=0;i<3;i++)
        {
            if(strcmp(key,name[i])==0)
            {
                printf("Found!");
                return;
            }
        }
        
        printf("Not found!");
        return;
    }
    
    readName(name);
    displayName(name);
    check(name,key);
    return 0;
}