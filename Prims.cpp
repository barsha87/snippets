#include<iostream.h>
#include<conio.h>

const int MAX=20;

class Queue
{
 private:
 int q[MAX];
 int tail;
 
 public:
 Queue()
  {
   tail=-1;
  }
 void enqueue(int p)
  {
   q[++tail]=p;
  }
 int extractMin(int key[])
  {
   int i,min=key[q[0]],pos=0,node=q[0];
   
   for(i=1;i<=tail;i++)
    {
     if(min>key[q[i]])
        {
         min=key[q[i]];
         pos=i;
         node=q[i];
        }
    }
    
   for(i=pos;i<tail;i++)
    {
     q[i]=q[i+1];
    }
   
   tail--;
   return node;
  }
 int isExist(int v)
  {
   int i;
   
   for(i=0;i<=tail;i++)
    {
     if(q[i]==v)
       return 1;
    }
   return 0;
  }
 int isEmpty()
  {
   if(tail==-1)
      return 1;
   return 0;
  }
};

class Graph
{
 private:
 int C[MAX+1][MAX+1];
 int n;
 
 public:
 Graph(int);
 void get();
 void print();
 void prims(int);
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

void printArray(int a[],int l,int u)
{
 cout<<endl;
 
 for(int i=l;i<=u;i++)
     cout<<a[i]<<" ";
}

void Graph::prims(int r)
{
 int key[n+1],p[n+1],i,j,u,v,length=0;//key=minimum distance from tree
 Queue q;
 
 for(i=1;i<=n;i++)
  {
   q.enqueue(i);
   key[i]=999;
   p[i]=0;   
  }
 key[r]=0;//since r is a part of the tree
 
 while(!q.isEmpty()) 
  {
   u=q.extractMin(key);
   
   for(v=1;v<=n;v++)
    {
     if(C[u][v]!=0&&C[u][v]!=999)
        {
         printArray(key,1,n);
         cout<<"\t("<<u<<","<<v<<")\t"<<q.isExist(v)<<"\t"<<key[v];
         if(q.isExist(v)&&C[u][v]<key[v])
            {
             key[v]=C[u][v];
             p[v]=u;
            }
        }
    }
  }
 cout<<"\n\nThe minimum spanning tree is:\nNode\tParent";
 
 for(i=1;i<=n;i++)
  {
   cout<<"\n"<<i<<"\t"<<p[i];
   
   if(i==r)
      {
       cout<<" (Root)";
       continue;
      }
   length+=C[i][p[i]];
  }
 cout<<"\n\nMinimum spanning length: "<<length;
}

int main()
{
 int size;
 
 cout<<"Enter size of graph (no. of nodes): ";
 cin>>size;
 
 Graph g(size);
 g.get();
 g.print();
 
 g.prims(1);
 
 getch();
 return 0;
}
