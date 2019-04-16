#include <iostream>
using namespace std;

class queue
{
      int a[50],n,res;
public:  
      int front,rear;  
      void insert();
      void remove();
      void display();
};
          
void queue::insert()
{
    cout<<"\nEnter element: ";
    cin>>n;
    
    if(rear==49) 
                cout<<"Overflow!! \n";
    else if(rear==-1)
    {
         front=rear=0;
         a[rear]=n;
    }
    else
    {
        rear++;
        a[rear]=n;
    }
}


void queue::remove()
{
    if(front==-1)
               cout<<"Underflow!! \n";
    else
    {
        res=a[front];
        if(front==rear)
        front=rear=-1;
        else
        front++;
        cout<<"\nThe deleted element is: "<<res<<endl;
    }
    
}

void queue::display()
{
     cout<<"\nThe Queue now is: \n";
                            
     if(front==-1)
                {
                            cout<<"Empty";
                            return;
                }
     for(int i=front;i<rear;i++)
             cout<<a[i]<<" ";
     cout<<a[rear];
}                    
int main()
{
     queue q;
     q.front=-1;
     q.rear=-1;
     int c;
     char ch='y';
     while (ch=='y'||ch=='Y')
     {
           cout<<"Menu: (1)Insert (2)Delete (3)Display : ";
           cin>>c;
           switch(c)
           {
                    case 1: q.insert();
                         break;
                    
                    case 2: q.remove();
                         break;
                    
                    case 3: q.display();
                            break;
                            
                    default: cout<<"\nInvalid Choice! ";
           }
           cout<<"\n continue? ";
           cin>>ch;
     }
     return 0;
}
 
