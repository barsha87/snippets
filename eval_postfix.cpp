#include<iostream>
#include<conio.h>
#include<math.h>
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
    temp=new node;
    temp=top;
    num=top->data;
    top=top->next;
    delete temp;
    return num;
}
main()
{
      char exp[100];
      stack obj;
      int i,a,b,c,t;
      cout<<"enter postfix expression";
      cin>>exp;
      for(i=0;i<strlen(exp);i++)
      {
         if(exp[i]=='+'||exp[i]=='-'||exp[i]=='*'||exp[i]=='/'||exp[i]=='%'||exp[i]=='^')
              {
                    b=obj.pop();
                    a=obj.pop();
                    switch(exp[i])
                    {
                                  case'+':c=a+b;
                                  break;
                                  case'-':c=a-b;
                                  break;
                                  case'*':c=a*b;
                                  case'/':c=a/b;
                                  case'%':c=a%b;
                                  case'^':c=pow(a,b);
                                  break;
                    }
                    obj.push(c);
              }
              else
              t=exp[i];
              obj.push(t-48);
         }
              cout<<"result: "<<c;
              getch();
}
