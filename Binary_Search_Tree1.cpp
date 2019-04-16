#include<iostream>
#include<conio.h>
using namespace std;

void insert(int ,int);
void del();
int search(int,int);
int max(int );
int min(int );

int arr[100];
main()
{     int choice=0,n=0,val;
      int pos=1;
      start:
      system("CLS");
      cout<<"\n1. Insert an array";
      cout<<"\n2. Search a node";
      cout<<"\n3. Delete a node";
      cout<<"\n4. Find maximum value";
      cout<<"\n5. Find minimum value";
      cout<<"\n6. Exit";
      cout<<"\nEnter your choice (1-6) : ";
      cin>>choice;
      pos=1;
      switch(choice)
      {       case 1: cout<<"\nEnter the number of nodes : ";
                      cin>>n;
                      cout<<"\nInput the elements :\n";
                      for(int i=0;i<n;i++)
                      {       cin>>val;
                              insert(val,1);
                      }
                      getch();
                      break;
              case 2:cout<<"\nEnter the node to be searched : ";
                   cin>>val;
                   pos=search(val,1);
                   if(pos!=-1)
                       cout<<"\nElement found at position "<<pos<<"\n";
                   else
                       cout<<"\nElement not found !!!\n";
                   getch();
                   break;
              case 3:del();
                   break;              
              case 4:
                   cout<<"\nMaximum value : "<<max(1)<<"\n";
                   getch();
                   break;
              case 5:
                   cout<<"\nMinimum value : "<<min(1)<<"\n";
                   getch();
                   break;
              case 6:exit(0);
                   break;
              default:exit(1);
                   break;
      }
      goto start;
      getch();
}

void insert(int a,int root)
{    if(arr[root]==0)
     {     arr[root]=a;
           return;
     }
     else if(a<=arr[root])
          insert(a,root*2);
     else
         insert(a,root*2+1);
}

void del()
{    
     int pos=0,pos1=0,node,flag=0;
     cout<<"\nInput the node to be deleted : ";
     cin>>node;
     flag=0;
     for(int i=1;i<21;i++)
     {
             if(arr[i]==node)
             {      flag=1;
                    pos=i;
                    break;
             }
     }
     if(flag==1)
     {
                pos1=pos*2;
                while(arr[pos1*2+1]!=0)
                {
                                     pos1=pos1*2+1;
                }
                arr[pos]=arr[pos1];
                arr[pos1]=0;
                cout<<"\nNode deleted successfully !!\n";
     }
     else
         cout<<"\nNo such node present !!!\n";
     getch();
}    

int search(int a,int root)
{    if(arr[root]==0)
          return -1;
     else if(a==arr[root])
         return root;
     else if(a<=arr[root])
          return search(a,root*2);
     else 
          return search(a,root*2+1);
     return -1;
}

int max(int root)
{   while(arr[root*2+1]!=0)
    {     return max(root*2+1);
    }
    return arr[root];
}

int min(int root)
{   while(arr[root*2]!=0)
    {     return min(root*2);
    }
    return arr[root];
}
