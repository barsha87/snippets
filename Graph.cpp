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
 void insert(int p)
  {
   q[++tail]=p;
  }
 int dequeue()
  {
   int i,temp=q[0];
   
   for(i=0;i<tail;i++)
    {
     q[i]=q[i+1];
    }
   
   tail--;
   return temp;
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
 int D[MAX+1][MAX+1];
 int n;
 
 public:
 Graph(int);
 void get();
 void print();
 void visitNode(int,int&,int*,int*,char*);
 void bfs(int);
 void dfs(int);
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
       D[i][j]=0;
     else
       D[i][j]=999;
    }
  }
}

void Graph::get()
{
 int i,j,node,nodenum;
 
 for(i=1;i<=n;i++)
  {
   cout<<"\nEnter number of nodes "<<i<<" is connected to:\n";
   cin>>nodenum;
   
   for(j=1;j<=nodenum;j++)
    {
     cout<<"Connected node no."<<j<<": ";
     cin>>node;
     
     D[i][node]=1;
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
     cout<<D[i][j]<<"\t";
    }
   cout<<endl<<endl;
  }
}

void Graph::visitNode(int u,int& time,int* d,int* f,char* color)
{
 int i;
 
 time+=1;
 color[u]='g';
 d[u]=time;
 
 for(i=1;i<=n;i++)
  {
   if(D[u][i]!=999&&D[u][i]!=0&&color[i]=='w')
     visitNode(i,time,d,f,color);     
  }
 
 time+=1;
 f[u]=time;
 color[u]='b';
}

void Graph::bfs(int s)
{
 char color[n+1];
 int p[n+1],d[n+1];
 Queue q;
 
 int i;
 
 for(i=1;i<=n;i++)
  {
   color[i]='w';
   p[i]=0;
   d[i]=0;
  }
  
 q.insert(s);
 
 while(!q.isEmpty())
  {
   int u=q.dequeue();
   color[u]='g';
   
   for(i=1;i<=n;i++)
    {
     if(D[u][i]!=999&&D[u][i]!=0&&color[i]=='w')
        {
         color[i]='g';
         p[i]=u;
         d[i]=d[u]+1;
         q.insert(i);
        }   
    }
   color[u]='b';
  }
  
 cout<<"\n\nNode\tDistance from source\tParent\n";
 
 for(i=1;i<=n;i++)
  {
   cout<<i<<"\t"<<d[i]<<"\t\t\t"<<p[i]<<endl;
  }
 cout<<endl;
}

void Graph::dfs(int s)
{
 char color[n+1];
 int d[n+1],f[n+1],i,time=0;
 
 for(i=1;i<=n;i++)
  {
   color[i]='w';
   d[i]=0;
   f[i]=0;
  }
  
 visitNode(s,time,d,f,color);
 
 cout<<"\n\nNode\tDiscovery Time\tFinishing Time\n";
 
 for(i=1;i<=n;i++)
  {
   cout<<i<<"\t"<<d[i]<<"\t\t"<<f[i]<<endl;
  }
 cout<<endl;
}

int main()
{
 int size,source;
 
 cout<<"Enter size of graph (no. of nodes): ";
 cin>>size;
 cout<<"Enter the source node: ";
 cin>>source;
 
 Graph g(size);
 g.get();
 
 cout<<"\nBREADTH-FIRST SEARCH RESULTS: ";
 g.bfs(source);
 cout<<"\nDEPTH-FIRST SEARCH RESULTS: ";
 g.dfs(source);
 
 getch();
 return 0;
}
