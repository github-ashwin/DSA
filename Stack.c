#include <stdio.h>
#include <stdlib.h>
#define SIZE 3

struct Node{
    int data;
    struct Node* next;
};

struct Node* top=NULL;
int count=0;

void push(int data)
{
    if(count==SIZE)
    {
        printf("Stack Overflow");
        return;
    }
    else{
        struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data=data;
        newNode->next=top;
        top=newNode;
        count++;
        printf("Element inserted:%d",data);
    }
}

void pop()
{
    if(count==0)
    {
        printf("Stack Underflow");
        return;
    }
    else{
        struct Node* temp=top;
        top=top->next;
        count--;
        printf("Popped Element:%d",temp->data);
        free(temp);
    }
}

int main()
{
    push(10);
    push(20);
    push(30);
    push(40);
    pop();
    pop();
    pop();
    pop();
}