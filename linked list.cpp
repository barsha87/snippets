#include<iostream.h>
#include<conio.h>

struct node
{
       int data;
       node *next;
};

class linked_list
{
             node *head;
             public:
             linked_list();
            void insert(int num,int pos);
             int remove(int pos);
             void display();
             int sort();
            
};
      
linked_list::linked_list()
{
                          head=NULL;
}
int linked_list::sort()
{
    int a[50],count=0,c;
    node *t;
    t=head;
    if(head==NULL)
    return 0;
    int i,j,max,min;
    
    while(t!=NULL)
    {
    a[count]=t->data;
    t=t->next;
    count++;
    }
    
    for(i=0;i<count;i++)
    {
    for(j=i+1;j<count;j++)
    {
                          if(a[i]>a[j])
                          {
                                       c=a[i];
                                       a[i]=a[j];
                                       a[j]=c;
                          }
                          
    }
    }
    max=a[count-1];
    cout<<"\nthe maximum value is "<<max;
    min=a[0];
    cout<<"\nthe minimum value is "<<min;
getch();
}






void linked_list::insert(int num,int pos)
{
    
     int count;
     node *temp,*q,*r;
     temp=new node;
     temp->data=num;
     temp->next=NULL;
     if(pos==1)
     {    
          temp->next=head;
          head=temp;
     }
     else
     {
      r=q=head;
      count=1;
     
      while(count<pos)
         {
                     
             r=q;
             if(q==NULL)
             {
             cout<<"position exceeds the size";
             return ;
             }
              q=q->next;
              count++;
         }
         
         r->next=temp;
         temp->next=q;
     }
}




void linked_list::display()
{
 node *q;
 q=head;
 if(q==NULL)
 cout<<"linked list empty";
 
 else
    {
              while(q!=NULL)
              {
                    cout<<"\n"<<q->data;
                    q=q->next;
              }    
    
    
    }   
}

int linked_list::remove(int pos)
{
    int num,count,i;
    node *q,*r;
    
    if(head==NULL)
    return -1;
    
    else if(pos==1)
      {            q=head;
                   num=head->data;
                   head=head->next;
                   delete q;
                   return num;
      }      
    else
    {
         r=q=head;
         count=1;
         while(count<pos)
         {
         r=q;
         if(q==NULL)
             {
              
              return 0;
             }
              q=q->next;
              count++;
         }
                      r->next=q->next;
                      num=q->data;
                      delete q;
                      return num;
    }
}



main()
{     int num,n1,ch,pos;
      linked_list a;
      do
      {
      cout<<"\n\n1.INSERT \n2.REMOVE \n3.DISPLAY \n4.MAXIMUM and MINIMUM\n5.EXIT\n";
      cin>>ch;
      switch(ch)
      {
                case 1:cout<<"\nEnter no to be inserted\n";
                       cin>>num;
                       cout<<"\nEnter position\n";
                       cin>>pos;
                       if(pos<0)
                       cout<<"\n enter proper position";
                       else
                       a.insert(num,pos);
                       break;
                case 2: cout<<"enter the position to be deleted";
                        cin>>pos;
                       if(pos<0)
                       cout<<"\nenter proper position";
                       else
                        {n1=a.remove(pos);
                        if(n1 == -1)
                        cout<<"linked list empty ";
                        else if(n1==0)
                        cout<<"invalid position";
                        else
                        cout<<"\nThe no removed is "<<n1;}
                        break;
                case 3:a.display();
                       break;
                case 4:            n1=a.sort();
                                   if(n1==0)
                                   cout<<"linked list empty";
                                   break;
                case 5:exit(0);
                
      }         
      }while(ch!=4);

}

