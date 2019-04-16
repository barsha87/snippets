#include <iostream>
#include <conio.h>
using namespace std;

class bfs
{
public :
       int q[50];
int visited[50];
int ar[50][50];
int r,c;
public:
    void accept();
    void bf();
};
void bfs::accept()
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

void bfs::bf()
{
    int start;
    int end;
    cout<<"enter start";
    cin>>start;
    visited[start]=1;
    int rear=0,front=0,i;
    q[++rear]=start;
     while(rear!=front)
    {
        start=q[++front];
        cout<<start<<"    ";
        for(i=1;i<=c;i++)
        {
            if(ar[start][i] && !visited[i])
            {
                q[++rear]=i;
                visited[i]=1;
            }
        }
    }
    

}

int main()
{
    bfs obj;
    obj.accept();
    obj.bf();
    getch();
}
