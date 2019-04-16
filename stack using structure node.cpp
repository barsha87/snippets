#include<iostream>
#include<stdio.h>
#include<conio.h>
using namespace std;
class stack
{

public:      
      struct node
      {
             int data;
             node *next;
      }*top,*temp;

       void push(int);
       void pop();
       void disp();
       int t=-1;
int main()
{
    char ch;
    int n,d;
    do{
         cout<<"1:Push 2:Pop 3:Display Enter choice: ";
         cin>>n;
         switch(n)
         {
                  case 1: 
                       cout<<"Enter element: ";
                       cin>>d;
                       push(d);
                       break;
                  case 2:
                       pop();
                       break;
                  case 3:
                       disp();
                       break;
                  default:
                       cout<<"Invalid choice: Pls try again!";
         }
         cout<<"\nDo u want to continue? (y/n): ";
         cin>>ch;
    }while(ch=='y'||ch=='Y');
    
    return 0;
}
 
void push(int d)
{
     temp=new node;
     temp->data=d; 
       if(t==-1)
       {
               top=temp;
               t++;
       }
       else
       {
            temp->next=top;
            top=temp;
            t++;
       }
     cout<<d<<" has been pushed.";
}
void pop()
{
     if(t==-1)
     cout<<"\nStack is Empty!";
     else
     {
     top=top->next;
     t--;
     }
}
void disp()
{
     if(t==-1)
     cout<<"Stack is EMPTY!!";
     else
     {
     temp=top;
     while(temp!='\0')
     {
             cout<<temp->data;
             cout<<" -> ";
             temp=temp->next;
     }
     }
}
