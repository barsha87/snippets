#include<iostream.h>
#include<conio.h>
#define MAX 20
#define MAXEDGE 190

class Graph
{
 private:
 int C[MAX+1][MAX+1];
 int E[MAXEDGE+1][3];
 int n;
 int edges;
 
 public:
 Graph(int);
 void swap(int&,int&);
 void get();
 void print();
 void printEdges();
 void makeSet();
 void kruskal();
};

Graph::Graph(int size)
{
 n=size;
 
 int i,j;
 
 for(i=1;i<=n;i++)
  {
   for(j=1;j<=n;j++)
    {
     if(i==j)
       C[i][j]=0;
     else
       C[i][j]=999;
    }
  }
}

void Graph::swap(int& a,int& b)
{
 int temp=a;
 a=b;
 b=temp;
}

void Graph::get()
{
 int i,j,node,nodenum,cost;
 
 for(i=1;i<=n;i++)
  {
   cout<<"\nEnter number of nodes "<<i<<" is connected to:\n";
   cin>>nodenum;
   
   for(j=1;j<=nodenum;j++)
    {
     cout<<"Connected node no."<<j<<": ";
     cin>>node;
     cout<<"Enter node cost: ";
     cin>>cost;
     
     C[i][node]=cost;
    }
  }
}

void Graph::print()
{
 int i,j;
 
 cout<<endl<<endl;
 
 for(i=1;i<=n;i++)
  {
   for(j=1;j<=n;j++)
    {
     cout<<C[i][j]<<"\t";
    }
   cout<<endl<<endl;
  }
}

void Graph::printEdges()
{
 int i;
 
 cout<<edges<<endl;
 
 for(i=1;i<=edges;i++)
  {
   cout<<endl<<E[i][0]<<"->"<<E[i][1]<<" ("<<E[i][2]<<")";
  }
}

void Graph::makeSet()
{
 int i,j,p=0;
 
 for(i=1;i<=n;i++)
  {
   for(j=1;j<=n;j++)
    {
     if(C[i][j]>0&&C[i][j]<999)
        {
         E[++p][0]=i;
         E[p][1]=j;
         E[p][2]=C[i][j];
        }
    }
  }
  
 edges=p;
  
 for(i=1;i<=edges-1;i++)
  {
   for(j=i+1;j<=edges;j++)
    {
     if(E[i][2]>E[j][2])
        {
         swap(E[i][0],E[j][0]);
         swap(E[i][1],E[j][1]);
         swap(E[i][2],E[j][2]);
        }
    }
  }
}

void Graph::kruskal()
{
 makeSet();
 
 int forest[n+1],i,j,temp,length=0;
 
 for(i=1;i<=n;i++)
  {
   forest[i]=i;
  }
 
 cout<<"\n\nThe minimum spanning tree is:";
 
 for(i=1;i<=edges;i++)
  {
   if(forest[E[i][0]]!=forest[E[i][1]])
     {
      temp=forest[E[i][1]];
      
      for(j=1;j<=n;j++)
       {
        if(forest[j]==temp)
           forest[j]=forest[E[i][0]];
       }
       
      length+=E[i][2];
      cout<<endl<<E[i][0]<<"->"<<E[i][1]<<" ("<<E[i][2]<<")";
     }
  }
 cout<<"\n\nMinimum Spanning Length: "<<length<<endl;  
}

int main()
{
 int size;
 
 cout<<"Enter size of graph (no. of nodes): ";
 cin>>size;
 
 Graph g(size);
 g.get();
 g.print();
 g.makeSet();
 g.printEdges();
 g.kruskal();
 
 getch();
 return 0;
}
