#include <iostream>
#include <conio.h>
using namespace std;

class dft
{
      public :int r;
              int c;
              int ar[50][50];
              int a[50],temp;
public:  
         dft()
         {top=1;}
      void accept();
      int top;   
      int pop();
      void push(int);
      void disp();
      void traverse();
      int check(int);
};
int dft::check(int n)
{
     for(int i=1;i<=top;++i)
     {
             if(a[i]==n)return 1;
             }
             return 0;
             }
void dft::traverse()
{
    int start,end;
    cout<<"Enter starting node"<<endl;
    cin>>start;
    cout<<"Enter ending node"<<endl;
    cin>>end;
    int i=1;
    int j=1;
    int s;
    push(start);
    while(a[top]!=end && top!=0)
    {
           while(i<=c && a[top]!=end )
           {
                      if(ar[a[top]][i]==1)
                      {
                                       
                                       if(check(i)==0)
                                       {
                                       push(i);
                                       i=1;
                                       }
                                       
                      }
                                       i++;
           }
           disp();
           
           
           
           
           
           if(i>c)
           {
                   i=a[top]+1;
                   pop();
           
           }
           
                        
    }   
    cout<<endl;
    if(top==0)cout<<"no path found";
    else
    disp();
}

void dft::accept()
{
   cout<<"Enter rows"<<endl;
   cin>>r;
   cout<<"Enter colums"<<endl;  
   cin>>c;
   int i,j;
   for(i=1;i<=r;++i)     
   {
                         for(j=1;j<=c;++j)
                         {
                                          cout<<"Element at row "<<i<<" column at "<<j<<"  ";
                                          cin>>ar[i][j];
                                          }
                                          }
                                          }
void dft::push(int n)
{
    
    if(top==49) 
                cout<<"\nOverflow!! \n";
    else
    {
        top++;
        a[top]=n;
    } 
}


int dft::pop()
{
    if(top==0)
               cout<<"\nUnderflow!! \n";
    else
    {
        temp=a[top];
        top--;
    }
    return temp;
    
}

void dft::disp()
{
     cout<<"\nThe Stack is: \n";
                            
     if(top==0)
                return;
     
     for(int i=1;i<=top;i++)
             cout<<"  "<<a[i];
}                    
int main()
{
     dft s;
     s.top=0;
     int c;
     s.accept();
     while(c != 1)
     {
     s.top=0;
     s.traverse();
     cin>>c;
                 }   
     getch();
     return 0;
}
