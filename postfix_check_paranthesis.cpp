#include<iostream>
#include<conio.h>
using namespace std;
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
{
    if(top==NULL)
    return -1;
    int num;
    node *temp;
    temp=top;
    num=top->data;
    top=top->next;
    delete temp;
    return num;
}
main()
{
      int i,flag=1,len;
      char t,exp[20];
      stack a;
      cout<<"enter the expression";
      cin>>exp;
      len=strlen(exp);
      for(i=0;i<len;i++)
      {
                        if(exp[i]=='('||exp[i]=='{'||exp[i]=='[')
                        a.push(exp[i]);
                        if(exp[i]==')'||exp[i]=='}'||exp[i]==']')
                        {
                        t=a.pop();
                        if((exp[i]==')' && t!='c')||(exp[i]=='}' && t!='{')||(exp[i]=']' && t!='['))
                        flag=0;
                        }
      }
      t=a.pop();
      if((flag==1)&&(t==-1))
      cout<<"\nparanthesis is balanced";
      else
      cout<<"\nparanthesis not balanced";
      getch();
}
