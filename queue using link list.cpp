#include<iostream.h>
#include<conio.h>

struct node
{
       int data;
       node *next;
};

class queue
{
             node *front,*rear;
             public:
             queue();
             void enqueue(int num);
             int dequeue();
             void display();
};

queue::queue()
{
              front=rear=NULL;
}

void queue::enqueue(int num)
{
     node *temp;
     temp=new node;
     temp->data=num;
     temp->next=NULL;
     if(front==NULL)
     {
                    rear=front=temp;
                    
     }
     else
     {
         rear->next=temp;
         rear=temp;
         
     }
}

int queue::dequeue()
{   int num;
    if(front==NULL)
    {
                         return -1;
    }
    
    node *temp;
    temp=front;
    num=front->data;
    front=front->next;
    delete temp;
    return num;
    
}
    
void queue::display()
{
     node *q;
     q=front;
     while(q!=NULL)
     {
     cout<<"\n"<<q->data;
     q=q->next;
     } 
}

main()
{     int num,n1,ch;
      queue a;
      do
      {
      cout<<"\n1.ENQUEUE \n2.DEQUEUE \n3.DISPLAY \n4.EXIT\n";
      cin>>ch;
      switch(ch)
      {
                case 1:cout<<"\nEnter no to be inserted";
                cin>>num;
                a.enqueue(num);
                break;
                case 2:n1=a.dequeue();
                if(n1==-1)
                cout<<"                     queue empty";
                else
                cout<<"\nThe no removed is "<<n1;
                break;
                case 3:a.display();
                break;
                case 4: exit(0);
      }
      }while(ch!=4);
                    
                
} 
   
