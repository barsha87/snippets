#include <iostream>
using namespace std;

class stack
{
      int a[50],n,res;
public:  
      int top;   
      void pop();
      void push();
      void disp();
};
          
void stack::push()
{
    cout<<"\nEnter element: ";
    cin>>n;
    
    if(top==49) 
                res=-1;
    else
    {
        top++;
        a[top]=n;
        res=0;
    }
    
    if (res==-1)
    {
    cout<<"Overflow!! \n";
    }
    
}


void stack::pop()
{
    if(top==-1)
               cout<<"Underflow!! \n";
    else
    {
        res=a[top];
        top--;
        cout<<"\nThe deleted element is: "<<res<<endl;
    }
    
}

void stack::disp()
{
     cout<<"\nThe Stack now is: \n";
                            
     if(top==-1)
                {cout<<"Empty";
                return;}
     cout<<a[top];
     for(int i=top-1;i>=0;i--)
             cout<<" "<<a[i];
}                    


int main()
{
     stack s;
     s.top=-1;
     int c;
     char ch='y';
     while (ch=='y'||ch=='Y')
     {
           cout<<"Enter Choice: (1)Push (2)Pop (3)Display : ";
           cin>>c;
           switch(c)
           {
                    case 1: s.push();
                         break;
                    
                    case 2: s.pop();
                         break;
                    
                    case 3: s.disp();
                            break;
                            
                    default: cout<<"\nInvalid Choice! ";
           }
           cout<<"\n continue? ";
           cin>>ch;
     }
     return 0;
}
 
