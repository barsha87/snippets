#include<iostream.h>
#include<conio.h>

struct node
{
       int data;
       node *next;
};

class stack
{
             node *top;
             public:
             stack();
             void push(int num);
             int pop();
             void display();
};

stack::stack()
{
              top=NULL;
}

void stack::push(int num)
{
                node *temp;
                temp=new node;
                temp->data=num;
                if(top==NULL)
                {
                top=temp;
                top->next=NULL;
                }
                else
                {
                temp->next=top;
                top=temp;
                }
}

int stack::pop()
{   if(top==NULL)
    {
    return -1;
    }
    int num;
    node *temp;
    temp=new node;
    temp=top;
    num=top->data;
    top=top->next;
    delete temp;
    return num;
}

void stack::display()
{
     node *temp;
    temp=top;
    while(temp!=NULL)
    {
    cout<<"\n"<<temp->data;
    temp=temp->next;
    }
}
     

main()
{     int num,n1,ch;
      stack a;
      do
      {
      cout<<"\n1.PUSH \n2.POP \n3.DISPLAY \n4.EXIT\n";
      cin>>ch;
      switch(ch)
      {
                case 1:cout<<"\nEnter no to be inserted\n";
                cin>>num;
                a.push(num);
                break;
                case 2:n1=a.pop();
                if(n1==-1)
                cout<<"          stack empty";
                else
                cout<<"\nThe no popped is "<<n1;
                break;
                case 3:a.display();
                break;
                case 4: exit(0);
      }
      }while(ch!=4);
                    
                
} 
