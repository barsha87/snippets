#include<iostream.h>
#include<conio.h>
class stack
{
      char a[20];
      int top;
      public:
             void push(char n);
             char pop();
             stack();
};
             
stack::stack()
{
      top=-1;
}
      
void stack::push(char n)
{
       top++;
       a[top]=n;
}
char stack::pop()
{
       char p;
       p=a[top];
       a[top]='\0';
       top--;
       return p;
}

class graph
{
      char v[20],p[20];
      int gptr[20][20],status[20],n;
      public:
             graph();
             void dfs();
             void disp();
};

graph::graph()
{
      int i,j;
      cout<<"no. of vertices in the graph: ";
      cin>>n;
      cout<<"enter nodes:\n";
      for(i=0;i<n;i++)
           {
           cin>>v[i];
           status[i]=1;
           }
      cout<<"\nenter graph:\n ";
      for(i=0;i<n;i++)
           cout<<" "<<v[i];
      cout<<"\n";
      for(i=0;i<n;i++)
      {
            cout<<v[i]<<" ";
            for(j=0;j<n;j++)
                cin>>gptr[i][j];
      }
}

void graph::dfs()
{
     stack s;
     int i,j,k=0;
     char ch;
     s.push(v[0]);
     status[0]=2;
     for(i=0;i<n;i++)
     {
           p[i]=s.pop();
           for(j=0;j<n;j++)
              {
               if(v[j]==p[i])
                   {
                   k=j;
                   break;
                   }
               }
           status[k]=3;
           for(j=0;j<n;j++)
           {
                 if(gptr[k][j]==1 && status[j]==1)
                      {
                      s.push(v[j]);
                      status[j]=2;
                      }
                 
           }
     }
}

void graph::disp()
{
     int i;
     cout<<"\ndepth first traversed graph:\n";
     for(i=0;i<n;i++)
          cout<<p[i]<<" ";
}           
main()
{
      graph g;
      g.dfs();
      g.disp();
      getch();
}
/*no. of vertices in the graph: 9
enter nodes:
a
f c b d
e
g
j
k

enter graph:
  a f c b d e g j k
 0 1 1 1 0 0 0 0 0
 1 0 1 0 1 0 0 0 0
 1 1 0 1 1 1 1 0 0
 1 0 1 0 0 0 1 0 0
 0 1 1 0 0 1 0 1 0
 0 0 1 0 1 0 1 1 1
 0 0 1 1 0 1 0 0 1
 0 0 0 0 1 1 0 0 1
 0 0 0 0 0 1 1 1 0

depth first traversed graph:
a b d g e j k c f

no. of vertices in the graph: 9
enter nodes:
1
2
3
4
5
6
7
8
9

enter graph:
  1 2 3 4 5 6 7 8 9
0 1 1 0 0 0 0 0 0
1 0 0 1 1 0 0 0 0
1 0 0 0 0 1 1 0 0
0 1 0 0 0 0 0 1 1
0 1 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0
0 0 0 1 0 0 0 0 0

depth first traversed graph:
1
*/

