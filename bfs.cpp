#include<iostream.h>
#include<conio.h>
class queue
{
		int a[20] ;
		int front, rear ;

	public :

		queue( ) ;
		void enq ( int n ) ;
		int deq( ) ;
} ;


queue :: queue( )
{
	front = -1 ;
	rear = -1 ;
}


void queue :: enq( int n )
{
	rear++ ;
	a[rear] = n ;

	if ( front == -1 )
		front = 0 ;
}


int queue :: deq( )
{
    int p;
	p = a[front] ;
	a[front] = '\0' ;
    front++ ;
    return p;
}


class graph
{
      char v[20],p[20];
      int gptr[20][20],status[20],n;
      public:
             graph();
             void bfs();
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

void graph::bfs()
{
     queue q;
     int i,j,k;
     q.enq(v[0]);
     status[0]=2;
     for(i=0;i<n;i++)
     {
           p[i]=q.deq();
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
                      q.enq(v[j]);
                      status[j]=2;
                      }
                 
           }
     }
}

void graph::disp()
{
     int i;
     cout<<"\nbreadth first traversed graph:\n";
     for(i=0;i<n;i++)
          cout<<p[i]<<" ";
}           
main()
{
      graph g;
      g.bfs();
      g.disp();
      getch();
}
