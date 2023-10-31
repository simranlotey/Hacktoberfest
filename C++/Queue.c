#include<stdio.h>
#include<stdlib.h>
#define SIZE 10
int front = -1;
int rear = -1;
int arr[SIZE],i;
void Enqueue();
void Dequeue();
void Display();
int main(){
    int choice;
    while(1){
        printf(" Perform Queue Operations here ");
        printf("\n1.Enqueue \n 2.Dequeue \n 3.Display");
        printf("\nEnter choice : ");
        scanf("%d",&choice);
        switch(choice){
            case 1: Enqueue();
            break;
            case 2: Dequeue();
            break;
            case 3: Display();
            break;
            case 4: exit(0);
            break;
            default:
            printf("invalid Choice!");
        }
    }
}
void Enqueue()
{
    int x;
    if(rear == SIZE -1){
        printf("overflow");
    }
    else{
        if(front = -1)
        front = 0;
        printf("enter element:");
        scanf("%d", &x);
        rear = rear+1;
        arr[rear] = x;
    }
}
void Dequeue(){
    if(rear == -1 && front<rear){
        printf("Underflow!!!");
    }
    else{
        printf("Deleted element is: %d\n",arr[front]);
        front = front+1;
    }
}
void Display(){
    if(rear == -1){
        printf("Underflow!!!\n");
    }
    else{
        printf("the elements are: \n");
        for(i=front;i<=rear;i++){
            printf("%d\n",arr[i]);
        }
    }
}
