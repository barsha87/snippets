#include<iostream.h>
#include<conio.h>
int main()
{   int a[50][50],i,j,r,c,stack[50];
    cout<<"Enter rows and columns: ";
    cin>>r>>c;
    r++;c++;
    cout<<"Enter the elements: ";
    for(i=1;i<r;i++)
    for(j=1;j<c;j++)
    cin>>a[i][j];
    cout<<"Adjacency matrix is: \n";
    for(i=1;i<r;i++)
    {               for(j=1;j<c;j++)
                    cout<<a[i][j]<<" ";
                    cout<<endl;
    }
    cout<<"\nThe graph traversal is: \n";
    cout<<1<<" ";
    stack[1]=1;
    int s=2;
    for(int k=1;k<r;k++)
    a[k][1]=0;
    for(i=1;i<r;i++)
    {               i=stack[1];
                    for(j=1;j<c;j++)
                    {               if(a[i][j]==1)
                                    {             stack[s++]=j;
                                                  cout<<j<<" ";
                                                  for(int k=1;k<r;k++)
                                                  a[k][j]=0;
                                    }
                                    if(j==c-1)
                                    {         for(int k=1;k<s-1;k++)
                                              stack[k]=stack[k+1];
                                              j=1;
                                              break;
                                    }
                    }
    }
    getch();
    return 0;
}
