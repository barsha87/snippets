#include<iostream>
#include<conio.h>
using namespace std;

/*struct node
{     int data;
      node *l_child;
      node *r_child;
}*root,*p;
*/
char a[21];

void insert();
void pre_order(int);
void in_order(int);
void post_order(int);

main()
{     start:
      system("CLS");
      int choice;
      cout<<"\n1. Insert a new node";
      cout<<"\n2. In-order traversal";
      cout<<"\n3. Pre-order traversal";
      cout<<"\n4. Post-order traversal";
      cout<<"\n5.Exit";
      cout<<"\nInput your choice (1-5) : ";
      cin>>choice;
      switch(choice)
      {             case 1:insert();
                         break;
                    case 2:in_order(1);
                         getch();
                         break;
                    case 3:pre_order(1);
                         getch();
                         break;
                    case 4:post_order(1);
                         getch();
                         break;
                    case 5:exit(0);
                         break;
      }
      goto start;
      getch();
}
                         
void insert()
{    int pos=-1,flag=0,choice=0,choice1=0;
     char node,ch,parent;
     cout<<"\nInput the node to be inserted : ";
     cin>>node;
     if(a[1]=='\0')
         a[1]=node;
     else
     {   cout<<"\nMake this node as child of : ";
         cin>>parent;
         flag=0;
         for(int i=1;i<=20;i++)
         {       if(a[i]==parent)
                 {       flag=1;
                         pos=i;
                         break;
                 }
         }
         //cout<<flag;
         if(flag==1)
         {          cout<<"\nMake this node as \n";
                    cout<<"\n1. Left child ";
                    cout<<"\n2. Right child ";
                    cout<<"\nInput your choice (1-2) : ";
                    cin>>choice1;
                    switch(choice1)
                    {       case 1 :a[pos*2]=node;
                                 break;
                            case 2 :a[pos*2+1]=node;
                                 break;
                    }
         }
         else
         {   cout<<"\nNo such element present !!!!!!!";
             getch();
             return;
         }
     }
}
 
/*void del()
{    int flag;
     char ele;
     cout<<"\nInput the element to be deleted :";
     cin>>ele;
     flag=0;
     for(int i=1;i<20;i++)
     {       if(a[i]==ele)
             {     flag=1;
                   a[i]='\0';
                   cout<<"\nElement deleted";getch();
                   break;
             }
     }
     if(flag==0)
     {          cout<<"\nElement not in the tree !!";
                getch();
     }
}*/
         
void pre_order(int root)
{    if(root<21)
     {          if(a[root]!=0) cout<<a[root]<<" ";
                pre_order(root*2);
                pre_order(root*2+1);
     }
}

void in_order(int root)
{    if(root<21)
     {          in_order(root*2);
                if(a[root]!=0) cout<<a[root]<<" ";
                in_order(root*2+1);
     }
}

void post_order(int root)
{    if(root<21)
     {          post_order(root*2);
                post_order(root*2+1);
                if(a[root]!=0) cout<<a[root]<<" ";
     }
}

/*void display()
{    system("CLS");
     for(int i=0;i<20;i++)
     {       */


